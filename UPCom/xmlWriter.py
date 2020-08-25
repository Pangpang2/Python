# -*- coding: UTF-8 -*-   
from xmlReader import *
from datetime import datetime
from datetime import timedelta
import time
import os
import re

class xmlWriter(object):
    def __init__(self, file, industry, business_id, output_path):
        self.xml_root = etree.Element('XMLRoot')
        self.xml_reader = xmlReader(file)
        self.industry = industry
        self.business_id = business_id
        self.output_path = output_path
        self.option_today = self.get_option_today_from_xml()

        self.print_log('INFO', 'xml: %s'%(file))
        self.print_log('INFO', 'Option Today: %s'%(self.option_today))
        self.print_log('INFO', 'Output Path: %s'%(self.output_path))

    def output_from_xml(self):

        self.get_demandforce_entities_from_xml()
        self.get_dflink_settings_from_xml()
        self.get_account_from_xml()
        self.get_animal_from_xml()
        self.get_custom_from_xml()
        self.get_diagnosis_from_xml()
        self.get_eyewears_from_xml()
        self.get_memberships_from_xml()
        self.get_taxes_from_xml()
        self.get_appointment_from_xml()
        #get apptcode in get_appointment_from_xml()
        self.get_calendarblock_from_xml()
        self.get_customer_from_xml()
        self.get_patientalert_from_xml()
        self.get_provider_from_xml()
        self.get_recall_from_xml()
        self.get_recommendation_from_xml()
        self.get_vehicle_from_xml()
        if(self.industry == 2):
            self.get_dental_transaction_from_xml()
        elif(self.industry == 1):
            self.get_auto_transaction_from_xml()
        else:
            self.get_transaction_from_xml()

        for child in self.xml_root:
            self.reorder_xml_node(child, 'id')

        now = time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
        file_name = '{0}xml_{1}_{2}.xml'.format(self.output_path, self.business_id,now)
        #file_name = self.output_path + 'xml.xml'
        xml_tree = etree.ElementTree(self.xml_root)
        xml_tree.write(file_name, encoding='utf-8',xml_declaration=True,pretty_print=True)

    def get_option_today_from_xml(self):
        entities = self.xml_reader.read_option_today()
        for entity in entities:
            return self.get_xml_datetime_attrib(entity, 'extractDateTime')

    def get_demandforce_entities_from_xml(self):
        entities = self.xml_reader.read_demandforce_entities()
        for entity in entities:
            elem = etree.SubElement(self.xml_root, 'DemandForce')
            elem.attrib['systemOS']               = self.get_xml_attrib(entity, 'systemOS')
            elem.attrib['systemName']             = self.get_xml_attrib(entity, 'systemName')
            elem.attrib['systemUser']             = self.get_xml_attrib(entity, 'systemUser')
            elem.attrib['systemIPAddress']        = self.get_xml_attrib(entity, 'systemIPAddress')
            elem.attrib['antivirusSystemName']    = self.get_xml_attrib(entity, 'antiVirusName')
            elem.attrib['dotNETFrameworkVersion'] = self.get_xml_attrib(entity, 'dotNETFrameworkVersion')
            elem.attrib['macAddress']             = self.get_xml_attrib(entity, 'macAddress')

    def get_dflink_settings_from_xml(self):
        entity = self.xml_reader.read_dflink_settings_entities()
        elem = etree.SubElement(self.xml_root, 'DFLinkSettings')
        elem.attrib['StartTimeFromTask']    = self.get_xml_attrib(entity, 'StartTimeFromTask')
        elem.attrib['EndTimeFromTask']      = self.get_xml_attrib(entity, 'EndTimeFromTask')
        elem.attrib['IntervalFromTask']     = self.get_xml_attrib(entity, 'IntervalFromTask')
        elem.attrib['TwoWayInterval']       = self.get_xml_attrib(entity, 'TwoWayInterval')
        elem.attrib['DFUpdateInterval']     = self.get_xml_attrib(entity, 'DFUpdateInterval')
        elem.attrib['LastRunDFUpdate']      = self.get_xml_datetime_attrib(entity, 'LastRunDFUpdate')
        elem.attrib['LastRunHourlySetting'] = self.get_xml_datetime_attrib(entity, 'LastRunHourlySetting')
        elem.attrib['RestUrl']              = self.get_xml_attrib(entity, 'RESTURL')
        elem.attrib['DeleteXML']            = self.get_xml_attrib(entity, 'DeleteXML')
        elem.attrib['InstallDir']           = self.get_xml_attrib(entity, 'InstallDir')
        elem.attrib['URL']                  = self.get_xml_attrib(entity, 'URL')

    def get_account_from_xml(self):
        entities = self.xml_reader.read_accounts()
        parent = etree.SubElement(self.xml_root, 'Accounts')
        for entity in entities:
            elem = etree.SubElement(parent, 'Account')
            elem.attrib['id']             = self.get_xml_attrib(entity, 'id')
            elem.attrib['overdueBalance'] = self.get_xml_attrib(entity, 'overdueBalance')
            elem.attrib['openBalance']    = self.get_xml_attrib(entity, 'openBalance')
            elem.attrib['totalRevenue']   = self.get_xml_attrib(entity, 'totalRevenue')
        parent = self.reorder_xml_node(parent, 'id')

    def get_animal_from_xml(self):
        entities = self.xml_reader.read_animals()
        parent = etree.SubElement(self.xml_root, 'Animals')
        for entity in entities:
            elem = etree.SubElement(parent, 'Animal')
            elem.attrib['id']           = self.get_xml_attrib(entity, 'id')
            elem.attrib['name']         = self.get_xml_attrib(entity, 'name')
            elem.attrib['species']      = self.get_xml_attrib(entity, 'species')
            elem.attrib['breed']        = self.get_xml_attrib(entity, 'breed')
            elem.attrib['coatColor']    = self.get_xml_attrib(entity, 'coatColor')
            elem.attrib['sex']          = self.get_xml_attrib(entity, 'sex')
            elem.attrib['provider']     = self.get_xml_attrib(entity, 'provider')
            elem.attrib['providerName'] = self.get_xml_attrib(entity, 'providerName')
            elem.attrib['birthday']     = self.get_xml_date_attrib(entity, 'birthday')
            elem.attrib['firstVisit']   = self.get_xml_date_attrib(entity, 'firstVisit')
            elem.attrib['lastVisit']    = self.get_xml_date_attrib(entity, 'lastVisit')
            elem.attrib['weight']       = self.get_xml_float_attrib(entity, 'weight', 1)
            elem.attrib['weightUnits']  = self.get_xml_attrib(entity, 'weightUnits')

    def get_custom_from_xml(self):
        entities = self.xml_reader.read_customs()
        parent = etree.SubElement(self.xml_root, 'Customs')
        for entity in entities:
            elem = etree.SubElement(parent, 'Custom')
            elem.attrib['id']    = self.get_xml_attrib(entity, 'id')
            elem.attrib['name']  = self.get_xml_attrib(entity, 'name')
            elem.attrib['value'] = self.get_xml_attrib(entity, 'value')

    def get_diagnosis_from_xml(self):
        entities = self.xml_reader.read_diagnosis()
        parent = etree.SubElement(self.xml_root, 'Diagnosis')
        for entity in entities:
            elem = etree.SubElement(parent, 'Diagnosis')
            elem.attrib['id']           = self.get_xml_attrib(entity, 'id')
            elem.attrib['date']         = self.get_xml_datetime_attrib(entity, 'date')
            elem.attrib['internalCode'] = self.get_xml_attrib(entity, 'internalCode')
            elem.attrib['externalCode'] = self.get_xml_attrib(entity, 'externalCode')
            elem.attrib['description']  = self.get_xml_attrib(entity, 'description')
            elem.attrib['category']     = self.get_xml_attrib(entity, 'category')
            elem.attrib['dismissed']    = self.get_xml_attrib(entity, 'dismissed')

    def get_eyewears_from_xml(self):
        entities = self.xml_reader.read_eyewears()
        parent = etree.SubElement(self.xml_root, 'Eyewears')
        for entity in entities:
            elem = etree.SubElement(parent, 'Eyewear')
            elem.attrib['id']            = self.get_xml_attrib(entity, 'id')
            elem.attrib['dispensed']     = self.get_xml_bool_attrib(entity, 'dispensed')
            elem.attrib['type']          = self.get_xml_attrib(entity, 'type')
            elem.attrib['dispensedDate'] = self.get_xml_datetime_attrib(entity, 'dispensedDate')
            elem.attrib['received']      = self.get_xml_bool_attrib(entity, 'received')
            elem.attrib['receivedDate']  = self.get_xml_datetime_attrib(entity, 'receivedDate')

    def get_memberships_from_xml(self):
        entities = self.xml_reader.read_memberships()
        parent = etree.SubElement(self.xml_root, 'Memberships')
        for entity in entities:
            elem = etree.SubElement(parent, 'Membership')
            elem.attrib['id']             =self.get_xml_attrib(entity, 'Id')
            if(elem.attrib['id'] is ''):
                elem.attrib['id']         =self.get_xml_attrib(entity, 'id')
            elem.attrib['member']         =self.get_xml_bool_attrib(entity, 'member')
            elem.attrib['startDate']      =self.get_xml_datetime_attrib(entity, 'startDate')
            elem.attrib['expirationDate'] =self.get_xml_datetime_attrib(entity, 'expirationDate')
            elem.attrib['cancelReason']   =self.get_xml_attrib(entity, 'cancelReason')
            elem.attrib['memberType']     =self.get_xml_attrib(entity, 'memberType')

    def get_taxes_from_xml(self):
        entities = self.xml_reader.read_taxes()
        parent = etree.SubElement(self.xml_root, 'Taxes')
        for entity in entities:
            elem = etree.SubElement(parent, 'Tax')
            elem.attrib['id']                 = self.get_xml_attrib(entity, 'id')
            elem.attrib['pyFilingStatus']     = self.get_xml_attrib(entity, 'pyFilingStatus')
            elem.attrib['cyEstimatedQ1']      = self.get_xml_attrib(entity, 'cyEstimatedQ1')
            elem.attrib['cyEstimatedQ2']      = self.get_xml_attrib(entity, 'cyEstimatedQ2')
            elem.attrib['cyEstimatedQ3']      = self.get_xml_attrib(entity, 'cyEstimatedQ3')
            elem.attrib['cyEstimatedQ4']      = self.get_xml_attrib(entity, 'cyEstimatedQ4')
            elem.attrib['pyIncomeWages']      = self.get_xml_attrib(entity, 'pyIncomeWages')
            elem.attrib['pyIncomeInterest']   = self.get_xml_attrib(entity, 'pyIncomeInterest')
            elem.attrib['pyIncomeRefund']     = self.get_xml_attrib(entity, 'pyIncomeRefund')
            elem.attrib['pyIncomeDividend']   = self.get_xml_attrib(entity, 'pyIncomeDividend')
            elem.attrib['pyIncomeAlimony']    = self.get_xml_attrib(entity, 'pyIncomeAlimony')
            elem.attrib['pyIncomeBusiness']   = self.get_xml_attrib(entity, 'pyIncomeBusiness')
            elem.attrib['pyIncomeCapitalGL']  = self.get_xml_attrib(entity, 'pyIncomeCapitalGL')
            elem.attrib['pyIncomeTaxableIRA'] = self.get_xml_attrib(entity, 'pyIncomeTaxableIRA')
            elem.attrib['pyIncomeOther']      = self.get_xml_attrib(entity, 'pyIncomeOther')
            elem.attrib['pyIncomeTotal']      = self.get_xml_attrib(entity, 'pyIncomeTotal')

    def get_appointment_from_xml(self):
        entities = self.xml_reader.read_appointments()
        parent = etree.SubElement(self.xml_root, 'Appointments')
        for entity in entities:
            xml_date = self.get_xml_datetime_attrib(entity, 'date')
            # appointment before optionToday will be ignored
            delta_time = self.compare_string_datetime(self.option_today, xml_date)
            if(delta_time > 0):
                continue
            elem = etree.SubElement(parent, 'Appointment')
            elem.attrib['id']            = self.get_xml_attrib(entity, 'id')
            elem.attrib['provider']      = self.get_xml_attrib(entity, 'provider')
            elem.attrib['providerName']  = self.get_xml_attrib(entity, 'providerName')
            elem.attrib['description']   = self.get_xml_attrib(entity, 'description')
            elem.attrib['duration']      = self.get_xml_attrib(entity, 'duration')
            elem.attrib['date']          = xml_date
            elem.attrib['confirmedDate'] = self.get_xml_datetime_attrib(entity, 'confirmedDate')
            elem.attrib['facility']      = self.get_xml_attrib(entity, 'facility')
            elem.attrib['code']          = self.get_xml_attrib(entity, 'code')
            elem.attrib['providerId']    = self.get_xml_attrib(entity, 'providerId')

            self.get_apptcode_from_xml(entity, elem)

    def get_apptcode_from_xml(self, appointment, apptcode_parent):
        #entities = self.xml_reader.read_apptcodes()
        entities = appointment.iter('ApptCode')
        for entity in entities:
            elem = etree.SubElement(apptcode_parent, 'ApptCode')
            elem.attrib['id']           = self.get_xml_attrib(entity, 'id')
            elem.attrib['code']         = self.get_xml_attrib(entity, 'code')
            elem.attrib['description']  = self.get_xml_attrib(entity, 'description')
            elem.attrib['externalCode'] = self.get_xml_attrib(entity, 'externalCode')

    def get_calendarblock_from_xml(self):
        facilities = self.xml_reader.read_facilities()
        parent = etree.SubElement(self.xml_root, 'CalendarBlocks')
        for facility in facilities:
            str_facility = self.get_xml_attrib(facility, 'facility')
            entities = facility.iter('CalendarBlock')
            for entity in entities:
                elem = etree.SubElement(parent, 'CalendarBlock')
                elem.attrib['id']            = self.get_xml_attrib(entity, 'id')
                elem.attrib['scheduledDate'] = self.get_xml_datetime_attrib(entity, 'scheduledDate')
                elem.attrib['title']         = self.get_xml_attrib(entity, 'title')
                elem.attrib['duration']      = self.get_xml_attrib(entity, 'duration')
                elem.attrib['facility']      = str_facility
                elem.attrib['notes']         = self.get_xml_attrib(entity, 'notes')
                self.validate_calendar(elem)

    def get_customer_from_xml(self):
        entities = self.xml_reader.read_customers()
        parent = etree.SubElement(self.xml_root, 'Customers')
        for entity in entities:
            elem = etree.SubElement(parent, 'Customer')
            elem.attrib['id']                      = self.get_xml_attrib(entity, 'id')
            elem.attrib['parentId']                = self.get_xml_attrib(entity, 'parentId')
            elem.attrib['firstVisit']              = self.get_xml_date_attrib(entity, 'firstVisit')
            elem.attrib['lastVisit']               = self.get_xml_date_attrib(entity, 'lastVisit')
            elem.attrib['type']                    = self.get_xml_attrib(entity, 'type')
            elem.attrib['insuranceType']           = self.get_xml_attrib(entity, 'insuranceType')
            elem.attrib['patientType']             = self.get_xml_attrib(entity, 'patientType')
            elem.attrib['lastMaintenanceDate']     = self.get_xml_date_attrib(entity, 'lastMaintenanceDate')
            elem.attrib['maintenanceInterval']     = self.get_xml_int_attrib(entity, 'maintenanceInterval')
            elem.attrib['maintenanceIntervalUnit'] = self.get_xml_attrib(entity, 'maintenanceIntervalUnit')
            elem.attrib['referral']                = self.get_xml_attrib(entity, 'referral')
            elem.attrib['points']                  = self.get_xml_attrib(entity, 'points')

    def get_patientalert_from_xml(self):
        entities = self.xml_reader.read_patientalerts()
        parent = etree.SubElement(self.xml_root, 'PatientAlerts')
        for entity in entities:
            elem = etree.SubElement(parent, 'PatientAlert')
            elem.attrib['id']          = self.get_xml_attrib(entity, 'id')
            elem.attrib['startDate']   = self.get_xml_datetime_attrib(entity, 'startDate')
            elem.attrib['endDate']     = self.get_xml_datetime_attrib(entity, 'endDate')
            elem.attrib['description'] = self.get_xml_attrib(entity, 'description')
            self.validate_patientalert(elem)

    def get_provider_from_xml(self):
        entities = self.xml_reader.read_providers()
        parent = etree.SubElement(self.xml_root, 'Providers')
        for entity in entities:
            elem = etree.SubElement(parent, 'Provider')
            elem.attrib['id']                   = self.get_xml_attrib(entity, 'id')
            elem.attrib['firstName']            = self.get_xml_attrib(entity, 'firstName')
            elem.attrib['middleName']           = self.get_xml_attrib(entity, 'middleName')
            elem.attrib['lastName']             = self.get_xml_attrib(entity, 'lastName')
            elem.attrib['bookingName']          = self.get_xml_attrib(entity, 'bookingName')
            elem.attrib['code']                 = self.get_xml_attrib(entity, 'code')
            elem.attrib['identificationNumber'] = self.get_xml_int_attrib(entity, 'identificationNumber')
            elem.attrib['active']               = self.get_xml_attrib(entity, 'active')
            elem.attrib['type']                 = self.get_xml_attrib(entity, 'type')

    def get_recall_from_xml(self):
        entities = self.xml_reader.read_recalls()
        parent = etree.SubElement(self.xml_root, 'Recalls')
        for entity in entities:
            elem = etree.SubElement(parent, 'Recall')
            elem.attrib['id']       = self.get_xml_attrib(entity, 'id')
            elem.attrib['date']     = self.get_xml_datetime_attrib(entity, 'date')
            elem.attrib['type']     = self.get_xml_attrib(entity, 'type')
            elem.attrib['provider'] = self.get_xml_attrib(entity, 'provider')
            elem.attrib['status']   = self.get_xml_attrib(entity, 'status')

    def get_recommendation_from_xml(self):
        entities = self.xml_reader.read_recommendations()
        parent = etree.SubElement(self.xml_root, 'Recommendations')
        for entity in entities:
            elem = etree.SubElement(parent, 'Recommendation')
            elem.attrib['id']          = self.get_xml_attrib(entity, 'id')
            elem.attrib['date']        = self.get_xml_datetime_attrib(entity, 'date')
            elem.attrib['description'] = self.get_xml_attrib(entity, 'description')
            elem.attrib['type']        = self.get_xml_attrib(entity, 'type')

    def get_vehicle_from_xml(self):
        entities = self.xml_reader.read_vehicles()
        parent = etree.SubElement(self.xml_root, 'Vehicles')
        for entity in entities:
            elem = etree.SubElement(parent, 'Vehicle')
            elem.attrib['id']                 = self.get_xml_attrib(entity, 'id')
            elem.attrib['year']               = self.get_xml_attrib(entity, 'year') +'-01-01'
            elem.attrib['make']               = self.get_xml_attrib(entity, 'make')
            elem.attrib['model']              = self.get_xml_attrib(entity, 'model')
            elem.attrib['driverType']         = self.get_xml_int_attrib(entity, 'driverType')
            elem.attrib['curMilesUpdate']     = self.get_xml_int_attrib(entity, 'curMilesUpdate') # curMilesUpdate
            elem.attrib['curMilesUpdateDate'] = self.get_xml_datetime_attrib(entity, 'curMilesUpdateDate') # curMilesUpdateDate
            elem.attrib['engineType']         = self.get_xml_attrib(entity, 'engineType')
            elem.attrib['vin']                = self.get_xml_attrib(entity, 'vin')
            elem.attrib['odometerDate']       = self.get_xml_datetime_attrib(entity, 'odometerDate')   # curMilesUpdate
            if(elem.attrib['odometerDate'] is ''):
                elem.attrib['odometerDate']   = elem.attrib['curMilesUpdateDate']
            elem.attrib['odometer']           = self.get_xml_int_attrib(entity, 'odometer')    # curMilesUpdateDate
            if(elem.attrib['odometer'] == '0'):
                elem.attrib['odometer']       = elem.attrib['curMilesUpdate']
            elem.attrib['license']            = self.get_xml_attrib(entity, 'license')
            elem.attrib['licenseState']       = self.get_xml_attrib(entity, 'licenseState')

    def get_transaction_from_xml(self):
        entities = self.xml_reader.read_transcations()
        parent = etree.SubElement(self.xml_root, 'Transactions')
        for entity in entities:
            elem = etree.SubElement(parent, 'Transaction')
            elem.attrib['type']         = self.get_xml_attrib(entity, 'type')
            elem.attrib['id']           = self.get_xml_attrib(entity, 'id')
            elem.attrib['date']         = self.get_xml_date_attrib(entity, 'date')
            elem.attrib['charge']       = self.get_xml_attrib(entity, 'charge')
            elem.attrib['provider']     = self.get_xml_attrib(entity, 'provider')
            elem.attrib['providerName'] = self.get_xml_attrib(entity, 'providerName')
            elem.attrib['category']     = self.get_xml_attrib(entity, 'category')
            elem.attrib['SubCategory']  = self.get_xml_attrib(entity, 'SubCategory')
            elem.attrib['code']         = self.get_xml_attrib(entity, 'code')
            elem.attrib['description']  = self.get_xml_attrib(entity, 'description')
            elem.attrib['status']       = self.get_xml_int_attrib(entity, 'status')
            elem.attrib['proivderId']   = self.get_xml_attrib(entity, 'proivderId')
            trans_date = self.get_xml_datetime_attrib(entity, 'date')
            self.validate_transaction(elem, trans_date)

    def get_dental_transaction_from_xml(self):
        entities = self.xml_reader.read_transcations()
        parent = etree.SubElement(self.xml_root, 'DentalTransactions')
        for entity in entities:
            elem = etree.SubElement(parent, 'DentalTransaction')
            elem.attrib['id']           = self.get_xml_attrib(entity, 'id')
            elem.attrib['date']         = self.get_xml_date_attrib(entity, 'date')
            elem.attrib['charge']       = self.get_xml_float_attrib(entity, 'charge', 1)
            elem.attrib['provider']     = self.get_xml_attrib(entity, 'provider')
            elem.attrib['providerName'] = self.get_xml_attrib(entity, 'providerName')
            elem.attrib['type']         = self.get_xml_int_attrib(entity, 'type')
            elem.attrib['category']     = self.get_xml_attrib(entity, 'category')
            elem.attrib['code']         = self.get_xml_attrib(entity, 'code')
            elem.attrib['description']  = self.get_xml_attrib(entity, 'description')
            elem.attrib['status']       = self.get_xml_int_attrib(entity, 'status')
            elem.attrib['procedure']    = self.get_xml_int_attrib(entity, 'procedure')
            elem.attrib['providerId']   = self.get_xml_attrib(entity, 'providerId')
            trans_date = self.get_xml_datetime_attrib(entity, 'date')
            self.validate_transaction(elem, trans_date)

    def get_auto_transaction_from_xml(self):
        entities = self.xml_reader.read_transcations()
        parent = etree.SubElement(self.xml_root, 'AutoTransactions')
        for entity in entities:
            elem = etree.SubElement(parent, 'AutoTransaction')
            elem.attrib['id']           = self.get_xml_attrib(entity, 'id')
            elem.attrib['date']         = self.get_xml_datetime_attrib(entity, 'date')
            elem.attrib['charge']       = self.get_xml_float_attrib(entity, 'charge', 1)
            elem.attrib['provider']     = self.get_xml_attrib(entity, 'provider')
            elem.attrib['providerName'] = self.get_xml_attrib(entity, 'providerName')
            elem.attrib['type']         = self.get_xml_int_attrib(entity, 'type')
            elem.attrib['category']     = self.get_xml_attrib(entity, 'category')
            elem.attrib['code']         = self.get_xml_attrib(entity, 'code')
            elem.attrib['description']  = self.get_xml_attrib(entity, 'description')
            elem.attrib['status']       = self.get_xml_int_attrib(entity, 'status')
            elem.attrib['miles']        = self.get_xml_int_attrib(entity, 'miles')
            elem.attrib['odometer']     = self.get_xml_attrib(entity, 'odometer')
            #If odometer is present then VehicleMileage will be set to odemeter, else if miles are
            #present in the xml then VehicleMileage will be set to miles. If both are not present,then it will be 0
            if(elem.attrib['odometer'] is '' and elem.attrib['miles'] is '0'):
                elem.attrib['odometer'] = 0
                elem.attrib['miles'] = 0
            elif(elem.attrib['odometer'] is ''):
                elem.attrib['odometer'] = elem.attrib['miles']
            trans_date = self.get_xml_datetime_attrib(entity, 'date')
            self.validate_transaction(elem, trans_date)

    def get_xml_attrib(self, entity, name):
        if entity.get(name) is None:
            return ''
        else:
            return entity.get(name).lstrip()

    def get_xml_datetime_attrib(self, entity, name):
        attrib = self.get_xml_attrib(entity, name)
        if attrib is '':
            return ''
        else:
            pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'
            return re.match(pattern, attrib).group().replace('T', ' ').replace('Z', '')

    def get_xml_date_attrib(self, entity, name):
        attrib = self.get_xml_attrib(entity, name)
        if attrib is '':
            return ''
        else:
            pattern = r'\d{4}-\d{2}-\d{2}'
            return re.match(pattern, attrib).group()

    def get_xml_bool_attrib(self, entity, name):
        attrib = self.get_xml_attrib(entity, name)
        return '0' if attrib is not '1' else '1'

    def get_xml_int_attrib(self, entity, name):
        attrib = self.get_xml_attrib(entity, name)
        return attrib if attrib is not '' else '0'

    def get_xml_float_attrib(self, entity, name, decimal_place):
        attrib = self.get_xml_attrib(entity, name)
        return str(round(float(attrib),decimal_place)) if attrib is not '' else '0'

    def string_to_datetime(self, string_date, ignore_time):
        format = '%Y-%m-%d %H:%M:%S'
        new_datetime = datetime.strptime(string_date, format)
        if(ignore_time is True):
            return datetime(new_datetime.year, new_datetime.month, new_datetime.day)
        else:
            return new_datetime

    def datetime_to_string(self, datetime1):
        return datetime1.strftime('%Y-%m-%d %H:%M:%S')

    def compare_string_datetime(self, str_datetime1, str_datetime2):
        datetime1 = time.mktime(time.strptime(str_datetime1,'%Y-%m-%d %H:%M:%S'))
        datetime2 = time.mktime(time.strptime(str_datetime2,'%Y-%m-%d %H:%M:%S'))
        return datetime1 - datetime2

    def validate_calendar(self, elem):
        cal_date = elem.get('scheduledDate')
        option_today_datetime = self.string_to_datetime(self.option_today, True)
        option_today_datetime = option_today_datetime + timedelta(seconds = 1)
        from_date = self.datetime_to_string(option_today_datetime + timedelta(days=-30))
        end_date =  self.datetime_to_string(option_today_datetime + timedelta(days=180))
        from_delta = self.compare_string_datetime(cal_date, from_date)
        end_delta = self.compare_string_datetime(cal_date, end_date)

        if(from_delta < 0 or end_delta > 0):
            elem.attrib['invalid'] = 'true'
            self.print_log('INVALID', 'CalendarBlock invalid as date [%s] is not between [%s] and [%s]'%(cal_date, from_date, end_date))

    def validate_transaction(self, elem, trans_date):
        option_today_datetime = self.string_to_datetime(self.option_today, False)
        from_date = '%s-%s-%s %s:%s:%s'%(option_today_datetime.year-2,option_today_datetime.month,option_today_datetime.day,option_today_datetime.hour,option_today_datetime.minute,option_today_datetime.second)
        from_delta = self.compare_string_datetime(trans_date, from_date)
        if(from_delta < 0):
            elem.attrib['invalid'] = 'true'
            self.print_log('INVALID', 'Transaction invalid as date is too far')

    def validate_patientalert(self, elem):
        id = elem.get('id')
        if(id is '0'):
            elem.attrib['invalid'] = 'true'
            self.print_log('INVALID', 'PatientAlert invalid as id is marked 0')

    def reorder_xml_node(self, parent, attr):
        parent[:] = sorted(parent, key=lambda child: child.get(attr))

    def print_log(self, log_level, log_info):
        print('[%s] %s'%(log_level, log_info))

