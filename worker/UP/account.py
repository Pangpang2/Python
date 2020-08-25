from __future__ import absolute_import
from common import Industry, Environment

class Account:
    business_id = None
    license_key = None
    system_name = None
    industry = None


class AccountHelper:
    @staticmethod
    def get_default_dental_account(env=Environment.STG):
        account = Account()
        if env == Environment.STG:
            account.business_id = '138000213'
            account.license_key = '91D2AF8A-56C7-FE29-301B-C2E44B4C656D'
            account.system_name = 'Dentrix'
            account.industry = Industry.DENTAL
            account.email = 'up_ng38_dental_38@demandforce.com'
            account.password = 'onDemand1!'
            # account.business_id = '138042221'
            # account.license_key = '3C72D6CC-4570-A68B-DB11-8E0DB1DDB71D'
            # account.system_name = 'Dentrix'
            # account.industry = Industry.DENTAL
            # account.email = 'J_test_27225333_1@d3one.com'
            # account.password = 'ondemand1!QAM'
        else:
            account.business_id = '130000001'
            account.license_key = '95F59D26-DBEE-9B78-D346-928806A2381E'
            account.system_name = 'Dentrix'
            account.industry = Industry.DENTAL

        return account

    @staticmethod
    def get_default_auto_account(env):
        account = Account()
        account.business_id = '138000218'
        account.license_key = 'EF83EAAB-2D7D-3A0F-7436-DC6BF76DDED1'
        account.system_name = 'R.O. Writer'
        account.industry = Industry.AUTO
        account.email = 'up_ng38_autoTest_38@demandforce.com'
        account.password = 'onDemand1!'
        return account

    @staticmethod
    def get_default_other_account(env):
        account = Account()
        account.business_id = '138000219'
        account.license_key = '2EA526A1-0C9C-0A02-EC81-90FACBA5C177'
        account.system_name = 'Complete Clinic Software'
        account.industry = Industry.OTHER
        account.email = 'up_ng38_other_38@demandforce.com'
        account.password = 'onDemand1!'#?
        return account

    @staticmethod
    def get_vetmatrix_account(env):
        # industry = 11
        account = Account()
        account.business_id = '138032114'
        account.license_key = '6F0DAC3A-F3A7-99AB-9119-0A27605B60F9'
        account.system_name = 'Complete Clinic Software'
        account.industry = Industry.OTHER
        account.email = 'J_vet_auto_3896576d_1@d3one.com'
        account.password = 'ondemand1!QAM'  #'*Z)C*8Gb'
        return account

    @staticmethod
    def get_inactive_account(env):
        account = Account()
        account.business_id = '138031604'
        account.license_key = 'C1EEF664-236E-158F-8E7E-ED3D7803669E'
        account.system_name = 'Complete Clinic Software'
        account.industry = Industry.OTHER
        account.email = 'J_testAuto_89d3754c_1@d3one.com'
        account.password = 'onDemand1!'  # '5T6d(ny*'
        return account




