from datetime import datetime

from dep_funs import print_enumerable_beauty, specials, numbers
from decorators import simple_exception_decorator
from requests_api import *

from enums import FindByActionsEnum
from items_generator import ItemGenerator


class Menus:

    @staticmethod
    def __add_items_to_list_menu(name: str) -> list:
        items = []
        while True:
            print("Choose action:\n"
                  f"'1' Add {name}\n"
                  "'0' End")
            a = input()
            if a == "1":
                item = input(f"Enter {name}:\n")
                if item:
                    items.append(item)
                    print(f"{name} added")
                else:
                    print("Wrong input")
            elif a == "0":
                break
            else:
                print("Wrong input")

        return items

    def __enter_item_db(self):
        while True:
            flag1 = True
            flag2 = True
            title = input("Enter title:\n")

            for i in range(0, len(specials)):
                if specials[i] in title:
                    print("Wrong input")
                    flag1 = False
                    break

            for each in numbers:
                if each in title:
                    print("Wrong input")
                    flag2 = False
                    break
            if flag1 and flag2:
                break

        while True:
            flag1 = True
            flag2 = True
            authors = self.__add_items_to_list_menu("author")
            for each in authors:
                for i in range(0, len(specials)):
                    if specials[i] in each:
                        print("Wrong input")
                        flag1 = False
                        break
                for each_ in numbers:
                    if each_ in each:
                        print("Wrong input")
                        flag2 = False
                        break
            if flag1 and flag2:
                break

        while True:
            flag1 = True
            flag2 = True
            genres = self.__add_items_to_list_menu("genre")
            for each in genres:
                for i in range(0, len(specials)):
                    if specials[i] in each:
                        print("Wrong input")
                        flag1 = False
                        break
                for each_ in numbers:
                    if each_ in each:
                        print("Wrong input")
                        flag2 = False
                        break
            if flag1 and flag2:
                break

        year = int(input("Enter year:\n"))
        width = int(input("Enter width:\n"))
        height = int(input("Enter height:\n"))

        cover = None
        while True:
            print("Choose cover:\n"
                  "'1' Hard\n"
                  "'2' Soft")
            a = input()
            if a == '1':
                cover = "hard"
                break
            elif a == '2':
                cover = "soft"
                break
            else:
                print("Wrong input")

        source = None
        while True:
            print("Choose source:\n"
                  "'1' Bought\n"
                  "'2' Present\n"
                  "'3' heritage")
            a = input()
            if a == '1':
                source = "bought"
                break
            elif a == '2':
                source = "present"
                break
            elif a == '3':
                source = "heritage"
                break
            else:
                print("Wrong input")

        buy_date = input("Enter buy_date:\n")
        read_date = input("Enter read_date:\n")
        rating = int(input("Enter raiting:\n"))

        item_contains = {"title": title, "author": authors, "genre": genres,
                         "year": year, "width": width, "height": height,
                         "cover": cover, "source": source, "buy_date": buy_date,
                         "read_date": read_date, "rating": rating}

        buy_date = datetime.strptime(buy_date, "%d-%m-%Y").date()
        print(type(buy_date))
        print(buy_date.year)
        if buy_date.year >= int(year):
            return item_contains
        else:
            raise Exception("Wrong date")

    def main(self):
        while True:
            print("Choose option:\n"
                  "'1' Get all in db\n"
                  "'2' Find item by field\n"
                  "'3' Add new item\n"
                  "'4' Gen items to db\n"
                  "'5' Edit item by index\n"
                  "'6' Delete item by index\n"
                  "'7' Delete db\n"
                  "'8' Restore db\n"
                  "'t' test\n"
                  "'0' Exit")
            a = input()
            if a == '1':
                print_enumerable_beauty(get_all_from_db())
            elif a == '2':
                self.__find_by_field_menu()
            elif a == '3':
                self.__add_item_menu()
            elif a == '4':
                self.__add_item_gen_menu()
            elif a == '5':
                self.__edit_item_by_index_menu()
            elif a == '6':
                self.__delete_item_by_index_menu()
            elif a == '7':
                print(delete_db())
            elif a == '8':
                self.__restore_db_menu()
            elif a == '0':
                return
            elif a == 't':
                self.add_test_item()
            else:
                print("Wrong input")

    @staticmethod
    def __restore_db_menu():

        while True:
            print("Choose option:\n"
                  "'1' Restore last bp\n"
                  "'2' Restore by index\n"
                  "'0' Back")
            a = input()

            if a == '1':
                print(restore_db())
            elif a == '2':
                try:
                    b = int(input("Enter index > -1 or index < 11:\n"))
                    if (b > -1) and (b < 11):
                        print(restore_db(b))
                        return
                    else:
                        raise Exception("Wrong input")
                except Exception as e:
                    print(e)
            elif a == '0':
                return
            else:
                print("Wrong input")

    @staticmethod
    def add_test_item():
        title = "testtitle"
        authors = ["auth", "newauth"]
        genres = ["action", "scifi"]
        year = 2009
        width = 123
        height = 321
        cover = "Soft"
        source = "Bought"
        buy_date = "12-05-2003"
        read_date = "13-06-2004"
        rating = 5

        item_contains = {"title": title, "author": authors, "genre": genres,
                         "year": year, "width": width, "height": height,
                         "cover": cover, "source": source, "buy_date": buy_date,
                         "read_date": read_date, "rating": rating}

        print(add_item_to_db(item_contains))

    @staticmethod
    def __add_item_gen_menu():
        while True:
            a = input("Choose action:\n"
                      "'1' Add without pseudo\n"
                      "'2' Add 10k with pdeudo\n"
                      "'0' Back\n")
            if a == '1':
                n = int(input("Enter items amount to gen:\n"))
                items = ItemGenerator().gen_item_json(n)
                for count, each in enumerate(items):
                    print(f"{add_item_to_db(each)} {count + 1} / {n}")
            elif a == '2':
                items = ItemGenerator().gen_items_json_with_pseudo_random()
                n = len(items)
                for count, each in enumerate(items):
                    print(f"{add_item_to_db(each)} {count + 1} / {n}")
            elif a == '0':
                return
            else:
                print("Wrong input")

    @staticmethod
    def __delete_item_by_index_menu(args=None):
        index = int(input("Enter index:\n"))
        print(delete_by_index(index))

    @staticmethod
    def __find_by_field_menu():
        while True:
            print("Choose option:\n"
                  "'1' By index\n"
                  "'2' By title\n"
                  "'3' By genre\n"
                  "'4' By author\n"
                  "'0' Back")
            a = input()
            if a == '1':
                inp = int(input("Enter index:\n"))
                print_enumerable_beauty(find_by(FindByActionsEnum.index.value, inp))
            elif a == '2':
                inp = input("Enter title:\n")
                print_enumerable_beauty(find_by(FindByActionsEnum.title.value, inp))
            elif a == '3':
                inp = input("Enter genre:\n")
                print_enumerable_beauty(find_by(FindByActionsEnum.genre.value, inp))
            elif a == '4':
                inp = input("Enter author:\n")
                print_enumerable_beauty(find_by(FindByActionsEnum.author.value, inp))
            elif a == '0':
                return
            else:
                print("Wrong input")

    @simple_exception_decorator
    def __add_item_menu(self):
        item = self.__enter_item_db()
        print(add_item_to_db(item))

    @simple_exception_decorator
    def __edit_item_by_index_menu(self):
        index = int(input("Enter index:\n"))
        item = self.__enter_item_db()
        print(edit_by_index(item, index))
