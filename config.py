# import configparser
import json
from appnames import *

def load_settings() :
# Open the app.json file in read mode
    with open(config_filename, read_mode) as f:
        # Parse the file content to a dictionary
        app = json.load(f)
        return app


def read_apikey() :
    # config = configparser.ConfigParser()
    # config.read(config_filename)
    config = load_settings()
    return config[settings_section_name][api_key_name]


def read_url() :
    # config = configparser.ConfigParser()
    # config.read(config_filename)
    config = load_settings()
    return config[settings_section_name][url_key_name]


def read_dbconnstring() :
    # config = configparser.ConfigParser()
    # config.read(config_filename)
    config = load_settings()
    return config[settings_section_name][database_key_name]


