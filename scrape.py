import json
from json.decoder import JSONDecodeError

import sys
import datetime
import requests
import typing

from quicktype_types import *

NODEINFO_URL = '/nodeinfo/2.0.json'


def get_nodeinfo(node: str) -> typing.Optional[NodeInfo20]:
    url = 'https://{}{}'.format(node, NODEINFO_URL)
    print("Trying to fetch:", url)
    
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
                nodeaddress = line

                # check if instance was scraped recently, last 24 hours (?)
                fi = FediInstance.query.filter(FediInstance.Address==nodeaddress).first()
                if fi:
                    now = datetime.datetime.utcnow()
                    delta = now - fi.modified_at
                    if delta.days <= 0:
                        print("< cached nodeinfo still valid")
                        continue

                ni = get_nodeinfo(nodeaddress)
                if ni is None:
                    print("got invalid request result")
                    fi = FediInstance(Address=nodeaddress, Valid=False)
                    db.session.add(fi)
                    db.session.commit()
                    continue

                fi = FediInstance.get_or_create_from_quicktype(nodeaddress, ni)
                print('>', nodeaddress, fi.NodeName)
                db.session.add(fi)
                db.session.commit()

