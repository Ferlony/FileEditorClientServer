from dep_funs import read_all_from_file


def find_by_decorator(fun):
    def inner_fun(self, name, item=None):
        db_list = read_all_from_file(self.db_path)
        out = []
        for count, each in enumerate(db_list):
            item = self._create_item_from_string(each)
            if fun(self, name, item):
                out.append(self._gen_item_contains(item, count))
        return out
    return inner_fun
