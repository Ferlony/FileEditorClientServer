from os import path, sep

import configparser
from dataclasses import dataclass


@dataclass
class ConfigData:
    local_path = path.dirname(path.abspath(__file__)) + sep + "local" + sep
    tmp_path = local_path + "tmp" + sep

    db_name = "db.txt"
    db_path = local_path + db_name

    config = configparser.ConfigParser()
    config.read("config.ini")
    config_host = str(config["DEFAULT"]["host"])
    config_port = int(config["DEFAULT"]["port"])

    config_logging = int(config["DEFAULT"]["logging_use"])
    if config_logging == 0:
        config_logging = False
    else:
        config_logging = True

