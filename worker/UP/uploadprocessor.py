import dbclient
from common import Environment, Industry
from d3one import D3One
from tools import Tools


class UploadProcessor:
    upload_path_local = r'C:\usr\local\d3one\in\d30'
    env = Environment.STG

    @staticmethod
    def clear_invalid_file():
        if UploadProcessor.env == Environment.LOCAL:
            upload_path = UploadProcessor.upload_path_local
            Tools.clear_invalid_file(upload_path)
        else:
            print('Is not ready for STG.')

    @staticmethod
    def check_invalid_file():
        if UploadProcessor.env == Environment.LOCAL:
            upload_path = UploadProcessor.upload_path_local
            exists = Tools.check_invalid_file_exists(upload_path)
            if exists == True:
                raise Exception('Uploaded file is invalid. %s' %upload_path)
        else:
            print('Is not ready for STG.')

    @staticmethod
    def check_upload_history(business_id, retry=10):
        while retry:
            query = "SELECT * FROM UploadHistory WHERE BusinessID='%s' ORDER BY LogDate DESC"%business_id
            record = dbclient.run_query(query, UploadProcessor.env)
            if record:
                print(record[0])
                return
            retry -= 1
            Tools.sleep(3)

        raise Exception('Could not find upload history for business %s'%business_id)

    @staticmethod
    def check_upload_data(d3, account, check_list=D3One.entities, is_delete=False):
        print('Check upload data')
        document = d3.parse_xml()
        for entity in check_list:
            print(entity + '  ')
            func_name = entity.lower()
            if entity == 'Transaction':
                if account.industry == Industry.DENTAL:
                    func_name = 'dental_visit'
                elif account.industry == Industry.AUTO:
                    func_name = 'auto_visit'
                else:
                    func_name = 'visit'

            f = getattr(UploadProcessor, 'get_{0}_from_db'.format(func_name))
            row_list = f(account.business_id)
            for row in row_list:
                print(row)
            if not is_delete:
                Tools.compare_entity_list(entity, document[entity], row_list)
    
    @staticmethod
    def clear_uploaded_data_for_business(business_id):
        print('Clear updated data for business {0}'.format(business_id))
        query_string = "DELETE FROM CalendarBlock  WHERE BusinessID={business_id};" \
            "DELETE FROM Provider  WHERE BusinessID={business_id};" \
            "DELETE FROM Customer WHERE BusinessID={business_id};" \
            "DELETE FROM CustomerPoints  WHERE BusinessID={business_id};" \
            "DELETE FROM Appointment  WHERE BusinessID={business_id};" \
            "DELETE FROM ApptCode  WHERE BusinessID={business_id};" \
            "DELETE FROM DentalVisit  WHERE BusinessID={business_id};" \
            "DELETE FROM AutoVisit  WHERE BusinessID={business_id};" \
            "DELETE FROM Visit  WHERE BusinessID={business_id};" \
            "DELETE FROM PatientAlert  WHERE BusinessID={business_id};" \
            "DELETE FROM RecallDueDate  WHERE BusinessID={business_id};" \
            "DELETE FROM Entity  WHERE BusinessID={business_id} AND Type in (1,2,3,4,5,6,7);" \
            "DELETE FROM CustomerOptions WHERE BusinessID={business_id};" \
            "DELETE FROM Recommendation  WHERE BusinessID={business_id};" \
            "DELETE FROM Vehicle  WHERE BusinessID={business_id}".format(business_id=business_id)

        for query in query_string.split(';'):
            dbclient.run_query(query.lstrip(' '), UploadProcessor.env)

    @staticmethod
    def clear_upload_history_for_business(business_id):
        print('Clear UploadHistory for business {0}'.format(business_id))
        dbclient.run_query("DELETE FROM UploadHistory WHERE BusinessID={business_id}".format(business_id=business_id))

    @staticmethod
    def clear_appointment_for_business(business_id):
        print('Clear appointment data for business {0}'.format(business_id))
        dbclient.run_query("DELETE FROM Appointment WHERE BusinessID={business_id}".format(business_id=business_id))
        dbclient.run_query("DELETE FROM ApptCode WHERE BusinessID={business_id}".format(business_id=business_id))

    @staticmethod
    def clear_customer_for_business(business_id):
        print('Clear Customer data for business {0}'.format(business_id))
        dbclient.run_query("DELETE FROM Customer WHERE BusinessID={business_id}".format(business_id=business_id))

    @staticmethod
    def clear_table_for_business(business_id, table):
        print('Clear {0} data for business {1}'.format(table, business_id))
        dbclient.run_query("DELETE FROM {table} WHERE BusinessID={business_id}".format(table=table, business_id=business_id))

    @staticmethod
    def get_business_system_from_db(business_id):
        columns = " * "
        query = "SELECT {0} FROM BusinessSystem WHERE BusinessID='{1}'".format(columns, business_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_business_interval_from_db(business_id):
        columns = " * "
        query = "SELECT {0} FROM BusinessInterval WHERE BusinessID='{1}'".format(columns, business_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_business_option_from_db(business_id):
        columns = " * "
        query = "SELECT {0} FROM BusinessOptions WHERE BusinessID='{1}'".format(columns, business_id)
        return dbclient.run_query(query, UploadProcessor.env)


    @staticmethod
    def get_business_dflink_property_from_db(business_id):
        columns = " * "
        query = "SELECT {0} FROM BusinessDFLinkProperties WHERE BusinessID='{1}'".format(columns, business_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_calendarblock_from_db(business_id):
        columns = "BusinessBlockID as id,ScheduledDate,Duration,Facility,Title,Notes,Status"
        query = "SELECT {0} FROM CalendarBlock WHERE BusinessID='{1}'".format(columns, business_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_provider_from_db(businsess_id):
        columns = "BusinessProviderID as id,Status,CODE,FirstName,MiddleName,LastName,BookingName,IdentificationNumber,Active,type"
        query = "SELECT {0} FROM Provider WHERE BusinessID = {1}".format(columns, businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_customer_from_db(businsess_id):
        row = dbclient.run_query('SELECT * FROM CustomerPoints WHERE BusinessID={0}'.format(businsess_id))
        print('CustomerPoints:' + str(row[0]['Points']))
        columns = "BusinessCustomerId as id,Status,HoHID as parentid,FirstVisit,LastVisit,Type,Insurance as insuranceType," \
                  "PatientType,LastMaintenance as lastMaintenanceDate,OptedIn,MaintenanceInterval,MaintenanceIntervalUnit,Referral"
        query = "SELECT {0} FROM Customer WHERE BusinessID = {1}".format(columns, businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_customer_options_from_db(businsess_id):
        columns = "*"
        query = "SELECT {0} FROM CustomerOptions WHERE BusinessID = {1}".format(columns, businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_demographics_from_db(businsess_id):
        columns = "firstName,lastName,middleName,gender,birthday, Birthday AS birthdayMonth,Birthday asbirthdayDay," \
                  "address1,address2,city,state,zipcode AS zip,email, workphone,homephone,cellphone,otherphone1," \
                  "otherphone2,alias,NAME"
        query = "SELECT {0} FROM Customer WHERE BusinessID = {1}".format(columns, businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_customer_points_from_db(businsess_id):
        query = "SELECT * FROM CustomerPoints WHERE BusinessID = {0}".format(businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_appointment_from_db(businsess_id):
        columns = "BusinessAppointmentID as id, code,Status,Services as description,providerName,facility,duration,providerId," \
                  "provider,ScheduledDate as date, type,ExternalConfirmedTime as confirmedDate, planId"
        query = "SELECT {0} FROM Appointment WHERE BusinessID = {1}".format(columns, businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_apptcode_from_db(businsess_id):
        columns = "BusinessApptCodeID as id,code,externalCode,description,ApptCodeStatus"
        query = "SELECT {0} FROM ApptCode WHERE BusinessID = {1}".format(columns, businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_dental_visit_from_db(businsess_id):
        columns = "PracticeVisitID as id, VisitDate as date, category,CustomField1 as code,providerName,provider,Revenue as charge,VisitDate," \
                  "type,Procedures as description,VisitStatus as status,FamilyMemberID as 'procedure',ProviderID"
        query = "SELECT {0} FROM DentalVisit WHERE BusinessID = {1}".format(columns, businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_auto_visit_from_db(businsess_id):
        columns = "RepairID as id, RepairDate as date, RepairAmount as charge,Provider,ProviderName,Type,Category," \
                  "ServiceCode as code, RepairDescription as description, NoticeType as status, VehicleMileage as miles," \
                  "VehicleMileage as odometer"
        query = "SELECT {0} FROM AutoVisit WHERE BusinessID = {1}".format(columns, businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_visit_from_db(businsess_id):
        columns = "ExternalVisitID as id, VisitDate as date,Revenue as charge,Provider, ProviderName, Category,Subcategory," \
                  "CustomField2 as code,ServiceDescription as description,VisitStatus as status,ProviderID "
        query = "SELECT {0} FROM Visit WHERE BusinessID = {1}".format(columns, businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_patientalert_from_db(businsess_id):
        columns = "PatientAlertID as id,STATUS,startDate,endDate,description"
        query = "SELECT {0} FROM PatientAlert WHERE BusinessID = {1}".format(columns,businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_recall_from_db(businsess_id):
        columns = "BusinessRecallDueDateID as id, date,status,type,provider,RecallStatus,RecallTypeID "
        query = "SELECT {0} FROM RecallDueDate WHERE BusinessID = {1}".format(columns, businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_recommendation_from_db(businsess_id):
        columns = "BusinessRecommendationID as id,Status,Date,Description, Type "
        query = "SELECT {0} FROM Recommendation WHERE BusinessID = {1}".format(columns, businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_animal_from_db(businsess_id):
        columns = "ManagementSystemId as id,Status, String1 as name, String2 as species, String3 as breed," \
                  "String4 as coatColor, String9 as sex, String5 as provider, String6 as providerName," \
                  "Anniversary as birthday, FirstVisit,LastVisit, Double1 as weight, String7 as weightUnits"
        query = "SELECT {0} FROM Entity WHERE BusinessID = {1} AND Type={2}".format(columns, businsess_id, 1)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_eyewear_from_db(businsess_id):
        columns = "ManagementSystemID as id, Status, CASE Boolean2 WHEN '1' THEN 'True' WHEN '0' THEN 'False' END AS dispensed," \
                  " String1 as type,Date2 as dispensedDate,CASE Boolean1 WHEN '1' THEN 'True' WHEN '0' THEN 'False' END AS received," \
                  " Date1 as receivedDate"
        query = "SELECT {0} FROM Entity WHERE BusinessID = {1} AND Type={2}".format(columns, businsess_id, 2)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_diagnosis_from_db(businsess_id):
        columns = "ManagementSystemId as id,Status, Date1 as date,String1 as internalCode,String2 as externalCode,String4 as description,String3 as category, Boolean1 as dismissed"
        query = "SELECT {0} FROM Entity WHERE BusinessID = {1} AND Type={2}".format(columns, businsess_id, 3)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_account_from_db(businsess_id):
        columns = "ManagementSystemID as id,Status,Integer1 as overdueBalance,Integer2 as openBalance,Integer3 as totalRevenue"
        query = "SELECT {0} FROM Entity WHERE BusinessID = {1} AND Type={2}".format(columns, businsess_id, 4)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_custom_from_db(businsess_id):
        columns = "ManagementSystemID as id,Status, String1 as name, String2 as value"
        query = "SELECT {0} FROM Entity WHERE BusinessID = {1} AND Type={2}".format(columns, businsess_id, 5)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_tax_from_db(businsess_id):
        columns = "ManagementSystemID as id, Status,String1 as pyFilingStatus, Integer1 as cyEstimatedQ1, Integer2 as cyEstimatedQ2," \
                  "Integer3 as cyEstimatedQ3,Integer4 as cyEstimatedQ4,Integer5 as pyIncomeWages,Integer6 as pyIncomeInterest," \
                  "Integer7 as pyIncomeRefund,Integer8 as pyIncomeDividend,Integer9 as pyIncomeAlimony,Integer10 as pyIncomeBusiness," \
                  "Integer11 as pyIncomeCapitalGL,Integer12 as pyIncomeTaxableIRA,Integer13 as pyIncomeOther,Integer14 as pyIncomeTotal"
        query = "SELECT {0} FROM Entity WHERE BusinessID = {1} AND Type={2}".format(columns, businsess_id, 6)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_membership_from_db(businsess_id):
        columns = "ManagementSystemID as id,Status, Boolean1 as member, Date1 as startDate, Date2 as expirationDate, String2 as cancelReason, String1 as memberType"
        query = "SELECT {0} FROM Entity WHERE BusinessID = {1} AND Type={2}".format(columns, businsess_id, 7)
        return dbclient.run_query(query, UploadProcessor.env)

    @staticmethod
    def get_vehicle_from_db(businsess_id):
        columns = "ShopVehicleID as id,Status,License,LicenseState,Make,Model,VIN,YEAR(ModelYear) as year"
        query = "SELECT {0} FROM Vehicle WHERE BusinessID = {1} ".format(columns, businsess_id)
        return dbclient.run_query(query, UploadProcessor.env)



