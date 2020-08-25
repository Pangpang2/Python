from enum import Enum
from lxml import etree
import os
import shutil
import gzip
import stat
from config import Config


class UDBFEntity(Enum):
    ADDRESSES = 'Addresses'
    PHONES = 'Phones'
    EMAILS = 'EMails'
    PATIENTS = 'Patients'
    PATIENT_PHONE_LINKS = 'PatientPhoneLinks'
    PATIENT_EMAIL_LINKS = 'PatientEMailLinks'
    RESPONSIBLES = 'Responsibles'
    RESPONSIBLE_PHONE_LINKS = 'ResponsiblePhoneLinks'
    RESPONSIBLE_EMAIL_LINKS = 'ResponsibleEMailLinks'
    PATIENT_RESPONSIBLE_LINKS = 'PatientResponsibleLinks'
    OFFICES = 'Offices'
    RECALLS = 'Recalls'
    STAFF = 'Staff'
    PATIENT_STAFF_LINKS = 'PatientStaffLinks'
    REFERRINGS = 'Referrings'
    PATIENT_REFERRING_LINKS = 'PatientReferrignLinks'
    PROCEDURES = 'Procedures'
    TREATMENT_PLANS = 'TreatmentPlans'
    APPOINTMENTS = 'Appointments'
    APPOINTMENT_PROCEDURE_LINKS = 'AppointmentProcedureLinks'
    ACCOUNTS = 'Accounts'
    INSURANCE_CONTRACTS = 'InsuranceContracts'
    LEDGERS = 'Ledgers'
    CALENDAR_BLOCKS = 'CalendarBlocks'
    ALERTS = 'Alerts'
    PATIENT_ALERT_LINKS = 'PatientAlertLinks'

class Reader:

    def __init__(self, file_path):
        self._file_path = file_path
        self.doc = etree.parse(self._file_path)

    def get_utility_by_name(self, utl_names):
        xml_dict = {}
        for utl_name in utl_names:
            base_name = os.path.basename(self._file_path).replace('.xml', '')
            path = os.path.join(Config.get_public_item('output_path'), base_name)
            if not os.path.exists(path):
                os.mkdir(path)
            file_name = os.path.join(path, '{0}_{1}.xml'.format(base_name, str(utl_name)))
            try:
                count = 0
                with open(file_name, 'wt') as f:
                    f.writelines('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r<root>\r')
                    for utility in self.doc.findall('*/{0}'.format(utl_name)):
                        for elem in list(utility):
                            f.writelines(etree.tostring(elem))
                        count += len(utility)
                    f.writelines('</root>')
                xml_dict[file_name] = count
            except etree.XMLSyntaxError:
                pass
        return xml_dict

    def get_records_count(self):
        return len(self.doc.findall('./record'))

