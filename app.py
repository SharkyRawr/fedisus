from models import FediInstance
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from db import db

app = Flask('fedisus')
app.config.from_envvar('FEDISUS_CONFIG', True)
app.config.from_object('settings')
db.init_app(app)


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
    }

    return render_template('simple_index.html', **ctx)



if __name__ == '__main__':
    from models import FediInstance
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(debug=True)
