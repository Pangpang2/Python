# -*- coding: UTF-8 -*-   
from dbReader import *
from lxml import etree
import time
import os


class dbWriter(object):
    def __init__(self, business_id, output_path):
        self.db_root = etree.Element('DBRoot')
        self.db_reader = dbReader(business_id)
        self.business_id = business_id
        self.output_path = output_path
        self.industry = self.get_industry()

        self.print_log('INFO', 'Start reading data from DB')
        self.print_log('INFO', 'Business Id: %s'%(business_id))
        self.print_log('INFO', 'Output Path: %s'%(output_path))

    def output_from_db(self):
        self.get_demandforce_entities_from_db()
        self.get_dflink_settings_from_db()
        self.get_account_from_db()
        self.get_animal_from_db()
        self.get_custom_from_db()
        self.get_diagnosis_from_db()
        self.get_eyewears_from_db()
        self.get_memberships_from_db()
        self.get_taxes_from_db()
        self.get_appointment_from_db()
        #get apptcode in get_appointment_from_db()
        self.get_calendarblock_from_db()
        self.get_customer_from_db()
        self.get_patientalert_from_db()
        self.get_provider_from_db()
        self.get_recall_from_db()
        self.get_recommendation_from_db()
        self.get_vehicle_from_db()
        if(self.industry == 2):
            self.get_dental_transaction_from_db()
        elif(self.industry == 1):
            self.get_auto_transaction_from_db()
        else:
            self.get_transaction_from_db()

        for child in self.db_root:
            self.reorder_xml_node(child, 'id')

        now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        file_name = '{0}_db_{1}_{2}.xml'.format(self.output_path, self.business_id,now)
        #file_name = self.output_path + '_db.xml'
        db_tree = etree.ElementTree(self.db_root)
        db_tree.write(file_name, encoding='utf-8',xml_declaration=True, pretty_print=True)

    def get_demandforce_entities_from_db(self):
        entities = self.db_reader.query_demandforce_entities()
        for entity in entities:
            elem = etree.SubElement(self.db_root, 'DemandForce')
            elem.attrib['systemOS']               = self.get_db_column(entity, 'SystemOS')
            elem.attrib['systemName']             = self.get_db_column(entity, 'SystemName')
            elem.attrib['systemUser']             = self.get_db_column(entity, 'SystemUser')
            elem.attrib['systemIPAddress']        = self.get_db_column(entity, 'SystemIPAddress')
            elem.attrib['antivirusSystemName']    = self.get_db_column(entity, 'AntivirusSystemName')
            elem.attrib['dotNETFrameworkVersion'] = self.get_db_column(entity, 'DotNETFrameworkVersion')
            elem.attrib['macAddress']             = self.get_db_column(entity, 'MACAddress')

    def get_dflink_settings_from_db(self):
        entities = self.db_reader.query_dflink_settings_entities()
        for entity in entities:
            elem = etree.SubElement(self.db_root, 'DFLinkSettings')
            elem.attrib['StartTimeFromTask']    = self.get_db_column(entity, 'StartTimeFromTask')
            elem.attrib['EndTimeFromTask']      = self.get_db_column(entity, 'EndTimeFromTask')
            elem.attrib['IntervalFromTask']     = self.get_db_column(entity, 'IntervalFromTask')
            elem.attrib['TwoWayInterval']       = self.get_db_column(entity, 'TwoWayInterval')
            elem.attrib['DFUpdateInterval']     = self.get_db_column(entity, 'DFUpdateInterval')
            elem.attrib['LastRunDFUpdate']      = self.get_db_column(entity, 'LastRunDFUpdate')
            elem.attrib['LastRunHourlySetting'] = self.get_db_column(entity, 'LastRunHourlySetting')
            elem.attrib['RestUrl']              = self.get_db_column(entity, 'RestUrl')
            elem.attrib['DeleteXML']            = self.get_db_column(entity, 'DeleteXML')
            elem.attrib['InstallDir']           = self.get_db_column(entity, 'InstallDir')
            elem.attrib['URL']                  = self.get_db_column(entity, 'URL')

    def get_account_from_db(self):
        entities = self.db_reader.query_accounts()
        parent = etree.SubElement(self.db_root, 'Accounts')
        for entity in entities:
            elem = etree.SubElement(parent, 'Account')
            elem.attrib['id']             = self.get_db_column(entity, 'ManagementSystemID')
            elem.attrib['overdueBalance'] = self.get_db_column(entity, 'Integer1')
            elem.attrib['openBalance']    = self.get_db_column(entity, 'Integer2')
            elem.attrib['totalRevenue']   = self.get_db_column(entity, 'Integer3')
            self.is_deleted_from_db(entity, elem, 'Status', '1')
            #elem.attrib['status']         = self.get_db_column(entity, 'Status')

    def get_animal_from_db(self):
        entities = self.db_reader.query_animals()
        parent = etree.SubElement(self.db_root, 'Animals')
        for entity in entities:
            elem = etree.SubElement(parent, 'Animal')
            elem.attrib['id']           = self.get_db_column(entity, 'ManagementSystemID')
            elem.attrib['name']         = self.get_db_column(entity, 'String1')
            elem.attrib['species']      = self.get_db_column(entity, 'String2')
            elem.attrib['breed']        = self.get_db_column(entity, 'String3')
            elem.attrib['coatColor']    = self.get_db_column(entity, 'String4')
            elem.attrib['sex']          = self.get_db_column(entity, 'String9')
            elem.attrib['provider']     = self.get_db_column(entity, 'String5')
            elem.attrib['providerName'] = self.get_db_column(entity, 'String6')
            elem.attrib['birthday']     = self.get_db_column(entity, 'Anniversary')
            elem.attrib['firstVisit']   = self.get_db_column(entity, 'FirstVisit')
            elem.attrib['lastVisit']    = self.get_db_column(entity, 'FirstVisit')
            elem.attrib['weight']       = self.get_db_column(entity, 'Double1')
            elem.attrib['weightUnits']  = self.get_db_column(entity, 'String7')
            self.is_deleted_from_db(entity, elem, 'Status', '1')

    def get_custom_from_db(self):
        entities = self.db_reader.query_customs()
        parent = etree.SubElement(self.db_root, 'Customs')
        for entity in entities:
            elem = etree.SubElement(parent, 'Custom')
            elem.attrib['id']     = self.get_db_column(entity, 'ManagementSystemID')
            elem.attrib['name']   = self.get_db_column(entity, 'String1')
            elem.attrib['value']  = self.get_db_column(entity, 'String2')
            self.is_deleted_from_db(entity, elem, 'Status', '1')

    def get_diagnosis_from_db(self):
        entities = self.db_reader.query_diagnosis()
        parent = etree.SubElement(self.db_root, 'Diagnosis')
        for entity in entities:
            elem = etree.SubElement(parent, 'Diagnosis')
            elem.attrib['id']           = self.get_db_column(entity, 'ManagementSystemID')
            elem.attrib['date']         = self.get_db_column(entity, 'Date1')
            elem.attrib['internalCode'] = self.get_db_column(entity, 'String1')
            elem.attrib['externalCode'] = self.get_db_column(entity, 'String2')
            elem.attrib['description']  = self.get_db_column(entity, 'String4')
            elem.attrib['category']     = self.get_db_column(entity, 'String3')
            elem.attrib['dismissed']    = self.get_db_column(entity, 'Boolean1')
            self.is_deleted_from_db(entity, elem, 'Status', '1')

    def get_eyewears_from_db(self):
        entities = self.db_reader.query_eyewears()
        parent = etree.SubElement(self.db_root, 'Eyewears')
        for entity in entities:
            elem = etree.SubElement(parent, 'Eyewear')
            elem.attrib['id']            = self.get_db_column(entity, 'ManagementSystemID')
            elem.attrib['dispensed']     = self.get_db_column(entity, 'Boolean2')
            elem.attrib['type']          = self.get_db_column(entity, 'String1')
            elem.attrib['dispensedDate'] = self.get_db_column(entity, 'Date2')
            elem.attrib['received']      = self.get_db_column(entity, 'Boolean1')
            elem.attrib['receivedDate']  = self.get_db_column(entity, 'Date1')
            self.is_deleted_from_db(entity, elem, 'Status', '1')

    def get_memberships_from_db(self):
        entities = self.db_reader.query_memberships()
        parent = etree.SubElement(self.db_root, 'Memberships')
        for entity in entities:
            elem = etree.SubElement(parent, 'Membership')
            elem.attrib['id']             = self.get_db_column(entity, 'ManagementSystemID')
            elem.attrib['member']         = self.get_db_column(entity, 'Boolean1')
            elem.attrib['startDate']      = self.get_db_column(entity, 'Date1')
            elem.attrib['expirationDate'] = self.get_db_column(entity, 'Date2')
            elem.attrib['cancelReason']   = self.get_db_column(entity, 'String2')
            elem.attrib['memberType']     = self.get_db_column(entity, 'String1')
            self.is_deleted_from_db(entity, elem, 'Status', '1')

    def get_taxes_from_db(self):
        entities = self.db_reader.query_taxes()
        parent = etree.SubElement(self.db_root, 'Taxes')
        for entity in entities:
            elem = etree.SubElement(parent, 'Tax')
            elem.attrib['id']                 = self.get_db_column(entity, 'ManagementSystemID')
            elem.attrib['pyFilingStatus']     = self.get_db_column(entity, 'String1')
            elem.attrib['cyEstimatedQ1']      = self.get_db_column(entity, 'Integer1')
            elem.attrib['cyEstimatedQ2']      = self.get_db_column(entity, 'Integer2')
            elem.attrib['cyEstimatedQ3']      = self.get_db_column(entity, 'Integer3')
            elem.attrib['cyEstimatedQ4']      = self.get_db_column(entity, 'Integer4')
            elem.attrib['pyIncomeWages']      = self.get_db_column(entity, 'Integer5')
            elem.attrib['pyIncomeInterest']   = self.get_db_column(entity, 'Integer6')
            elem.attrib['pyIncomeRefund']     = self.get_db_column(entity, 'Integer7')
            elem.attrib['pyIncomeDividend']   = self.get_db_column(entity, 'Integer8')
            elem.attrib['pyIncomeAlimony']    = self.get_db_column(entity, 'Integer9')
            elem.attrib['pyIncomeBusiness']   = self.get_db_column(entity, 'Integer10')
            elem.attrib['pyIncomeCapitalGL']  = self.get_db_column(entity, 'Integer11')
            elem.attrib['pyIncomeTaxableIRA'] = self.get_db_column(entity, 'Integer12')
            elem.attrib['pyIncomeOther']      = self.get_db_column(entity, 'Integer13')
            elem.attrib['pyIncomeTotal']      = self.get_db_column(entity, 'Integer14')
            self.is_deleted_from_db(entity, elem, 'Status', '1')

    def get_appointment_from_db(self):
        entities = self.db_reader.query_appointments()
        parent = etree.SubElement(self.db_root, 'Appointments')
        for entity in entities:
            elem = etree.SubElement(parent, 'Appointment')
            elem.attrib['id']            = self.get_db_column(entity, 'BusinessAppointmentID')
            elem.attrib['provider']      = self.get_db_column(entity, 'Provider')
            elem.attrib['providerName']  = self.get_db_column(entity, 'ProviderName')
            elem.attrib['description']   = self.get_db_column(entity, 'Services')
            elem.attrib['duration']      = self.get_db_column(entity, 'Duration')
            elem.attrib['date']          = self.get_db_column(entity, 'ScheduledDate')
            elem.attrib['confirmedDate'] = self.get_db_column(entity, 'ExternalConfirmedTime')
            elem.attrib['facility']      = self.get_db_column(entity, 'Facility')
            elem.attrib['code']          = self.get_db_column(entity, 'code')
            elem.attrib['providerId']    = self.get_db_column(entity, 'ProviderID')
            self.is_deleted_from_db(entity, elem, 'Status', '7')
            appt_id = self.get_db_column(entity, 'ID')
            self.get_apptcode_from_db(elem, appt_id)

    def get_apptcode_from_db(self, parent, appt_code):
        entities = self.db_reader.query_apptcodes(appt_code)
        for entity in entities:
            elem = etree.SubElement(parent, 'ApptCode')
            elem.attrib['id']           = self.get_db_column(entity, 'BusinessApptCodeID')
            elem.attrib['code']         = self.get_db_column(entity, 'CODE')
            elem.attrib['description']  = self.get_db_column(entity, 'Description')
            elem.attrib['externalCode'] = self.get_db_column(entity, 'ExternalCode')
            self.is_deleted_from_db(entity, elem, 'ApptCodeStatus', '7')

    def get_calendarblock_from_db(self):
        entities = self.db_reader.query_calendarblocks()
        parent = etree.SubElement(self.db_root, 'CalendarBlocks')

        for entity in entities:
            elem = etree.SubElement(parent, 'CalendarBlock')
            elem.attrib['id']            = self.get_db_column(entity, 'BusinessBlockID')
            elem.attrib['scheduledDate'] = self.get_db_column(entity, 'ScheduledDate')
            elem.attrib['title']         = self.get_db_column(entity, 'Title')
            elem.attrib['duration']      = self.get_db_column(entity, 'Duration')
            elem.attrib['facility']      = self.get_db_column(entity, 'Facility')
            elem.attrib['notes']         = self.get_db_column(entity, 'Notes')
            self.is_deleted_from_db(entity, elem, 'Status', '7')


    def get_customer_from_db(self):
        entities = self.db_reader.query_customers()
        parent = etree.SubElement(self.db_root, 'Customers')
        for entity in entities:
            elem = etree.SubElement(parent, 'Customer')
            elem.attrib['id']                      = self.get_db_column(entity, 'BusinessCustomerId')
            elem.attrib['parentId']                = self.get_db_column(entity, 'HoHID')
            elem.attrib['firstVisit']              = self.get_db_column(entity, 'FirstVisit')
            elem.attrib['lastVisit']               = self.get_db_column(entity, 'LastVisit')
            elem.attrib['type']                    = self.get_db_column(entity, 'Type')
            elem.attrib['insuranceType']           = self.get_db_column(entity, 'Insurance')
            elem.attrib['patientType']             = self.get_db_column(entity, 'PatientType')
            elem.attrib['lastMaintenanceDate']     = self.get_db_column(entity, 'LastMaintenance')
            elem.attrib['maintenanceInterval']     = self.get_db_column(entity, 'MaintenanceInterval')
            elem.attrib['maintenanceIntervalUnit'] = self.get_db_column(entity, 'MaintenanceIntervalUnit')
            elem.attrib['referral']                = self.get_db_column(entity, 'Referral')
            elem.attrib['points']                  = self.get_db_column(entity, 'Points')
            self.is_deleted_from_db(entity, elem, 'Status', '4')

    def get_patientalert_from_db(self):
        entities = self.db_reader.query_patientalerts()
        parent = etree.SubElement(self.db_root, 'PatientAlerts')
        for entity in entities:
            elem = etree.SubElement(parent, 'PatientAlert')
            elem.attrib['id']          = self.get_db_column(entity, 'PatientAlertID')
            elem.attrib['startDate']   = self.get_db_column(entity, 'StartDate')
            elem.attrib['endDate']     = self.get_db_column(entity, 'EndDate')
            elem.attrib['description'] = self.get_db_column(entity, 'Description')
            self.is_deleted_from_db(entity, elem, 'Status', '7,1')

    def get_provider_from_db(self):
        entities = self.db_reader.query_providers()
        parent = etree.SubElement(self.db_root, 'Providers')
        for entity in entities:
            elem = etree.SubElement(parent, 'Provider')
            elem.attrib['id']                   = self.get_db_column(entity, 'BusinessProviderID')
            elem.attrib['firstName']            = self.get_db_column(entity, 'FirstName')
            elem.attrib['middleName']           = self.get_db_column(entity, 'MiddleName')
            elem.attrib['lastName']             = self.get_db_column(entity, 'LastName')
            elem.attrib['bookingName']          = self.get_db_column(entity, 'BookingName')
            elem.attrib['code']                 = self.get_db_column(entity, 'CODE')
            elem.attrib['identificationNumber'] = self.get_db_column(entity, 'IdentificationNumber')
            elem.attrib['active']               = self.get_db_column(entity, 'Active')
            elem.attrib['type']                 = self.get_db_column(entity, 'Type')
            self.is_deleted_from_db(entity, elem, 'Status', '7')

    def get_recall_from_db(self):
        entities = self.db_reader.query_recalls()
        parent = etree.SubElement(self.db_root, 'Recalls')
        for entity in entities:
            elem = etree.SubElement(parent, 'Recall')
            elem.attrib['id']       = self.get_db_column(entity, 'BusinessRecallDueDateID')
            elem.attrib['date']     = self.get_db_column(entity, 'date')
            elem.attrib['type']     = self.get_db_column(entity, 'type')
            elem.attrib['provider'] = self.get_db_column(entity, 'provider')
            elem.attrib['status']   = self.get_db_column(entity, 'status')
            self.is_deleted_from_db(entity, elem, 'RecallStatus', '7')

    def get_recommendation_from_db(self):
        entities = self.db_reader.query_recommendations()
        parent = etree.SubElement(self.db_root, 'Recommendations')
        for entity in entities:
            elem = etree.SubElement(parent, 'Recommendation')
            elem.attrib['id']           = self.get_db_column(entity, 'BusinessRecommendationID')
            elem.attrib['date']         = self.get_db_column(entity, 'Date')
            elem.attrib['description']  = self.get_db_column(entity, 'Description')
            elem.attrib['type']         = self.get_db_column(entity, 'Type')
            self.is_deleted_from_db(entity, elem, 'Status', '1')

    def get_vehicle_from_db(self):
        entities = self.db_reader.query_vehicles()
        parent = etree.SubElement(self.db_root, 'Vehicles')
        for entity in entities:
            elem = etree.SubElement(parent, 'Vehicle')
            elem.attrib['id']                 = self.get_db_column(entity, 'ShopVehicleID')
            elem.attrib['year']               = self.get_db_column(entity, 'ModelYear')
            elem.attrib['make']               = self.get_db_column(entity, 'Make')
            elem.attrib['model']              = self.get_db_column(entity, 'Model')
            elem.attrib['driverType']         = self.get_db_column(entity, 'DriverType')
            elem.attrib['curMilesUpdate']     = self.get_db_column(entity, 'MilesAtUpdate')
            elem.attrib['curMilesUpdateDate'] = self.get_db_column(entity, 'LastMileageDate')
            elem.attrib['engineType']         = self.get_db_column(entity, 'EngineType')
            elem.attrib['vin']                = self.get_db_column(entity, 'VIN')
            elem.attrib['odometerDate']       = self.get_db_column(entity, 'LastMileageDate')
            elem.attrib['odometer']           = self.get_db_column(entity, 'MilesAtUpdate')
            elem.attrib['license']            = self.get_db_column(entity, 'License')
            elem.attrib['licenseState']       = self.get_db_column(entity, 'LicenseState')
            self.is_deleted_from_db(entity, elem, 'Status', '1')

    def get_transaction_from_db(self):
        entities = self.db_reader.query_transactions()
        parent = etree.SubElement(self.db_root, 'Transactions')
        for entity in entities:
            elem = etree.SubElement(parent, 'Transaction')
            elem.attrib['type']         = self.get_db_column(entity, 'Type')
            elem.attrib['id']           = self.get_db_column(entity, 'ExternalVisitID')
            elem.attrib['date']         = self.get_db_column(entity, 'VisitDate')
            elem.attrib['charge']       = self.get_db_column(entity, 'Revenue')
            elem.attrib['provider']     = self.get_db_column(entity, 'Provider')
            elem.attrib['providerName'] = self.get_db_column(entity, 'ProviderName')
            elem.attrib['category']     = self.get_db_column(entity, 'Category')
            elem.attrib['SubCategory']  = self.get_db_column(entity, 'Subcategory')
            elem.attrib['code']         = self.get_db_column(entity, 'CustomField2')
            elem.attrib['description']  = self.get_db_column(entity, 'ServiceDescription')
            elem.attrib['status']       = self.get_db_column(entity, 'VisitStatus')
            elem.attrib['proivderId']   = self.get_db_column(entity, 'ProviderID')

    def get_dental_transaction_from_db(self):
        entities = self.db_reader.query_dental_transactions()
        parent = etree.SubElement(self.db_root, 'DentalTransactions')
        for entity in entities:
            elem = etree.SubElement(parent, 'DentalTransaction')
            elem.attrib['id']           = self.get_db_column(entity, 'PracticeVisitID')
            elem.attrib['date']         = self.get_db_column(entity, 'VisitDate')
            elem.attrib['charge']       = self.get_db_column(entity, 'Revenue')
            elem.attrib['provider']     = self.get_db_column(entity, 'Provider')
            elem.attrib['providerName'] = self.get_db_column(entity, 'ProviderName')
            elem.attrib['type']         = self.get_db_column(entity, 'Type')
            elem.attrib['category']     = self.get_db_column(entity, 'Category')
            elem.attrib['code']         = self.get_db_column(entity, 'CustomField1')
            elem.attrib['description']  = self.get_db_column(entity, 'Procedures')
            elem.attrib['status']       = self.get_db_column(entity, 'VisitStatus')
            elem.attrib['procedure']    = self.get_db_column(entity, 'FamilyMemberID')
            elem.attrib['providerId']   = self.get_db_column(entity, 'ProviderID')

    def get_auto_transaction_from_db(self):
        entities = self.db_reader.query_auto_transactions()
        parent = etree.SubElement(self.db_root, 'AutoTransactions')
        for entity in entities:
            elem = etree.SubElement(parent, 'AutoTransaction')
            elem.attrib['id']           = self.get_db_column(entity, 'RepairID')
            elem.attrib['date']         = self.get_db_column(entity, 'RepairDate')
            elem.attrib['charge']       = self.get_db_column(entity, 'RepairAmount')
            elem.attrib['provider']     = self.get_db_column(entity, 'Provider')
            elem.attrib['providerName'] = self.get_db_column(entity, 'ProviderName')
            elem.attrib['type']         = self.get_db_column(entity, 'Type')
            elem.attrib['category']     = self.get_db_column(entity, 'Category')
            elem.attrib['code']         = self.get_db_column(entity, 'ServiceCode')
            elem.attrib['description']  = self.get_db_column(entity, 'RepairDescription')
            elem.attrib['status']       = self.get_db_column(entity, 'NoticeType')
            elem.attrib['miles']        = self.get_db_column(entity, 'VehicleMileage')
            elem.attrib['odometer']     = self.get_db_column(entity, 'VehicleMileage')

    def get_industry(self):
        industries = self.db_reader.query_industry_from_db()
        for industry in industries:
            return industry['Industry']

    def get_db_column(self, row, name):
        if row[name] is None:
            return ''
        else:
            return str(row[name])

    def is_deleted_from_db(self, entity, elem, db_field, status_list):
        status = self.get_db_column(entity, db_field)
        for status_num in status_list:
            if(status == status_num):
                elem.attrib['status'] = status
                elem.attrib['isDeleted'] = 'true'
                break

    def reorder_xml_node(self, parent, attr):
        parent[:] = sorted(parent, key=lambda child: child.get(attr))


    def print_log(self, log_level, log_info):
        print('[%s] %s'%(log_level, log_info))


