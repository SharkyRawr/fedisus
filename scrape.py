from concurrent.futures import ThreadPoolExecutor, as_completed

import urllib3
urllib3.disable_warnings()

import json
from json.decoder import JSONDecodeError

import datetime
import requests
import typing
import tqdm

from quicktype_types import *

from app import app, db
from models import FediInstance

NODEINFO_URL = '/nodeinfo/2.0.json'


def get_nodeinfo(node: str) -> typing.Optional[NodeInfo20]:
    url = 'https://{}{}'.format(node, NODEINFO_URL)

    try:
        r = requests.get(url, timeout=5, verify=False)
        r.raise_for_status()
        obj = json.loads(r.text)
        if isinstance(obj, dict):
            ni = node_info20_from_dict(obj)
            return ni
    except requests.RequestException as rex:
        print(rex)
    except JSONDecodeError as jsonex:
        print(jsonex)


def scrape_host(nodeaddress: str, pb) -> None:
    with app.app_context():
        # check if instance was scraped recently, last 24 hours (?)
        fi = FediInstance.query.filter(FediInstance.Address == nodeaddress).first()
        if fi:
            now = datetime.datetime.utcnow()
            delta = now - fi.modified_at
            if delta.days <= 0:
                pb.write("< cached nodeinfo still valid for " + nodeaddress)
                return

        ni = get_nodeinfo(nodeaddress)
        if ni is None:
            pb.write("got invalid request result")
            fi = FediInstance(Address=nodeaddress, Valid=False)
            db.session.add(fi)
            db.session.commit()
            return

        fi = FediInstance.get_or_create_from_quicktype(nodeaddress, ni)
        pb.write('> ' + nodeaddress or "" + " " + fi.NodeName or "")
        db.session.add(fi)
        db.session.commit()


if __name__ == '__main__':
    instances = []
    with open('instances.txt') as f:
        instances = [a.strip() for a in f.read().replace('\r\n', '\n').split('\n')]
        with tqdm.tqdm(total=len(instances)) as pb:
            with ThreadPoolExecutor(max_workers=8) as ex:
                futures = [ex.submit(scrape_host, url, pb) for url in instances]
                for future in as_completed(futures):
                    result = future.result()
                    pb.update(1)
