from common import Scope, Industry, Constants, Action
from tools import Tools
import os
from lxml import etree


class D3One:

    template_directory = 'template/'
    generate_directory = 'output/'

    entities = ['CalendarBlock', 'Provider', 'Customer','Demographics', 'Appointment', 'ApptCode', 'Transaction',
                'PatientAlert', 'Recall', 'Eyewear', 'Diagnosis', 'Account', 'Custom', 'Tax', 'Membership',
                'Vehicle', 'Animal', 'Recommendation']

    def generate_d3one_file(self, scope, action, account):
        """

        :param scope:
        :param action:
        :param Account account:
        :return:
        """
        file_name = self.get_file_name(account.industry, account.business_id, scope)
        customer_data = self.get_customer_data(account)
        customer_data.update({'scope': scope.lower()})

        content = self.generate_from_template(account.industry, action, scope, customer_data)
        output_path = self.write_to_file(content, file_name)
        return output_path


    def get_file_name(self, industry, business_id, scope):
        if industry == Industry.DENTAL:
            sign = 'D'
        elif industry == Industry.AUTO:
            sign = 'A'
        else:
            sign = 'O'

        file_name = '{business_id}.ng38{sign}1_{scope}.{datetime}.xml' \
            .format(business_id=business_id,
                    sign=sign,
                    scope=scope,
                    datetime=Tools.current_date_plus_X_days(-1, Constants.FILE_DATE_TIME))

        return file_name

    def generate_from_template(self, industry, action, scope, args):
        if scope == Scope.TRUEDELTA and action == Action.DELETE:
            template_file = '{industry}_{action}_{scope}.xml'.format(industry=industry, action=action, scope=scope.lower())
        else:
            template_file = '{industry}_{action}.xml'.format(industry=industry, action=action)
        template_object = Tools.fetch_template(D3One.template_directory, template_file)
        parsed = Tools.render_template(template_object, args)
        return parsed

    def get_customer_data(self, account):
        customer_data = {'license_key': account.license_key,
                         'system': account.system_name,
                         'extract_datetime': '{date}-08:00'.format(date=Tools.current_date_plus_X_days(-1, Constants.COMMON_DATE_FORMAT_T)),
                         'calendar_block_date': '{date}-07:00'.format(date=Tools.current_date_plus_X_days(5, Constants.COMMON_DATE_FORMAT_T)),
                         'appt_date': Tools.current_date_plus_X_days(10, Constants.COMMON_DATE_FORMAT_T),
                         'trans_date': '{date}-07:00'.format(date=Tools.current_date_plus_X_days(-10, Constants.COMMON_DATE_FORMAT_T))
                         }
        return customer_data

    def write_to_file(self, content, file_name, compress=True):
        """ Write to xml/gz file

        :param bool compress:
        :return:
        """
        generate_root_path = Tools.build_relative_directory_path(D3One.generate_directory)
        if not os.path.exists(generate_root_path):
            os.mkdir(generate_root_path)

        output_path = Tools.build_relative_directory_path(D3One.generate_directory + file_name)
        print('Generate data file to: ' + output_path)

        # Write file content
        with open(output_path, 'w') as f:
            f.write(content)

        self.xml_file = output_path

        if compress == True:
            output_path = Tools.compress_to_zip_file_(output_path)

        return output_path

    def parse_xml(self):
        """ transfer entiry to dict"""
        parser = etree.XMLParser(remove_blank_text=True)
        root = etree.parse(self.xml_file, parser=parser)
        document = {}

        for element in root.iter(D3One.entities):
            if element.tag in document:
                document[element.tag].append(element.attrib)
            else:
                document[element.tag] = [element.attrib]
        return document


    def remove_output_files(self):
        Tools.remove_folder(D3One.generate_directory)
