import json

import requests

from config_dataclass import ConfigData


api_address = "http://" + ConfigData.config_host + ":" + str(ConfigData.config_port)


def get_all_from_db():
    return requests.get(api_address + "/get_all_from_db").json()


def find_by(action, inp):
    inp_data = {"action": action, "inp": str(inp)}
    inp_data = json.dumps(inp_data)
    return requests.post(api_address + "/find_by", data=inp_data).json()


def add_item_to_db(item):
    inp_data = item
    return requests.post(api_address + "/add_item_to_db", json=inp_data).json()


def edit_by_index(item, index):
    inp_data = {'item': item, 'index': index}
    return requests.put(api_address + "/edit_by_index", json=inp_data).json()


def delete_by_index(index):
    inp_data = {'index': index}
    return requests.put(api_address + "/delete_by_index", json=inp_data).json()


def delete_db():
    return requests.delete(api_address + "/delete_db").json()


def restore_db(index=-1):
    inp_data = {'index': index}
    return requests.put(api_address + "/restore_db", json=inp_data).json()
