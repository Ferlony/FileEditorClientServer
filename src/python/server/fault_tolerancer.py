from shutil import copyfile
from os import walk, path, remove
from pathlib import Path

import xxhash

from config_dataclass import ConfigData
from dep_funs import read_file


class FaultTolerancer:

    @staticmethod
    def __walk_in_path() -> list:
        files_list = []
        for root, directories, files in walk(ConfigData.tmp_path):
            for filename in files:
                files_list.append(filename)

        return files_list

    @staticmethod
    def __get_sorted_files_by_modification_date() -> list:
        sorted_files = sorted(Path(ConfigData.tmp_path).iterdir(), key=path.getmtime)
        out = []
        for each in sorted_files:
            out.append(str(each))

        return out

    @staticmethod
    def __copy_db():
        item_contents = read_file(ConfigData.db_path)
        copyfile(ConfigData.db_path,
                 ConfigData.tmp_path + f"{xxhash.xxh3_128_hexdigest(item_contents)}.txt")

    def __control_bp_amount(self):
        max_amount = 10
        items_amount = len(self.__walk_in_path())
        if items_amount < max_amount:
            return
        elif items_amount == max_amount:
            sorted_files = self.__get_sorted_files_by_modification_date()
            remove(sorted_files[0])
            return
        else:
            raise Exception

    def copy_db(self):
        self.__control_bp_amount()
        self.__copy_db()

    def restore_db(self, ind: int):
        sorted_files = self.__get_sorted_files_by_modification_date()
        copyfile(sorted_files[ind], ConfigData.db_path)
        return "DB restored successfully"
