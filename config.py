import configparser
from appnames import *

def read_apikey() :
    config = configparser.ConfigParser()
    config.read(config_filename)
    return config[settings_section_name][api_key_name]


def read_url() :
    config = configparser.ConfigParser()
    config.read(config_filename)
    return config[settings_section_name][url_key_name]

