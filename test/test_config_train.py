import configparser


def test_conf_A():
    config = configparser.ConfigParser()
    config.sections()

    config.read('test_config_train.ini')
    config.sections()
    prop = config["sectionA"]["prop"]  # значение строка
    prop_int = config["sectionA"].getint("prop_int")  # значение как число
    print(prop)
    print(prop_int / 1)


def test_conf_C():
    config = configparser.ConfigParser()
    config.sections()

    config.read('test_config_train.ini')

    prop = config["sectionC"].getboolean("prop_bool")  # логическое значение
    if (prop):
        print("корректно считалось")
