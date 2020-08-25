from account import AccountHelper
from common import *
from integration import Integration
from uploadprocessor import UploadProcessor
import jenkins_caller
import time

class Helper:
    @staticmethod
    def printout(line):
        print('\033[31;0m{line}\033[0m'.format(line=line))

    @staticmethod
    def sleep(sceond=10):
        time.sleep(sceond)

if __name__ == '__main__':

    env = Environment.STG
    #env = Environment.LOCAL
    print('Test environment %s'%env)
    print('')

    dental_account = AccountHelper.get_default_dental_account(env)
    auto_account = AccountHelper.get_default_auto_account(env)
    other_account = AccountHelper.get_default_other_account(env)
    vetmatrix_account = AccountHelper.get_vetmatrix_account(env)

    # dental full
    # scope = Scope.FULL
    # check_list = ['CalendarBlock', 'Provider', 'Customer','Demographics', 'Appointment', 'ApptCode',
    #             'PatientAlert', 'Recall', 'Eyewear', 'Diagnosis', 'Account', 'Custom', 'Tax', 'Membership']
    # check_list = ['Appointment', 'Customer']
    # Integration.upload_data(dental_account, scope, Action.INSERT, env, clear=False, check_list=check_list)
    # Integration.upload_data(dental_account, scope, Action.UPDATE, env, clear=False, check_list=check_list)
    # Integration.upload_data(dental_account, scope, Action.DELETE, env, clear=False, check_list=check_list)

    # auto full
    # scope = Scope.TRUEDELTA
    # check_list = [Entity.VEHICLE, Entity.APPOINTMENT, Entity.APPTCODE, Entity.TRANSACTION, Entity.RECOMMENDATION]
    # Integration.upload_data(auto_account, scope, Action.INSERT, env, clear=False, check_list=check_list)
    # Integration.upload_data(auto_account, scope, Action.UPDATE, env, clear=False, check_list=check_list)
    #Integration.upload_data(auto_account, scope, Action.DELETE, env, clear=False, check_list=check_list)

    #other full
    # scope = Scope.TRUEDELTA
    # check_list = [Entity.ANIMAL, Entity.APPOINTMENT, Entity.APPTCODE, Entity.TRANSACTION, Entity.RECOMMENDATION]
    # #Integration.upload_data(other_account, scope, Action.INSERT, env, clear=True, check_list=check_list)
    # Integration.upload_data(other_account, scope, Action.UPDATE, env, clear=False, check_list=check_list)
    # Integration.upload_data(other_account, scope, Action.DELETE, env, clear=False, check_list=check_list)

    # dental delta regression
    #Integration.upload_data(auto_account, Scope.TRUEDELTA, Action.UPDATE, env)


    # # # reminder 2.0 scenario 1 https://testrail.internetbrands.com/testrail/index.php?/tests/view/116236638
    # UploadProcessor.clear_upload_history_for_business(vetmatrix_account.business_id)
    # UploadProcessor.clear_appointment_for_business(vetmatrix_account.business_id)
    # UploadProcessor.clear_customer_for_business(vetmatrix_account.business_id)

    # upload with appointment without apptcode
    # Integration.upload_data_with_file(vetmatrix_account, 'template', '138032114_without_procedure.xml', env,
    #                                   clear=False)
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('planId without procedure: ' + appt_list[0]['planId'])
    #
    # jenkins_caller.run_assign_planid_reminder_2()
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('expected plan id: d7af319c-754a-4d21-afc9-b3388e3c22b6')
    # Helper.printout('actual plan id:   ' + appt_list[0]['planId'])
    # assert appt_list[0]['planId'] == 'd7af319c-754a-4d21-afc9-b3388e3c22b6', 'planId should be default plan id.'
    #
    # # upload with appt with apptcode
    # Integration.upload_data_with_file(vetmatrix_account, 'template', '138032114_one_procedure.xml', env, clear=False)
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('planId after add apptcode: ' + appt_list[0]['planId'])
    #
    # jenkins_caller.run_assign_planid_reminder_2()
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('expected plan id: 64cac400-e9a0-11e9-901c-7ddf5bf4632f')
    # Helper.printout('actual plan id:   ' + appt_list[0]['planId'])

    # scenario 2 https://testrail.internetbrands.com/testrail/index.php?/tests/view/116236639
    # UploadProcessor.clear_upload_history_for_business(vetmatrix_account.business_id)
    # UploadProcessor.clear_appointment_for_business(vetmatrix_account.business_id)
    # # upload with appt with apptcode
    # Integration.upload_data_with_file(vetmatrix_account, 'template', '138032114_one_procedure.xml', env, clear=False)
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('planId after add apptcode: ' + appt_list[0]['planId'])
    #
    # jenkins_caller.run_assign_planid_reminder_2()
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('expected plan id: 64cac400-e9a0-11e9-901c-7ddf5bf4632f')
    # Helper.printout('actual plan id:   ' + appt_list[0]['planId'])
    #
    # # upload another procedure
    # Integration.upload_data_with_file(vetmatrix_account, 'template', '138032114_another_procedure.xml', env, clear=False)
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('planId after update apptcode: ' + appt_list[0]['planId'])
    #
    # jenkins_caller.run_assign_planid_reminder_2()
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('expected plan id: 6846eb10-e9a3-11e9-b217-eb9ad3d38f16')
    # Helper.printout('actual plan id:   ' + appt_list[0]['planId'])

    # UploadProcessor.clear_table_for_business(auto_account.business_id, Entity.APPOINTMENT)
    # UploadProcessor.clear_table_for_business(auto_account.business_id, Entity.APPTCODE)
    # row = UploadProcessor.get_animal_from_db(other_account.business_id)
    # print row[0]
    #
    # Integration.upload_data_with_file(dental_account, 'output',
    #                                   '138000213.ng38D1_Delta.2019-10-07-23-02-44.xml',
    #                                   env, clear=False)
    # row = UploadProcessor.get_animal_from_db(auto_account.business_id)
    # print row[0]

    # #scenario 3  https://testrail.internetbrands.com/testrail/index.php?/tests/view/116236640
    # UploadProcessor.clear_upload_history_for_business(vetmatrix_account.business_id)
    # UploadProcessor.clear_appointment_for_business(vetmatrix_account.business_id)
    # # upload with appointment without apptcode
    # Integration.upload_data_with_file(vetmatrix_account, 'template', '138032114_without_procedure.xml', env,
    #                                   clear=False)
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('planId without procedure: ' + appt_list[0]['planId'])
    #
    # jenkins_caller.run_assign_planid_reminder_2()
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('expected plan id: d7af319c-754a-4d21-afc9-b3388e3c22b6')
    # Helper.printout('actual plan id:   ' + appt_list[0]['planId'])
    # # assert appt_list[0]['planId'] == 'd7af319c-754a-4d21-afc9-b3388e3c22b6', 'planId should be default plan id.'
    #
    # # upload with appt with apptcode
    # Integration.upload_data_with_file(vetmatrix_account, 'template', '138032114_one_procedure.xml', env, clear=False)
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('planId after add apptcode: ' + appt_list[0]['planId'])
    #
    # jenkins_caller.run_assign_planid_reminder_2()
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('expected plan id: 64cac400-e9a0-11e9-901c-7ddf5bf4632f')
    # Helper.printout('actual plan id:   ' + appt_list[0]['planId'])
    #
    # # upload with appt with new apptcode
    # Integration.upload_data_with_file(vetmatrix_account, 'template', '138032114_new_procedure.xml', env, clear=False)
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('planId after add new apptcode: ' + appt_list[0]['planId'])
    #
    # jenkins_caller.run_assign_planid_reminder_2()
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('expected plan id: d7af319c-754a-4d21-afc9-b3388e3c22b6')
    # Helper.printout('actual plan id:   ' + appt_list[0]['planId'])
    #
    # #-------------------------------------------------------------------

    # scenario 4
    # UploadProcessor.clear_upload_history_for_business(vetmatrix_account.business_id)
    # UploadProcessor.clear_appointment_for_business(vetmatrix_account.business_id)
    # # upload with appt with apptcode
    # Integration.upload_data_with_file(vetmatrix_account, 'template', '138032114_one_procedure.xml', env, clear=False)
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('planId after add apptcode: ' + appt_list[0]['planId'])
    #
    # jenkins_caller.run_assign_planid_reminder_2()
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('expected plan id: 64cac400-e9a0-11e9-901c-7ddf5bf4632f')
    # Helper.printout('actual plan id:   ' + appt_list[0]['planId'])
    #
    # # upload with appointment without apptcode
    # Integration.upload_data_with_file(vetmatrix_account, 'template', '138032114_without_procedure.xml', env,
    #                                   clear=False)
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('planId without procedure: ' + appt_list[0]['planId'])
    #
    # jenkins_caller.run_assign_planid_reminder_2()
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('expected plan id: d7af319c-754a-4d21-afc9-b3388e3c22b6')
    # Helper.printout('actual plan id:   ' + appt_list[0]['planId'])
    # # assert appt_list[0]['planId'] == 'd7af319c-754a-4d21-afc9-b3388e3c22b6', 'planId should be default plan id.'
    #
    # # upload with appt with apptcode
    # Integration.upload_data_with_file(vetmatrix_account, 'template', '138032114_one_procedure.xml', env, clear=False)
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('planId after add apptcode: ' + appt_list[0]['planId'])
    #
    # jenkins_caller.run_assign_planid_reminder_2()
    # appt_list = UploadProcessor.get_appointment_from_db(vetmatrix_account.business_id)
    # Helper.printout('expected plan id: 64cac400-e9a0-11e9-901c-7ddf5bf4632f')
    # Helper.printout('actual plan id:   ' + appt_list[0]['planId'])

    # -------------------------------------------------------------------

    # UploadProcessor.clear_table_for_business(dental_account.business_id, 'BusinessDFLinkProperties')
    # UploadProcessor.clear_table_for_business(dental_account.business_id, 'BusinessInterval')
    # UploadProcessor.clear_table_for_business(dental_account.business_id, 'BusinessOptions')
    # UploadProcessor.clear_table_for_business(dental_account.business_id, 'UploadHistory')
    # UploadProcessor.clear_table_for_business(dental_account.business_id, 'CustomerOptions')
    Integration.upload_data_with_file(dental_account, 'output',
                                      '138000213.ng38D1_Delta.2019-10-07-23-02-44.xml',
                                      env, clear=False)
    # print UploadProcessor.get_customer_options_from_db(dental_account.business_id)
    # print UploadProcessor.get_business_system_from_db(dental_account.business_id)
    # print UploadProcessor.get_business_dflink_property_from_db(dental_account.business_id)
    # print UploadProcessor.get_business_interval_from_db(dental_account.business_id)
    # print UploadProcessor.get_business_option_from_db(dental_account.business_id)
    # print UploadProcessor.get_business_option_from_db(dental_account.business_id)





