import ast
import uuid
import time
import datetime
from datetime import timedelta
import re
import gzip
import zipfile
import shutil
import collections
import pytz
from bs4 import BeautifulSoup
from configparser import ConfigParser
import os
import json
import simplejson
from dateutil.relativedelta import *
from dateutil import parser
import importlib
import random
import string
import phonenumbers
from dateutil import tz
from mako.lookup import TemplateLookup
from mako.lookup import Template
import difflib
from difflib import SequenceMatcher
import requests

from collections import OrderedDict
import distutils.util
from pathlib import Path


class Tools:
    """ Class of short reusable general static methods used as helper methods """
    def __init__(self):
        pass

    IS_DEBUG = True

    @staticmethod
    def get_module(module_name):
        """ Will load a python module by name

        :param str module_name:

        :rtype: module
        :return: module object
        """
        try:
            return importlib.import_module(module_name)
        except Exception as e:
            print("Error - can not get module: " + module_name + "\n" + str(e))
            return None

    @staticmethod
    def get_class(module_name, class_name):
        """ Will load a python class by name

        :param str module_name:
        :param str class_name:

        :rtype: object
        :return: class object
        """
        try:
            return getattr(module_name, class_name)
        except Exception as e:
            print("Error - can not get module")
            return None

    @staticmethod
    def has_equivalent_numbers(number_one, number_two):
        """ checks to see if two numbers are equivalent

        :param str or int number_one:
        :param str or int number_two:

        :rtype: bool
        :return: are equivalent numerically
        """
        try:
            return int(number_one) == int(number_two)
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def sleep(sleep_time):
        """ Basic sleep method to sleep for seconds

        :param int sleep_time: sleep time in seconds
        """
        time.sleep(sleep_time)

    @staticmethod
    def get_sub_string(string, number):
        """ Get substring from 0 to char at int

        :param str string:
        :param int number:

        :rtype: str
        :return: cuts string at int
        """
        try:
            return string[:number]
        except Exception as e:
            return None


    @staticmethod
    def string_has_string_part(full_string, string_part):
        if full_string != None:
            return string_part in full_string
        else:
            error_message = "No string part"
            Tools.log(error_message)

    @staticmethod
    def get_uuid():
        """ Creates a long UUID

        :rtype: str
        :return: 8 char uuid
        """
        return Tools.get_sub_string(str(uuid.uuid4()), 8)

    @staticmethod
    def get_uuid_dynamic_size(int_size):
        if isinstance(int_size, int):
            return Tools.get_sub_string(str(uuid.uuid4()), int_size)
        else:
            Tools.raise_exception("Error - Enter an int")

    @staticmethod
    def get_random_number():
        """
        create a random number begin start and stop, and increment is step
        :return:
        """
        return random.randrange(1000, 2000, 25)

    @staticmethod
    def get_random_number_from_range(max, min=0):
        """return a number at the range

        :param int max:
        :param int min:

        :rtype: int
        :return: int
        """
        return random.randrange(min, max, 1)

    @staticmethod
    def get_random_string(num):
        """
        create a random string begin start and stop, and increment is step
        :return:
        """
        return ''.join(random.SystemRandom().choice(string.ascii_letters+ string.digits) for _ in range(num))

    @staticmethod
    def divisor(dividend, divisor):
        """ Get quotient as int and remainder from division.

        :param int dividend:
        :param int divisor:

        :rtype: array
        :return: [quotient, remainder]
        """
        if abs(dividend) > abs(divisor):
            quotient = int(abs(dividend) / abs(divisor))
            remainder = abs(dividend) % abs(divisor)
            return quotient, remainder

    @staticmethod
    def is_negative(number):
        """Finds the number to be negative or not

        :param number:

        :rtype: bool
        :return: is negative
        """
        return number < 0

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
                Tools.log(str(e) + "Date Format Error")

    @staticmethod
    def formatted_phone(phone):
        """
        Will format the phone number provided with format (xxx) xxx-xxxx
        :param phone:
        :return: formatted phone number
        """
        if phone is not None and phone != '':
            return phonenumbers.format_number(phonenumbers.parse(str(phone), 'US'),
                                              phonenumbers.PhoneNumberFormat.NATIONAL)
        else:
            return phone



    @staticmethod
    def dash_formatted_phone(phone_number):
        """Formats the phone 555555555 -> 555-555-5555

        :param str phone_number:
        :return: the formatted phone 555-555-5555
        """
        return '-'.join([phone_number[:3], phone_number[3:6], phone_number[6:]])

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
            Tools.log(e)
            return None

    @staticmethod
    def flatten_string(string):
        """ Will remove spaces and lines from a string (useful for cleaning URLS)

        :param str string:

        :rtype: str
        :return: string with formatting removed
        """
        string = string.replace("\n", "")
        string = string.replace("\r", "")
        string = string.replace("\t", "")
        string = string.replace(" ", "")
        string = "".join(string.splitlines())
        return string.strip()

    @staticmethod
    def check_null_and_single_quotify(string):
        """
        if the string passed in is None, then return NULL, as a valid reference for database
        so this is intended to be used together with database insert/update
        :param string: the string to be checked and quotified
        :return: the quatified string or NULL if the string is None
        """
        if string is None:
            return "NULL"
        return Tools.single_quotify(string)

    @staticmethod
    def single_quotify(string):
        """ Will add quotes to a string
        :param str string:

        :rtype: str
        :return: String with quotes
        """
        if Tools.has_initial_quote(string) is not True:
            return "'" + str(string) + "'"
        else:
            return str(string)

    @staticmethod
    def double_quotify(string):
        """ Will add double quotes to a string, sometimes we need double quote specially
        :param str string:

        :rtype: str
        :return: String with quotes
        """
        if Tools.has_initial_quote(string) is not True:
            return "\"" + str(string) + "\""
        else:
            return str(string)

    @staticmethod
    def remove_quotes(string):
        """Removes quotes from a string

        :param str string:

        :rtype: str
        :return: string without quotes
        """
        raw_string = str(string)
        updated_string = raw_string.replace('"', '')
        return updated_string.replace("'", '')


    @staticmethod
    def convert_to_null(string):
        try:
            updated_string = Tools.remove_quotes(string).lower()
            if updated_string == "none" or updated_string == "null":
                return "null"
        except Exception as e:
            return "null"
        return string

    @staticmethod
    def has_initial_quote(string):
        """ Checks if string starts with single quote

        :param str string:

        :rtype: bool
        :return: has quoted string
        """
        substring = Tools.get_sub_string(string, 1)
        return substring == "'"

    @staticmethod
    def basic_regex_match(full_text, after_pattern, before_pattern):
        """ Will find a string within a string between two patterns

        :param str full_text:
        :param str after_pattern:
        :param str before_pattern:

        :rtype: str
        :return: string between after_pattern and before_pattern
        """
        text = re.search(after_pattern + '(.*)', full_text)
        if text is not None:
            string = text.groups()[0]
            if string is not None:
                new_text = re.search(r'(\S+)\s*'+before_pattern+'(?!/)', string, re.UNICODE)
                return new_text.groups()[0]
            else:
                return None
        else:
            return None

    @staticmethod
    def normalize_spaces(text):
        """ normalize the spaces in the specified text,
        so any continuous spaces will be replaced into one single space,
        for instance, called before trying to do text verification
        in which case spaces aren't a primary concern but will make disturbances

        :param str text: the text to normalize
        :rtype: str
        :return: result text
        """
        spaces_regex = '\s{2,}'
        one_space = " "
        pattern = re.compile(spaces_regex)

        while True:
            m = pattern.search(text)
            if m is None:
                break
            start = m.start()
            end = m.end()
            text = text[0:start] + one_space + text[end:]
        return text

    @staticmethod
    def body_to_content_type(json_var, headers):
        """ Return JSON string if Content-Type is 'application/json'. Else dictionary.

        :param str or dict json_var: python dictionary or string representation of a JSON object.
            If headers['Content-Type'] is not 'application/json', this will get turned into a dictionary.
        :param dict headers: Request headers.
            This method will use the 'Content-Type' header to determine which type this

        :rtype: str or dict
        :return: JSON string if Content-Type is 'application/json'. Else dictionary.
        """
        if headers['Content-Type'] == 'application/json' and isinstance(json_var, dict):
            return json.dumps(json_var)
        if headers['Content-Type'] != 'application/json' and not isinstance(json_var, dict) and json_var is not None:
            return json.loads(json_var)
        else:
            return json_var

    @staticmethod
    def log(string):
        """ Togglable print function

        :param str, int string:
        """
        if Tools.IS_DEBUG:
            try:
                print(str(string))

            except Exception as e:
                print("Error Printing String from library.tools.log")

    @staticmethod
    def fetch_dictionary_part(message, term):
        """

        :param dict, kafka.consumer.fetcher.ConsumerRecord message:
        :param term:
        :return:
        """
        try:
            return message[term]
        except:
            pass

    @staticmethod
    def fetch_ini_section(filename, section):
        """ Get dictionary containing information from section in ini file

        :param str filename: ini file to get data from.
        :param str section: section of ini file to get data from.

        :rtype: dict
        :return: holding data from requested section/file in form"""
        # create a parser
        parser = ConfigParser()
        parser.optionxform = str
        # read config file
        try:
            parser.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), filename))
        except Exception:
            raise Exception('Error parsing file "{0}" '.format(filename))
        # get section, default to account_info
        config_dict = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                config_dict[param[0]] = param[1]
        else:
            raise Exception('Section "{0}" not found in the file "{1}" '.format(section, filename))
        return config_dict

    @staticmethod
    def print_class_attributes(class_object):
        """ prints the attributes for a class

        :param object class_object:
        """
        attributes = vars(class_object)
        print (', '.join("%s: %s" % item for item in attributes.items()))

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
        #sys.path.insert(0, COMBINED_PATH)
        return COMBINED_PATH

    @staticmethod
    def text_similarity_ratio(first_text_content, second_text_content):
        """REturns a ratio of text similarity

        :param str first_text_content:
        :param str second_text_content:

        :rtype: float
        :return: percentage of text similarity
        """
        return SequenceMatcher(None, str(first_text_content), str(second_text_content)).ratio()

    @staticmethod
    def compare_text_template_content(first_text_content, second_text_content, squash=False):
        """Compares two content objects

        :param str, list first_text_content:
        :param str, list second_text_content:

        :rtype: bool
        :return: Confirms objects equality
        """

        first_text_array = Tools.split_list(first_text_content)
        second_text_array = Tools.split_list(second_text_content)
        if squash:
            result_first_lines = list()
            result_second_lines = list()
            for line in first_text_array:
                if len(line.strip()):
                    result_first_lines.append(line.strip())
            for line in second_text_array:
                if len(line.strip()):
                    result_second_lines.append(line.strip())
            return Tools.compare_line_by_line(result_first_lines, result_second_lines)
        else:
            return Tools.compare_line_by_line(first_text_array, second_text_array)

    @staticmethod
    def compare_line_by_line(first_text_array, second_text_array):
        is_equal = True
        line_count = 0
        if len(first_text_array) == len(second_text_array):
            for line in first_text_array:
                first_line = first_text_array[line_count].strip()
                second_line = second_text_array[line_count].strip()
                if Constants.SKIP_LINES in first_line or Constants.SKIP_LINES in second_line:
                    pass
                elif first_line != second_line:
                    is_equal = False
                    Tools.print_comparison_difference(first_text_array, second_text_array, line_count)
                line_count += 1
            return is_equal
        else:
            Tools.log("First List Size(acutal content): " + str(len(first_text_array)))
            Tools.log(str(first_text_array))
            Tools.log("Second List Size(expected content): " + str(len(second_text_array)))
            Tools.log(str(second_text_array))
            raise Exception("Templates are not equal size")

    @staticmethod
    def print_comparison_difference(first_list, second_list, index):
        """

        :param list first_list:
        :param list second_list:
        :param int index:
        """
        Tools.log("Found a difference in 2 lists:")
        Tools.log("first string list:" + str(first_list))
        Tools.log("second string list:" + str(second_list))
        first_line = first_list[index]
        second_line = second_list[index]
        Tools.log("line at {index} in list1:{line}".format(index=index, line=first_line))
        Tools.log("line at {index} in list2:{line}".format(index=index, line=second_line))
        output_list = [li for li in difflib.ndiff(str(first_list), str(second_list)) if li[0] != ' ']

        Tools.log(output_list)

    @staticmethod
    def print_string_difference(first_text_content, second_text_content):
        """Shows the difference in a text string

        :param str, first_text_content:
        :param str, second_text_content:
        """
        for i, s in enumerate(difflib.ndiff(first_text_content, second_text_content)):
            if s[0] == ' ':
                continue
            elif s[0] == '-':
                Tools.log(u'Delete "{}" from position {}'.format(s[-1], i))
                #Tools.log(first_text_content[-10+i:10+i])
            elif s[0] == '+':
                Tools.log(u'Add "{}" to position {}'.format(s[-1], i))

    @staticmethod
    def split_list(list_object):
        """Safe split

        :param str, list list_object:

        :rtype: str, list
        :return: The split list
        """
        try:
            return list_object.splitlines()
        except Exception as e:
            return list_object

    @staticmethod
    def join_list(list_object):
        """Safely joins list

        :param list list_object:

        :rtype: str
        :return: the joined list
        """
        if isinstance(list_object, list):
            return '\n'.join(list_object)
        else:
            return list_object

    @staticmethod
    def groupNumbers(n, sep=','):
        s = str(abs(n))[::-1]
        groups = []
        i = 0
        while i < len(s):
            groups.append(s[i:i + 3])
            i += 3
        retval = sep.join(groups)[::-1]
        if n < 0:
            return '-%s' % retval
        else:
            return retval

    @staticmethod
    def fetch_rest_content(rest_response):
        """Gets content from rest response and scrubs content for errors

        :param rest_response:

        :rtype: str
        :return: content string
        """
        rest_content = rest_response.text
        fixed_text = re.sub(r'[^\x00-\x7F]+', ' ', rest_content)
        return fixed_text

    @staticmethod
    def render_template(template_content, template_tags):
        """ Renders template using a conversion dictionary

        :param Template template_content:
        :param dict, list template_tags:

        :rtype: str
        :return:the template rendered as a string
        """
        try:
            return template_content.render(**template_tags).encode('ascii', 'ignore').replace("\r\n", "\n")
        except Exception as e:
            Tools.log("Could not render template: "+str(e))

    @staticmethod
    def render_template_utf(template_content, template_tags):
        """ Renders template using a conversion dictionary

        :param Template template_content:
        :param dict, list template_tags:

        :rtype: str
        :return:the template rendered as a string
        """
        try:
            return template_content.render(**template_tags).encode('utf-8', 'ignore').replace("\r\n", "\n")
        except Exception as e:
            Tools.log("Could not render template: "+str(e))



    @staticmethod
    def convert_string_to_dictionary(dictionary_string):
        """Converts a dictionary that has become a string back into a dictionary

        :param str dictionary_string:

        :rtype: dict
        :return: converted dictionary
        """
        if dictionary_string is not None and isinstance(dictionary_string, str) or isinstance(dictionary_string, unicode):
            try:
                return ast.literal_eval(dictionary_string)
            except Exception as e:
                Tools.log("Could not convert string to dictionary: "+str(e))
        else:
            return None

    @staticmethod
    def add_brackets_to_string(string):
        """Add brackets for post objects

        :param str string:

        :rtype: str
        :return:
        """
        return '{' + str(string) + '}'

    @staticmethod
    def convert_string_to_bool(value):
        if not isinstance(value, bool):
            value = distutils.util.strtobool(value)
        return value

    @staticmethod
    def object_has_value(object_of_value):
        """ Does the object exist

        :param obj object_of_value:

        :rtype: bool
        :return: True or False
        """
        return object_of_value is not None and len(object_of_value) > 0

    @staticmethod
    def objects_have_value(*arg):
        """ Do the objects exist

        :param object arg:

        :rtype: bool
        :return: True or False
        """
        is_error_free = True
        for item in arg:
            if not Tools.object_has_value(item):
                is_error_free = False
        return is_error_free

    @staticmethod
    def raise_exception(exception):
        raise Exception(exception)


    @staticmethod
    def generate_email_address(uuid):
        """

        :param uuid:
        :return: unique business email
        """
        email_suffix = BusinessSetupConstants.BUSINESS_EMAIL_SUFFIX
        email = BusinessSetupConstants.BUSINESS_EMAIL_PREFIX + uuid + email_suffix
        return email

    @staticmethod
    def convert_string_to_json(string):
        """Converts a json type string object into a real json string

        :param Str string:

        :rtype: json
        :return: the json formatted object
        """
        if string is not None and isinstance(string, str):
            try:
                return simplejson.loads(string, object_pairs_hook=OrderedDict)
            except Exception as e:
                pass
                Tools.log("Could not convert string to json object")
        else:
            return None

    @staticmethod
    def convert_response_to_json_data(response):
        try:
            response_text = response.text
            json_data = json.loads(response_text)
            return json_data
        except Exception as e:
            Tools.log("Could not convert response to json object")
            return None

    @staticmethod
    def convert_json_to_string(json_object):
        """Converts a string into a json object

        :param json json_object:

        :rtype: str
        :return: the converted string
        """
        try:
            return json.dumps(json_object, sort_keys=True)
        except Exception as e:
            Tools.log("Could not convert json object to string")

    @staticmethod
    def order_object(object):
        """Orders dictionaries and lists

        :param obj object:

        :rtype: obj
        :return: The object ordered
        """
        if isinstance(object, dict):
            return sorted((key, Tools.order_object(value)) for key, value in object.items())
        if isinstance(object, list):
            return sorted(Tools.order_object(list_object) for list_object in object)
        else:
            return object

    @staticmethod
    def well_ordered_json_string(json_object):
        """ Turns raw json into a well ordered string

        :param json, str json_object:

        :rtype: str
        :return:
        """
        json_content = Tools.convert_string_to_json(json_object)
        ordered_json_content = Tools.order_object(json_content)
        return Tools.convert_json_to_string(ordered_json_content)

    @staticmethod
    def check_matching_json_data(actual_response, expected_response, skip_text="ERASED_CONTENT"):
        """ This parameter requires json objects turned into a a string as a parameter.
        It checks for matching dictionary values
        Json template text can be updated to skip value checks for dynamic data

        :param str actual_response:
        :param str expected_response:

        """
        Tools.log("Verify advanced JSON content match")

        # ordered string
        actual_response_string = Tools.well_ordered_json_string(actual_response)
        expected_response_string = Tools.well_ordered_json_string(expected_response)

        # list
        actual_response_list = Tools.convert_string_to_json(actual_response_string)
        expected_response_list = Tools.convert_string_to_json(expected_response_string)

        # iterates through json object which should at root be a list and not a dictionary
        for count, actual_collection_object in enumerate(actual_response_list, start=0):

            # dictionary conversion
            actual_dictionary_object = Tools.cast_dictionary_object(actual_collection_object)
            expected_collection_object = expected_response_list[count]
            expected_dictionary_object = Tools.cast_dictionary_object(expected_collection_object)

            # key list
            actual_key_list = None
            if isinstance(actual_dictionary_object, dict):
                actual_key_list = actual_dictionary_object.keys()

            for actual_key in actual_key_list:
                actual_key_value = actual_dictionary_object[actual_key]
                expected_key_value = expected_dictionary_object[actual_key]
                Tools.log(actual_key_value)
                Tools.log(expected_key_value)
                if expected_key_value == skip_text:
                    # skips check
                    pass
                else:
                    content_error = " - " + str(actual_key)+": \nexpected:\n" + str(expected_key_value) + "\nactual:\n" + str(actual_key_value)
                    assert actual_key_value == expected_key_value, content_error

    @staticmethod
    def cast_dictionary_object(collection_object):
        try:
            return dict(collection_object)
        except Exception as e:
            if len(collection_object) == 2:
                return {collection_object[0]: collection_object[1]}
            else:
                Tools.log("Error converting object to a dictionary")


    @staticmethod
    def flatten_nested_dictionary(object_dictionary):
        """WIll un-nest dictionaries. Used specifically for nested json objects.
        WILL CAUSE PROBLEMS if there are duplicate keys

        :param collections.OrderedDict dictionary object_dictionary:

        :rtype: collections.OrderedDict dictionary
        :return:
        """
        if object_dictionary is not None:
            object = Tools.nested_dictionary_iteration(object_dictionary)
            flat_dictionary = {}
            for i in object:
                flat_dictionary[i[0]] = i[1]
            return flat_dictionary
        else:
            return None

    @staticmethod
    def nested_dictionary_iteration(nested_dictionary):
        """Flattens an nestered ordered dictionary

        :param nested_dictionary:
        :return:
        """
        if nested_dictionary is not None and isinstance(nested_dictionary, collections.OrderedDict):
            for key, value in nested_dictionary.iteritems():
                if isinstance(value, collections.Mapping):
                    for inner_key, inner_value in Tools.nested_dictionary_iteration(value):
                        yield inner_key, inner_value
                else:
                    yield key, value


    @staticmethod
    def fetch_dictionary_keys(dictionary):
        if dictionary is not None and isinstance(dictionary, collections.OrderedDict):
            return dictionary.keys()
        else:
            Tools.log("Error - is not a dictionary: " + str(type(dictionary)))
            return None


    @staticmethod
    def is_key_name_in_dictionary(key_name, dictionary):
        """ Looks to see if a dictionary contains a key value pair

        :param str key_name:
        :param collections.OrderedDict dictionary:

        :rtype: bool
        :return: Yes or no the key name is in the dictionary
        """
        if key_name is not None and dictionary is not None and isinstance(dictionary, dict):
            if key_name in dictionary:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def fetch_value_from_string_dictionary(key_name, dictionary):
        """ Fetches a str value from a dictionary

        :param str key_name:
        :param collections.OrderedDict dictionary:

        :rtype: str
        :return: The value for the dictionary
        """
        if (Tools.is_key_name_in_dictionary(key_name, dictionary)):
            return dictionary[key_name]
        else:
            return None

    @staticmethod
    def fetch_dictionary_value(key_name, dictionary):
        if dictionary == None:
            error = "Dictionary is empty"
            Tools.raise_exception(error)
        try:
            value = dictionary[key_name]
            return value
        except:
            error = "Key not found in dictionary"
            Tools.raise_exception(error)
            Tools.log(str(dictionary))

    @staticmethod
    def is_string_value_in_dictionary(key_name, key_value, dictionary):
        """Looks for a matching key value in a dictionary

        :param str key_name:
        :param str key_value:
        :param collections.OrderedDict dictionary:

        :rtype: bool
        :return: Yes or no the value matches
        """
        if Tools.fetch_value_from_string_dictionary(key_name, dictionary):
            if dictionary[key_name] == key_value:
                return True
            else:
                return False
        else:
            return False


    @staticmethod
    def print_dictionary(dictionary):
        for k, v in dictionary.items():
            print(k, v)

    ##########
    ###
    # Dates nad times
    ###
    ##########

    @staticmethod
    def current_date(time_zone=None):
        """ Will return the current date

        :param tzlocal time_zone:

        :rtype: datetime.datetime
        :return: current date
        """
        if time_zone is None:
            return datetime.datetime.now()
        else:
            return datetime.datetime.now(time_zone)

    @staticmethod
    def current_date_plus_X_days(day):
        """ Will return the current date + days

        :rtype: datetime.datetime
        :return: current date
        """
        return datetime.datetime.now() + timedelta(days=day)

    @staticmethod
    def current_time():
        """ Will return the current time in seconds

        :rtype: time.time
        :return: current time
        """
        return time.time()

    @staticmethod
    def convert_str_to_datetime(date_string, date_format):
        """ Return a datetime corresponding to date_string, parsed according to date_format.

        :param str date_string: String representing date to be returned.
        :param str date_format: Format of date_string.

        :rtype: datetime.datetime
        :return: datetime object representing date_string.
        """
        return datetime.datetime.strptime(date_string, date_format)

    @staticmethod
    def fetch_date_by_month_offset(month_offset, date_format):
        """ Will create a date with a month offset. Will rollback the year if necessary

        :param int month_offset:
        :param str date_format:

        :rtype: str
        :return: date w/offset
        """
        current_date = Tools.current_date()
        if month_offset is not None and format is not None and isinstance(month_offset, (int)):
            updated_date = current_date + relativedelta(months=month_offset)
            return updated_date.strftime(date_format)
        else:
            return current_date

    @staticmethod
    def is_date_within_minute_range(date_time, minute_offset, date_center=None):
        """checks to see if a date is within a minute range. default is current time, but and date can be added

        :param datetime.datetime date_time:
        :param int minute_offset:
        :param datetime.datetime date_center:
        :return: Boolean
        """
        if date_center is None:
            date_center = Tools.current_date(tz.tzlocal())
        past_date = date_time - timedelta(minutes=minute_offset)
        future_date = date_time + timedelta(minutes=minute_offset)
        if future_date > date_center and past_date < date_center:
            return True
        else:
            return False

    @staticmethod
    def fetch_date_by_minute_offset(minute_offset, date_format, start_date = None):
        """ Will create a date with a minute offset

        :param int minute_offset:
        :param str date_format:

        :rtype: str
        :return: date w/offset
        """
        if start_date is None:
            current_date = Tools.current_date()
        else:
            Tools.log(type(start_date))
            current_date = start_date
        if minute_offset is not None and date_format is not None:
            date = current_date + timedelta(minutes=minute_offset)
            return date.strftime(date_format)
        else:
            return current_date

    @staticmethod
    def fetch_date_by_days_offset(days_offset, date_format):
        """ Will create a date with a days offset

        :param int days_offset:
        :param str date_format:
        :rtype: str
        :return: date w/offset
        """
        current_date = Tools.current_date()
        if days_offset is not None and isinstance(days_offset, (int)):
            date = current_date + timedelta(days=days_offset)
            return date.strftime(date_format)
        else:
            return current_date

    @staticmethod
    def update_time_zone(date_time, new_time_zone, original_time_zone):
        """changes the time according to a time zone change

        :param datetime.datetime date_time:
        :param TimeZones new_time_zone:
        :param TimeZones original_time_zone:

        :rtype: datetime.datetime
        :return: time zone updated date
        """
        scrub_date = Tools.scrub_date(date_time)
        original_time_zone_code = pytz.timezone(original_time_zone)
        aware_date = original_time_zone_code.localize(scrub_date)
        new_time_zone_code = pytz.timezone(new_time_zone)
        return aware_date.astimezone(new_time_zone_code)

    @staticmethod
    def scrub_common_date_by_removal(date_string):
        """ removes all date time info from string after year-day-month

        :param str date_string:

        :rtype: datetime.datetime
        :return : newly formatted date with extra info removed
        """
        index = date_string.rfind("T")
        new_date_string = date_string[:index]
        formatted_date = Tools.formatted_date(new_date_string, Constants.DAY_FORMAT)
        return formatted_date

    @staticmethod
    def scrub_date(date_time):
        """Removes formatting from a date

        :param datetime.datetime date_time:

        :rtype: datetime.datetime
        :return: newly formatted date
        """
        formatted_date = Tools.formatted_date(str(date_time), Constants.COMMON_DATE_FORMAT)
        return datetime.datetime.strptime(formatted_date, Constants.COMMON_DATE_FORMAT)

    @staticmethod
    def update_time_zone_to_local(date_time):
        """will update the time zone to the current time zone

        :param date_time:

        :rtype: Date
        :return: The updated date
        """
        if isinstance(date_time, str):
            new_date = Tools.date_from_string(date_time)
        else:
            new_date = date_time
        try:
            return new_date.astimezone(tz.tzlocal())
        except Exception as e:
            print("Error updating timezone: " + str(e))
            return None

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
    def compress_to_gz_file_(file_name):
        """
        compress xml file to gz file
        :param str file_name:
        :rtype: str
        :return: gz file full path
        """
        gz_file_name = '%s.gz' % file_name
        try:
            with open(file_name, 'rb') as f_in, gzip.open(gz_file_name, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                return gz_file_name
        except Exception as e:
            raise Exception("Error when compress to gz file: " + str(e))

    @staticmethod
    def extract_zip_file(zip_file, target_folder=None, password=None):
        try:
            z = zipfile.ZipFile(zip_file)
            z.extractall(path=target_folder, pwd=password)
        except Exception as e:
            raise Exception("Error when extract zip file: " + str(e))

    @staticmethod
    def remove_redundant_files(path, exception_suffix):
        """
        remove files under path except files with specific suffix
        :param str path: folder path
        :param str exception_suffix:
        :return:
        """
        try:
            for file in os.listdir(path):
                if not exception_suffix in file:
                    os.remove(path + file)
        except Exception as e:
            print("Error when remove folder %s: %s "%(path, str(e)))
            return None


    @staticmethod
    def fetch_project_root():
        """
        Returns project root folder
        """
        return str(Path(__file__).parent.parent)

    @staticmethod
    def join_directory(base_directory, location):
        """

        :param base_directory:
        :param location:

        :rtype:
        :return:
        """

        return os.path.join(os.path.normpath(base_directory), location)

    @staticmethod
    def json_data_write_tool(directory, file_name, data):
        """

        :param directory:
        :param file_name:
        :param data:

        :return:
        """
        file_object = Tools.join_directory(directory, file_name)
        Tools.log(directory)
        with open(file_object, 'w') as outfile:
            json.dump(data, outfile)

    @staticmethod
    def formatted_date_string(date):
        """ Will format a date object
        and return it as string

        :param datetime.datetime, str date:

        :rtype: str
        :return: formatted date
        """
        if isinstance(date, str):
            date = Tools.date_from_string(date)
        if date is not None:
            return date.strftime(Constants.COMMON_DATE_FORMAT)
        else:
            return date

    @staticmethod
    def formatted_day_string(date):
        """ Will format a date object
        and return it as string

        :param datetime.datetime, str date:

        :rtype: str
        :return: formatted date
        """
        if isinstance(date, str):
            date = Tools.date_from_string(date)
        if date is not None:
            return date.strftime(Constants.DAY_FORMAT)
        else:
            return date

    @staticmethod
    def formatted_template_datetime_string(date):
        """ Will convert a date to a string in format "Y-%m-%d %H:%M:%S.%f+0000" (miliseconds keeps 3 digits)
        :param date:
        :return:
        """
        if isinstance(date, str):
            date = Tools.date_from_string(date)
        if date is not None:
            return date.strftime(Constants.TEMPLATE_MILLISECONDS_DATE_FORMAT)[:-3] + "+0000"
        else:
            return date

    @staticmethod
    def compare_dictionary_content(first_dict, second_dict, exact=True):
        """ Compare dictionaries and return True or False
        If exact is False, only need to verify fist_dict items

        :param first_dict:
        :param second_dict:
        :param exact: whether to compare dictionary exactly. default is False.
        :return:
        :rtype: bool
        """

        if exact == True and list.sort(first_dict.keys()) != list.sort(second_dict.keys()):
            Tools.log('First dictionary keys : {0}'.format(list.sort(first_dict.keys())))
            Tools.log('Second dictionary keys: {0}'.format(list.sort(second_dict.keys())))
            return False

        for key, value in first_dict.items():
            # Ignore type info when comparing datetime variable with others
            if exact == False and (isinstance(value, (datetime.date, datetime.datetime)) or \
                    isinstance(second_dict[key], (datetime.date, datetime.datetime))):
                first_value = Tools.formatted_date(value, Constants.TEMPLATE_TIMEZONE_DATE_FORMAT)
                second_value = Tools.formatted_date(second_dict[key], Constants.TEMPLATE_TIMEZONE_DATE_FORMAT)
            else:
                first_value = str(value)
                second_value = str(second_dict[key])

            if first_value != second_value:
                Tools.log('First dictionary :{key}:{value}'.format(key=key, value=first_value))
                Tools.log('Second dictionary:{key}:{value}'.format(key=key, value=second_value))
                return False

        return True


    @staticmethod
    def get_URL_from_String(test_string):
        """

        :param test_string: The string you need to get URL from
        :return: URL in string
        """
        pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
        url = re.findall(pattern, test_string)
        return url

    @staticmethod
    def convert_json_response_to_dict(response_json):
        """ Converts json recieved as a response to a dictionary
        If exact is False, only need to verify fist_dict items
        :param response_json:
        :return:
        :rtype: dict
        """
        string1 = str(response_json.text)[1:-1]
        dict = json.loads(string1)
        return dict

    @staticmethod
    def send_request_get(url, headers=None):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response
        else:
            return None

    @staticmethod
    def fetch_email_div_content(raw_email_body, basic_parse=True):
        if basic_parse:
            Tools.log("Html full text email parse")
            try:
                soup = BeautifulSoup(raw_email_body, 'html.parser')
                message_text = soup.get_text()
                formatted_message_text = message_text.encode("utf-8", errors='replace_with_space').strip()
                return str(formatted_message_text)
            except Exception as exception:
                Tools.log("Could not format email message")
                Tools.log(exception)
        else:
            Tools.log("Customer email body parse")
            try:
                soup_object = BeautifulSoup(raw_email_body, 'html.parser')
                formatted_message_text = soup_object.find_all('div', {'class': 'customEmailBody'})[0].text.encode(
                    'ascii', 'ignore').strip()
                return formatted_message_text
            except Exception as exception:
                Tools.log("Could not format custom email message")
                Tools.log(exception)



