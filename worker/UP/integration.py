from worker.UP.account import AccountHelper
from worker.UP.d3one import D3One
from worker.UP.common import *
from worker.UP.dflink import DFLink
from worker.UP.endpoint import Endpoint
from worker.UP.tools import Tools
from worker.UP.uploadprocessor import UploadProcessor
from lxml import etree
import os


class Integration:

    @staticmethod
    def upload_data(account, scope, action, env, clear=True, check_list=D3One.entities):
        print('============================================================')
        print(account.industry + ' ' + scope + ' ' + action)
        # clear data for business
        UploadProcessor.env = env

        UploadProcessor.clear_upload_history_for_business(account.business_id)

        if clear:
            print('Clear uploaded file and db')
            UploadProcessor.clear_invalid_file()
            UploadProcessor.clear_uploaded_data_for_business(account.business_id)

        # generate file
        d3 = D3One()
        file_path = d3.generate_d3one_file(scope, action, account)

        # upload
        if env == Environment.LOCAL:
            url = Endpoint.LOCAL
        else:
            url = Endpoint.STG
        DFLink.upload(url, account.license_key, file_path)

        # check .invalid file
        UploadProcessor.check_invalid_file()

        # check upload history and data
        UploadProcessor.check_upload_history(account.business_id)
        is_delete = True if action == Action.DELETE else False
        UploadProcessor.check_upload_data(d3, account, check_list, is_delete)

        # clear out put
        #d3.remove_output_files()

    @staticmethod
    def upload_data_with_file(account, directory, file_name, env, clear=True):
        """
        Clear data, Upload existing file, Check upload status
        :param account:
        :param directory:
        :param file_name:  xml file name
        :param env:
        :param clear:
        :return:
        """

        UploadProcessor.env = env
        if clear:
            print('Clear uploaded file and db')
            UploadProcessor.clear_invalid_file()
            UploadProcessor.clear_uploaded_data_for_business(account.business_id)

        # upload
        if env == Environment.LOCAL:
            url = Endpoint.LOCAL
        else:
            url = Endpoint.STG

        # update license key
        full_path = Tools.build_relative_directory_path(directory) + "\\" + file_name
        root = etree.parse(full_path)
        if root.getroot().get('licenseKey'):
            root.getroot().set('licenseKey', account.license_key)
        license_node = root.find('Business//Extract//DFLinkSettings//BusinessList//Business//LicenseKey')
        if license_node is not None:
            license_node.text=account.license_key
        root.write(full_path)

        gz_file = Tools.compress_to_zip_file_(full_path)
        print('Upload file:' + gz_file)
        DFLink.upload(url, account.license_key, gz_file)

        # check .invalid file
        UploadProcessor.check_invalid_file()

        # check upload history and data
        UploadProcessor.check_upload_history(account.business_id)

        UploadProcessor.clear_invalid_file()
