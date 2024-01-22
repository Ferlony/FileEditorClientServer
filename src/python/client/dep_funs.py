import json
from os import path
from string import punctuation


specials = punctuation.split()
numbers = " ".join([str(i) for i in range(0, 10)]).split(" ")


def print_enumerable_beauty(some_list):
    try:
        for count, each in enumerate(some_list):
            print(f"index: {count}")
            print(each)
            print()
    except Exception as e:
        print(some_list)


def encode_item_to_json(item) -> json:
    return json.JSONEncoder().encode(item)


def read_file(file_path) -> str:
    if not path.exists(file_path):
        raise Exception("File not exists")
    with open(file_path, "r") as f:
        return f.read()
