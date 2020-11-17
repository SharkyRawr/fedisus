import json

import requests

from instances import JUST_A_RANDOM_LIST_OF_INSTANCES
from quicktype_types import *

NODEINFO_URL = '/nodeinfo/2.1.json'


def get_nodeinfo(node: str) -> NodeInfo:
    r = requests.get('https://{}{}'.format(node, NODEINFO_URL))
    r.raise_for_status()

    ni = node_info_from_dict(json.loads(r.text))

    return ni


if __name__ == '__main__':
    from app import app, db
    from models import FediInstance
    with app.app_context():

        for nodeaddress in JUST_A_RANDOM_LIST_OF_INSTANCES:
            ni = get_nodeinfo(nodeaddress)

            fi = FediInstance.get_or_create_from_quicktype(nodeaddress, ni)
            db.session.add(fi)
            db.session.commit()
