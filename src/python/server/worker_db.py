from multipledispatch import dispatch

from models import DBModel
from dep_funs import *
from decorators import find_by_decorator


class WorkerDB:
    def __init__(self, db_path):
        self.db_path = db_path

    db_format = "{};{};{};{};{};{};{};{};{};{};{}"

    @staticmethod
    def _gen_item_contains(item: DBModel) -> str:
        out = (
               "title: {}\n"
               "author: {}\n"
               "genre: {}\n"
               "year: {}\n"
               "width: {}\n"
               "height: {}\n"
               "cover: {}\n"
               "source: {}\n"
               "buy_date: {}\n"
               "read_date: {}\n"
               "rating: {}")
        return out.format(item.title, item.author,
                          item.genre, item.year, item.width,
                          item.height, item.cover, item.source,
                          item.buy_date, item.read_date, item.rating)

    @staticmethod
    def _create_item_from_string(item: str) -> DBModel:
        item_list = item.strip('\n').split(";")
        item_contains = {"title": item_list[0],
                         "author": convert_string_list_to_list(item_list[1]),
                         "genre": convert_string_list_to_list(item_list[2]),
                         "year": item_list[3],
                         "width": item_list[4],
                         "height": item_list[5],
                         "cover": item_list[6],
                         "source": item_list[7],
                         "buy_date": item_list[8],
                         "read_date": item_list[9],
                         "rating": item_list[10]}
        db_item = DBModel(**item_contains)
        return db_item

    def __create_db(self):
        create_file(self.db_path)

    def get_last_index(self):
        counter = 0
        with open(self.db_path) as f:
            for each in f.readlines():
                counter += 1
        return counter

    def remove_db(self):
        return

    def add_item_to_db(self, item: DBModel):
        self.__create_db()
        index = self.get_last_index()
        formated_string = self.db_format.format(item.title, item.author,
                                                item.genre, item.year, item.width,
                                                item.height, item.cover, item.source,
                                                item.buy_date, item.read_date, item.rating)

        write_to_file(formated_string + "\n", self.db_path)
        return "Item added successfully"

    def get_all_from_db(self) -> list:
        db_list = read_all_from_file(self.db_path)
        out = []
        for count, each in enumerate(db_list):
            item = self._create_item_from_string(each)
            out.append(self._gen_item_contains(item))
        return out

    @find_by_decorator
    def find_by_title(self, name, item: DBModel = None):
        if name.lower() in item.title:
            return True

    @find_by_decorator
    def find_by_genre(self, name, item: DBModel = None):
        if name in item.genre:
            return True

    @find_by_decorator
    def find_by_author(self, name, item: DBModel = None):
        if name in item.author:
            return True

    @dispatch(str)
    def find_by_field(self, name: str) -> list:
        db_list = read_all_from_file(self.db_path)
        out = []
        for count, each in enumerate(db_list):
            item = self._create_item_from_string(each)
            if name in each:
                out.append(self._gen_item_contains(item))
        return out

    @dispatch(int)
    def find_by_id(self, index: int) -> list:
        db_list = read_all_from_file(self.db_path)
        out = []
        for count, each in enumerate(db_list):
            item = self._create_item_from_string(each)
            if count == index:
                out.append(self._gen_item_contains(item))
                break
        return out

    def edit_by_index(self, index: int, item: DBModel):
        formated_string = self.db_format.format(item.title, item.author,
                                                item.genre, item.year, item.width,
                                                item.height, item.cover, item.source,
                                                item.buy_date, item.read_date, item.rating)
        db_list = read_all_from_file(self.db_path)
        db_list[index] = formated_string + "\n"
        rewrite_all_list_to_file(db_list, self.db_path)
        return "Item edited successfully"

    def delete_by_index(self, index: int):
        db_list = read_all_from_file(self.db_path)
        del db_list[index]
        rewrite_all_list_to_file(db_list, self.db_path)
