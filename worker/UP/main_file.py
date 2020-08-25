# from __future__ import absolute_import
from worker.UP.account import AccountHelper
from worker.UP.common import *
from worker.UP.integration import Integration
from worker.UP.uploadprocessor import UploadProcessor
from worker.UP.account import Account
import time

#  uplod with specify business

class Helper:
    @staticmethod
    def printout(line):
        print(('\033[31;0m{line}\033[0m'.format(line=line)))

    @staticmethod
    def sleep(sceond=10):
        time.sleep(sceond)

if __name__ == '__main__':

    env = Environment.STG
    #env = Environment.LOCAL
    print(('Test environment %s'%env))
    print('')

    account = Account()
    account.business_id = '138043361'
    account.license_key = 'BF1AF703-B070-0EF0-DD5B-535D42638F22'

    # clear upload history
    UploadProcessor.clear_table_for_business(account.business_id, 'UploadHistory')

    Integration.upload_data_with_file(account, 'template', 'test.xml', env, clear=False)


    # print UploadProcessor.get_customer_options_from_db(dental_account.business_id)
    # print UploadProcessor.get_business_system_from_db(dental_account.business_id)
    # print UploadProcessor.get_business_dflink_property_from_db(dental_account.business_id)
    # print UploadProcessor.get_business_interval_from_db(dental_account.business_id)
    # print UploadProcessor.get_business_option_from_db(dental_account.business_id)
    # print UploadProcessor.get_business_option_from_db(dental_account.business_id)





