import json
import typing
from collections import OrderedDict
from models import FediInstance
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from db import db

app = Flask('fedisus')
app.config.from_envvar('FEDISUS_CONFIG', True)
app.config.from_object('settings')
db.init_app(app)

def count_reject_popularity(instances: typing.List[FediInstance], only_more_than_one=True):
        import operator
        r = {}
        for i in instances:
            rej = i.MRF_Reject.split(', ')
            for reject in rej:
                if reject in r:
                    r[reject] += 1
                else:
                    r[reject] = 1

        if only_more_than_one:
            for k in list(r.keys()):
                if r[k] <= 1:
                    del r[k]
        return OrderedDict(sorted(r.items(), key=operator.itemgetter(1), reverse=True))

@app.route('/')
def index():

    with_reject = FediInstance.query.filter(FediInstance.MRF_Reject != None)

    ctx = {
        'stats': {
            'numinstances': FediInstance.query.count(),
            'nummrf': FediInstance.query.filter(FediInstance.MRF_Policies != None).count(),
            'numreject': with_reject.count(),
        },
        'rejects': with_reject.all(),
        'reject_popularity': count_reject_popularity(with_reject.all()),
        'last_update': FediInstance.query.order_by(FediInstance.modified_at.desc()).first().modified_at
    }

    return render_template('simple_index.html', **ctx)


@app.route('/rejects.json')
def rejects_json():
    with_reject = FediInstance.query.filter(FediInstance.MRF_Reject != None)
    num = with_reject.count()

    reject_stats = count_reject_popularity(with_reject.all(), only_more_than_one=False)
    res = dict(reject_stats)
    

    return json.dumps(res)



if __name__ == '__main__':
    from models import FediInstance
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(debug=True)
