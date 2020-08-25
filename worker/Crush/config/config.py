from configparser import ConfigParser
import os


class Config(object):
    __file_name = 'config.ini'
    __config_public_values = None

    @classmethod
    def get_public_item(cls, key):
        cls.__config_public_values = Config.__fetch_ini_section('public')
        return cls.__config_public_values[key]

    @classmethod
    def set_public_item(cls, key, value):
        cls.__set_ini_section('public', key, value)

    @classmethod
    def __fetch_ini_section(cls, section):
        """Get dictionary containing information from section in ini file
        :param filename: ini file to get data from.
        :param section: section of ini file to get data from.
        :return dictionary holding data from requested section/file in form"""
        # create a parser
        parser = ConfigParser()
        parser.optionxform = str
        # read config file
        try:
            parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), cls.__file_name))
        except Exception:
            raise Exception('Error parsing file "{0}" '.format(cls.__file_name))
        # get section, default to account_info
        config_dict = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                config_dict[param[0]] = param[1]
        else:
            raise Exception('Section "{0}" not found in the file "{1}" '.format(section, cls.__file_name))
        return config_dict

    @classmethod
    def __set_ini_section(cls, section, key, value):
        # create a parser
        parser = ConfigParser()
        parser.optionxform = str
        file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), cls.__file_name)
        # read config file
        try:
            parser.read(file_path)
        except Exception:
            raise Exception('Error parsing file "{0}" '.format(cls.__file_name))
        # get section, default to account_info
        if parser.has_section(section):
            parser.set(section, key, value)
            with open(file_path, 'wb') as configfile:
                parser.write(configfile)
        else:
            raise Exception('Section "{0}" not found in the file "{1}" '.format(section, cls.__file_name))



