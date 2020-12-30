import json
from json.decoder import JSONDecodeError

import sys
import datetime
import requests
import typing
import tqdm

from quicktype_types import *

NODEINFO_URL = '/nodeinfo/2.0.json'


def get_nodeinfo(node: str) -> typing.Optional[NodeInfo20]:
    url = 'https://{}{}'.format(node, NODEINFO_URL)
    
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        obj = json.loads(r.text)
        if isinstance(obj, dict):
            ni = node_info20_from_dict(obj)
            return ni
    except requests.RequestException as rex:
        print(rex)
    except JSONDecodeError as jsonex:
        print(jsonex)


if __name__ == '__main__':
    from app import app, db
    from models import FediInstance
    with app.app_context():
        with open('instances.txt') as f:
            while (line := f.readline().strip()) != "":
                with tqdm.tqdm() as pb:
                    nodeaddress = line
                    pb.update()

                    # check if instance was scraped recently, last 24 hours (?)
                    fi = FediInstance.query.filter(FediInstance.Address==nodeaddress).first()
                    if fi:
                        now = datetime.datetime.utcnow()
                        delta = now - fi.modified_at
                        if delta.days <= 0:
                            pb.write("< cached nodeinfo still valid for " + nodeaddress)
                            continue

                    ni = get_nodeinfo(nodeaddress)
                    if ni is None:
                        pb.write("got invalid request result")
                        fi = FediInstance(Address=nodeaddress, Valid=False)
                        db.session.add(fi)
                        db.session.commit()
                        continue

                    fi = FediInstance.get_or_create_from_quicktype(nodeaddress, ni)
                    pb.write('> ' + nodeaddress or "" + " " + fi.NodeName or "")
                    db.session.add(fi)
                    db.session.commit()

