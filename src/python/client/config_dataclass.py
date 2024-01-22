import configparser
from dataclasses import dataclass


@dataclass
class ConfigData:
    config = configparser.ConfigParser()
    config.read("config.ini")
    config_host = str(config["DEFAULT"]["host"])
    config_port = int(config["DEFAULT"]["port"])
