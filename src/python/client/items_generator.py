from random import randint
from datetime import datetime
from json import loads

from dep_funs import read_file


class ItemGenerator:

    N = 9999999
    Max_N = 5

    @staticmethod
    def _add_pseudo_random():
        pseudo_list = loads(read_file("books.json"))
        return pseudo_list

    @staticmethod
    def __choose_random_from_cover_menu() -> str:
        r = randint(1, 2)
        if r == 1:
            return "Hard"
        else:
            return "Soft"

    @staticmethod
    def __choose_random_from_source_menu() -> str:
        r = randint(1, 3)
        if r == 1:
            return "Bought"
        elif r == 2:
            return "Present"
        else:
            return "Heritage"

    @staticmethod
    def __gen_random_datetime(bg_year, end_year):
        time_format = '%d-%m-%Y'

        def correct_time(inp: int):
            if inp < 10:
                return "0" + str(inp)
            else:
                return inp

        str_time = f"{correct_time(randint(1, 28))}-{correct_time(randint(1, 12))}-{randint(bg_year, end_year)}"
        rand_time = datetime.strptime(str_time, time_format).date()
        return str(rand_time)

    @staticmethod
    def __gen_random_int(N) -> int:
        return randint(1, N)

    def __gen_random_str_list(self) -> list:
        return [str(randint(1, self.N)) for i in range(0, randint(1, self.Max_N))]

    def __gen_random_str_int(self) -> str:
        return str(randint(1, self.N))

    def gen_item_json(self, items_amount: int) -> list:
        out = []
        for i in range(0, items_amount):
            title = self.__gen_random_str_int()
            authors = self.__gen_random_str_list()
            genres = self.__gen_random_str_list()
            year = self.__gen_random_str_int()
            width = self.__gen_random_int(self.N)
            height = self.__gen_random_int(self.N)
            cover = self.__choose_random_from_cover_menu()
            source = self.__choose_random_from_source_menu()
            buy_date = self.__gen_random_datetime(1900, 2000)
            read_date = self.__gen_random_datetime(2001, 2024)
            rating = self.__gen_random_int(5)

            item_contains = {"title": title, "author": authors, "genre": genres,
                             "year": year, "width": width, "height": height,
                             "cover": cover, "source": source, "buy_date": buy_date,
                             "read_date": read_date, "rating": rating}

            out.append(item_contains)

        return out

    def gen_items_json_with_pseudo_random(self) -> list:
        out = []
        items_amount = 10000
        pseudo_items = self._add_pseudo_random()
        for each in pseudo_items:
            title = each['title']
            authors = [each['author']]
            genres = self.__gen_random_str_list()
            year = each['year']
            width = self.__gen_random_int(self.N)
            height = self.__gen_random_int(self.N)
            cover = self.__choose_random_from_cover_menu()
            source = self.__choose_random_from_source_menu()
            buy_date = self.__gen_random_datetime(1900, 2000)
            read_date = self.__gen_random_datetime(2001, 2024)
            rating = self.__gen_random_int(5)

            item_contains = {"title": title, "author": authors, "genre": genres,
                             "year": year, "width": width, "height": height,
                             "cover": cover, "source": source, "buy_date": buy_date,
                             "read_date": read_date, "rating": rating}

            out.append(item_contains)

        return out + self.gen_item_json(items_amount - len(out))
