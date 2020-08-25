from d3one import D3One
from mapper import *
from lxml import etree
import datetime
from ingestor_upload import IngestorUpload
from tools import Tools


class Reverter:

    def __init__(self, filename):
        self.filename = r"E:\Git\Python\tools\Reversion\data\dental.xml"
        self.parser = etree.XMLParser()
        self.tree = etree.parse(r"E:\Git\Python\tools\Reversion\data\udbf.xml", parser=self.parser)

        self.patient_mapper = PatientMapper()
        self.email_mapper = EmailMapper()
        self.patient_email_mapper = PatientEmailMapper()
        self.address_mapper = AddressMapper()
        self.resp_mapper = ResponsibleMapper()
        self.pat_resp_mapper = PatientResponsibleMapper()
        self.account_mapper = AccountMapper()
        self.contract_mapper = ContractMapper()
        self.alert_mapper = AlertMapper()
        self.pat_alert_mapper = PatientAlertMapper()
        self.appt_mapper = AppointmentMapper()
        self.staff_mapper = StaffMapper()
        self.procedure_mapper = ProcedureMapper()
        self.appt_proc_mapper = AppointmentProcedureMapper()
        self.ledger_mapper = LedgerMapper()


    def revert(self):
        # parse D3One file
        d3one = D3One(self.filename)

        # revert entities
        self.revert_entities(d3one)

        # username = 'ibexdtx01'
        # password = 'onibex1!'
        # password = '*Fc^Z6).'
        username='dfcxautdd10a5bd@d3one.com'
        password='password'


        upload_file = self.__write_to_file(username)

        # file_name = r'E:\Git\Python\tools\Reversion\data\out\2019-07-01-01-55-55.xml'
        # upload_file = Tools.gzip_file(file_name)

        ##
        IngestorUpload.upload(username, password, upload_file, 'stg')


    def revert_entities(self, d3one):

        section = 'insert'

        customers = d3one.get_customers()
        demographics = d3one.get_demographics()

        for customer_id, customer in customers.items():
            demographic = demographics[customer_id]
            customer_info = dict(customer.items() + demographic.items())

            # map address
            if customer_info.has_key('address1'):
                address_string, address_model = self.address_mapper.map_address(customer_info)
                self.__add_entity_from_string(section, 'Addresses', address_string)
                address_id = address_model.id
            else:
                address_id = ''

            # map patient
            patient_string, patient_model = self.patient_mapper.map_patient(customer_info, address_id, '')
            self.__add_entity_from_string(section, 'Patients', patient_string)

            # map email, patient email link
            if customer_info.has_key('email') and customer_info['email'] not in self.email_mapper.email_list:
                email_string, email_model = self.email_mapper.map_email(customer_info)
                self.__add_entity_from_string(section, 'EMails', email_string)

                pat_email_string, pat_email_model = self.patient_email_mapper.map_paitent_email(patient_model.id, email_model.id)
                self.__add_entity_from_string(section, 'PatientEMailLinks', pat_email_string)

            # map staff, patient staff link
            # if customer_info.has_key('provider') and customer_info['provider'] not in self.staff_mapper.staff_list:
            #     staff_string, staff_model = self.staff_mapper.map_staff(customer_info)
            #     self.__add_entity_from_string(section, 'Staff', staff_string)

            # map responsible
            responsible_id = patient_model.id
            if customer.has_key('parentId') and demographics.has_key(customer['parentId']):
                responsible_id = customer['parentId']
            if responsible_id not in self.resp_mapper.responsible_list:
                resp_string, resp_model = self.resp_mapper.map_responsible(demographics[responsible_id], responsible_id)
                self.__add_entity_from_string(section, 'Responsibles', resp_string)

            # map patient responsible link
            pat_resp_string, pat_resp_model = self.pat_resp_mapper.map_paitent_responsible(patient_model.id, responsible_id)
            self.__add_entity_from_string(section, 'PatientResponsibleLinks', pat_resp_string)

            # map insurance contract
            if customer.has_key('insuranceType') and customer['insuranceType'] not in self.contract_mapper.contract_list:
                contract_string, contract_model = self.contract_mapper.map_contract(customer_info)
                self.__add_entity_from_string(section, 'InsuranceContracts', contract_string)
                contract_id = contract_model.id
            else:
                contract_id = ''

            # map account
            account_string, account_model = self.account_mapper.map_account(pat_resp_model.id, contract_id)
            self.__add_entity_from_string(section, 'Accounts', account_string)

            # map alert, patient alert link
            all_patient_alerts = d3one.get_patient_alerts()
            patient_alerts = [alert for id, alert in all_patient_alerts.items() if alert['customer_id'] == customer_id]
            for alert in patient_alerts:
                alert_string, alert_model = self.alert_mapper.map_alert(alert)
                self.__add_entity_from_string(section, 'Alerts', alert_string)

                pat_alert_string, pat_alert_model = self.pat_alert_mapper.map_paitent_alert(patient_model.id, alert_model.id)
                self.__add_entity_from_string(section, 'PatientAlertLinks', pat_alert_string)

            # map appointment
            all_appointments = d3one.get_appointment()
            appointments = [appt for id, appt in all_appointments.items() if appt['customer_id'] == customer_id]
            for appt in appointments:
                # map staff
                if appt.has_key('provider') and appt['provider'] not in self.staff_mapper.staff_list:
                    staff_string, staff_model = self.staff_mapper.map_staff(appt)
                    self.__add_entity_from_string(section, 'Staff', staff_string)
                    staff_id = staff_model.id
                elif customer_info.has_key('provider'):
                    staff_id = customer_info['provider']
                else:
                    staff_id = ''

                # map appointment
                appt_string, appt_model = self.appt_mapper.map_appointment(appt, patient_model.id, staff_id)
                self.__add_entity_from_string(section, 'Appointments', appt_string)
                appointment_id = appt_model.id

                # map apptcode
                all_appt_codes = d3one.get_appt_code()
                appt_codes = [appt_code for id, appt_code in all_appt_codes.items() if appt_code['appointment_id'] == appointment_id]
                for appt_code in appt_codes:
                    # map procedure
                    if appt_code['id'] not in self.procedure_mapper.procedure_list:
                        proc_string, proc_model = self.procedure_mapper.map_procedure_from_appt_code(appt_code, appointment_id)
                        self.__add_entity_from_string(section, 'Procedures', proc_string)


                    # map appointment procedure
                    appt_proc_string, appt_proc_model = self.appt_proc_mapper.map_appt_proc(appointment_id, appt_code['id'])
                    self.__add_entity_from_string(section, 'AppointmentProcedureLinks', appt_proc_string)

            # map transaction
            all_transactions = d3one.get_transaction()
            transactions = [trans for id, trans in all_transactions.items() if trans['customer_id'] == customer_id]
            for trans in transactions:
                # map staff
                if trans.has_key('provider') and trans['provider'] not in self.staff_mapper.staff_list:
                    staff_string, staff_model = self.staff_mapper.map_staff(trans)
                    self.__add_entity_from_string(section, 'Staff', staff_string)
                    staff_id = staff_model.id
                elif customer_info.has_key('provider'):
                    staff_id = customer_info['provider']
                else:
                    staff_id = ''

                # map procdure
                proc_string, proc_model = self.procedure_mapper.map_procedure_from_transaction(trans)
                self.__add_entity_from_string(section, 'Procedures', proc_string)

                # map ledger
                ledger_string, ledger_model = self.ledger_mapper.map_ledger(trans, account_model.id, staff_id, proc_model.id)
                self.__add_entity_from_string(section, 'Ledgers', ledger_string)

    def __add_entity_from_string(self, section, name, entity_string):
        parent_element = self.tree.find('.//{section}/{name}'.format(section=section, name=name))
        if parent_element == None:
            root_element = self.tree.find('.//{section}'.format(section=section))
            parent_element = etree.fromstring('<{entity}/>'.format(entity=name))
            root_element.append(parent_element)

        entity_element = etree.fromstring(entity_string)

        entity_element.tail = "\n"
        parent_element.append(entity_element)

    def __write_to_file(self, username):
        """ Write to xml/gz file

        :param bool compress:
        :return:
        """
        # file_name = username + '_' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.xml'
        file_name = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.xml'
        output_path = r'E:\Git\Python\tools\Reversion\data\out\{file_name}'.format(file_name=file_name)

        # Write file content
        output = open(output_path, 'wb')
        try:
            output.write(etree.tostring(self.tree))
        finally:
            output.close()

        return Tools.gzip_file(output_path)


if __name__ == '__main__':
    reverter = Reverter("")
    reverter.revert()