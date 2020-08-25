import datetime
import time
import os
import shutil
import sys
from datetime import timedelta
from mako.lookup import TemplateLookup
from mako.lookup import Template
import zipfile
from collections import OrderedDict
from common import Constants
from dateutil import parser



class Tools:

    @staticmethod
    def current_date_plus_X_days(days, format):
        date = datetime.datetime.now() + timedelta(days=days)
        return date.strftime(format)

    @staticmethod
    def fetch_template(template_directory, template_file_name={}):
        """ Fetches the template object using mako

        :param str template_directory: the directory made using the relative path
        :param str template_file_name: the name of the tmeplate file

        :rtype: Template
        :return: Grabs the template from a file
        """
        template_path = Tools.build_relative_directory_path(template_directory)
        print(template_path)
        template_lookup = TemplateLookup(
            directories=template_path, input_encoding='utf-8')
        return template_lookup.get_template(template_file_name)

    @staticmethod
    def build_relative_directory_path(directory_name):
        """Finds the relative path of the directory and creates a temporary python path to the location

        :param str directory_name: the name of the directory

        :rtype: uri
        :return: The relative location of the directory
        """
        COMBINED_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), directory_name)
        # sys.path.insert(0, COMBINED_PATH)
        return COMBINED_PATH

    @staticmethod
    def render_template(template_content, template_tags):
        """ Renders template using a conversion dictionary

        :param Template template_content:
        :param dict, list template_tags:

        :rtype: str
        :return:the template rendered as a string
        """
        try:
            if sys.version_info[0] >= 3:
                return template_content.render(**template_tags)
            else:
                return template_content.render(**template_tags).encode('ascii', 'ignore').replace("\r\n", "\n")
        except Exception as e:
            print("Could not render template: " + str(e))

    @staticmethod
    def remove_folder(folder):
        try:
            shutil.rmtree(folder)
        except Exception as e:
            print("Error when remove folder %s : %s " % (folder, str(e)))
            return None

    @staticmethod
    def compress_to_zip_file_(file_path):
        """
        compress xml file to zip file
        :param str file_name:
        :rtype: str
        :return: gz file full path
        """
        zip_file_name = '%s.zip' % file_path
        try:
            azip = zipfile.ZipFile(zip_file_name, 'w')
            azip.write(file_path, zip_file_name, compress_type=zipfile.ZIP_DEFLATED)
            azip.close()
            return zip_file_name

        except Exception as e:
            raise Exception("Error when compress to gz file: " + str(e))

    @staticmethod
    def clear_invalid_file(upload_path):
        if os.path.exists(upload_path):
            for file in os.listdir(upload_path):
                if file.endswith('.invalid'):
                    os.remove(os.path.join(upload_path, file))

    @staticmethod
    def check_invalid_file_exists(upload_path):
        if os.path.exists(upload_path):
            for file in os.listdir(upload_path):
                if file.endswith('.invalid'):
                    return True
            return False
        else:
            return False

    @staticmethod
    def formatted_date(date, date_format):
        """ Will format a date object

        :param datetime.datetime, str date:
        :param str date_format:

        :rtype: str
        :return: formatted date
        """
        if isinstance(date, str):
            date = Tools.date_from_string(date)
        if date is not None and date_format is not None:
            return Tools.zero_padding_update(date, date_format)
        else:
            return date

    @staticmethod
    def date_from_string(date_string):
        """Will turn a date into a string

        :param str date_string: a date

        :rtype: datetime.datetime
        :return: a date that is now a string
        """
        try:
            return parser.parse(date_string)
        except Exception as e:
            print(e)
            return None

    @staticmethod
    def zero_padding_update(date, date_format):
        """ Fixes notation for zero padding across OS - windows -> other

              :param datetime.datetime, str date:
              :param str date_format:

              :rtype: str
              :return: formatted date
        """
        try:
            return datetime.datetime.strftime(date, date_format)
        except Exception as e:
            if date_format.find('#'):
                updated_date_format = date_format.replace('#', '-')
                final_date = datetime.datetime.strftime(date, updated_date_format)
                return final_date
            if date_format.find('-'):
                updated_date_format = date_format.replace('-', '#')
                final_date = datetime.datetime.strftime(date, updated_date_format)
                return final_date
            else:
                print(str(e) + "Date Format Error")

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

    @staticmethod
    def dict_sort_by_key(dict):
        new_dict = OrderedDict()
        keys = sorted(dict.keys())
        for key in keys:
            new_dict[key] = dict[key]

        return new_dict

    @staticmethod
    def compare_entity_list(entity, list_1, list_2):
        if entity == 'Demographics':
            id = 'firstName'
        else:
            id = 'id'

        for row_1 in list_1:
            row_2 = Tools.find_entity_in_list_by_value(list_2, id, row_1[id])
            Tools.compare_dictionary_content(row_1, row_2)

    @staticmethod
    def find_entity_in_list_by_value(list, key, value):
        for row in list:
            if row[key] == value:
                return row

    @staticmethod
    def compare_dictionary_content(first_dict, second_dict, exact=False):
        """ Compare dictionaries and return True or False
        If exact is False, only need to verify fist_dict items

        :param first_dict:
        :param second_dict:
        :param exact: whether to compare dictionary exactly. default is False.
        :return:
        """

        if exact == True and list.sort(first_dict.keys()) != list.sort(second_dict.keys()):
            print('\033[32;0mFirst dictionary keys : {0}'.format(list.sort(first_dict.keys())))
            print('Second dictionary keys: {0}'.format(list.sort(second_dict.keys())))
            return
        else:
            first_dict = Tools.lower_dict_keys(first_dict)
            second_dict = Tools.lower_dict_keys(second_dict)

        for key, value in first_dict.items():
            # Ignore type info when comparing datetime variable with others
            if not key in second_dict:
                print('\033[31;0mSecond dictionary do not have [{key}]\033[0m'.format(key=key))
                print('\033[31;0mFirst dictionary: {key}:{value}\033[0m'.format(key=key,value=value))
                continue
            if isinstance(value, (datetime.date, datetime.datetime)) or \
                    isinstance(second_dict[key], (datetime.date, datetime.datetime)) or \
                    'date' in key or 'firstvisit' == key or 'lastvisit' == key or 'birthday' in key:

                if len(value) < 11 or len(second_dict[key]) < 11:
                    time_format = Constants.DAY_FORMAT
                else:
                    time_format = Constants.TEMPLATE_TIMEZONE_DATE_FORMAT
                first_value = Tools.formatted_date(value, time_format)
                second_value = Tools.formatted_date(second_dict[key], time_format)
                if len(first_value) > len(second_value):
                    first_value = first_value[0:len(second_value)]
                if len(first_value) < len(second_value):
                    second_value = second_value[0:len(first_value)]
            else:
                first_value = str(value)
                second_value = str(second_dict[key])

            if 'phone' in key:
                first_value = first_value.replace('(','').replace(')','').replace('-','')
                second_value = second_value.replace('(', '').replace(')', '').replace('-', '')

            if first_value != second_value:
                print('\033[31;0mFirst dictionary :{key}:{value}\033[0m'.format(key=key, value=first_value))
                print('\033[31;0mSecond dictionary:{key}:{value}\033[0m'.format(key=key, value=second_value))


    @staticmethod
    def lower_dict_keys(dict):
        new_dict ={}
        for key, value in dict.items():
            new_dict[key.lower()] = value

        return new_dict








