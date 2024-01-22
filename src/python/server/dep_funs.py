from os import path, remove


def write_to_file(item, file_path):
    if not path.exists(file_path):
        raise Exception("File not exists")

    with open(file_path, 'a') as f:
        f.write(item)


def rewrite_all_list_to_file(items: list, file_path):
    if not path.exists(file_path):
        raise Exception("File not exists")

    with open(file_path, 'w') as f:
        for each in items:
            f.write(each)


def read_all_from_file(file_path) -> list:
    if not path.exists(file_path):
        raise Exception("File not exists")

    out = []
    with open(file_path, "r") as f:
        for each in f.readlines():
            out.append(each)
    return out


def read_file(file_path) -> str:
    if not path.exists(file_path):
        raise Exception("File not exists")
    with open(file_path, "r") as f:
        return f.read()


def create_file(file_path):
    if not path.exists(file_path):
        with open(file_path, 'w') as f:
            pass


def remove_file(file_path):
    if path.exists(file_path):
        remove(file_path)
        return 0


def convert_string_list_to_list(item: str) -> list:
    return eval(item)
