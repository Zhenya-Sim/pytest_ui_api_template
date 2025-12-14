import configparser

global_config = configparser.ConfigParser()
global_config.sections()
global_config.read("test_config.ini")


class ConfigProvider:
    def __init__(self):
        self.config = global_config

    def get(self, section: str, prop: str):
        return self.config[section].get(prop)

    def get_int(self, section: str, prop: str):
        return self.config[section].getint(prop)

# получение конкретного значения конкретной секции
    # def get_ui_url(self):
    #     return self.config["ui"].get("base_url")
