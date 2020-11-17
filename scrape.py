import json
import json.decoder

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
    except json.decoder.JSONDecodeError as jsonex:
        print(jsonex)


if __name__ == '__main__':
    from app import app, db
    from models import FediInstance
    with app.app_context():
        with open('instances.txt') as f:
            while (line := f.readline().strip()) is not None:
                nodeaddress = line
                ni = get_nodeinfo(nodeaddress)
                if ni is None:
                    print("skip invalid request result")
                    continue

                fi = FediInstance.get_or_create_from_quicktype(nodeaddress, ni)
                print('>', nodeaddress, fi.NodeName)
                db.session.add(fi)
                db.session.commit()

