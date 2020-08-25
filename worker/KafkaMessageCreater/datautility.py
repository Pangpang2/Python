import django
from django.template import Template, Context
import os
import datetime


try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class DataUtility:
    __template_root = './resources/templates/'
    __generate_root = './generate'
    __document = None

    def __init__(self):
        pass

    @staticmethod
    def from_basic_template(template_path, args):
        source = open(DataUtility.__template_root + template_path)
        try:
            # Read template content
            content = source.read()

            # Render content with arg parse
            django.setup()
            t = Template(content)
            parsed = t.render(Context(args))

            # Write parsed content to element tree
            DataUtility.__document = ET.fromstring(parsed)
        except Exception as e:
            print(repr(e))
        finally:
            source.close()

    @staticmethod
    def add_entity_from_template(template_path, args, parent_xpath):
        source = open(DataUtility.__template_root + template_path)
        try:
            # Read template content
            content = source.read()

            # Render content with arg parse
            django.setup()
            t = Template(content)
            parsed = t.render(Context(args))

            # Write parsed content to element tree
            DataUtility.__add_entity_from_content(parsed, parent_xpath)
        except Exception as e:
            print(repr(e))
        finally:
            source.close()

    @staticmethod
    def write_to_file():
        # Prepare file objects
        DataUtility.__prepare_generate_root()
        us_time_now = datetime.datetime.now()
        output_path = os.path.join(DataUtility.__generate_root,
                                   us_time_now.strftime('%Y-%m-%d-%H-%M-%S') + '.xml')
        if os.path.exists(output_path):
            os.remove(output_path)
        print('Generate data file to: ' + output_path)

        # Write file content
        output = open(output_path, 'a')
        try:
            output.write(ET.tostring(DataUtility.__document, encoding='unicode'))
        finally:
            output.close()

        return output_path

    @staticmethod
    def __prepare_generate_root():
        if not os.path.exists(DataUtility.__generate_root):
            os.makedirs(DataUtility.__generate_root)

    @staticmethod
    def __add_entity_from_content(content, parent_xpath):
        # Write parsed content to element tree
        entity_element = ET.fromstring(content)
        DataUtility.__shrink_attributes(entity_element)
        for child in entity_element:
            DataUtility.__shrink_attributes(child)

        # Attach it to the parent
        parent_element = DataUtility.__document.find(parent_xpath)
        parent_element.append(entity_element)

    @staticmethod
    def __shrink_attributes(node):
        temp = node.attrib.copy()
        for attr in node.attrib:
            if '' == node.attrib[attr] or 'APPT:' == node.attrib[attr]:
                del temp[attr]
        node.attrib = temp
