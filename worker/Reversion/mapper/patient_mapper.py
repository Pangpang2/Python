from mapper import Mapper
import sys
sys.path.append("..")
from model.patient import Patient

class PatientMapper(Mapper):

    def __init__(self):
        super(PatientMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><FirstName>{first_name}</FirstName><LastName>{last_name}</LastName>" \
                          "<BirthDate>{birth_date}</BirthDate><Status>{status}</Status><AddressID>{address_id}</AddressID>" \
                          "<Gender>{gender}</Gender><LastVisitDate>{last_visit}</LastVisitDate>" \
                          "<LastMaintenanceDate>{last_maintenance}</LastMaintenanceDate>" \
                          "<FirstVisitDate>{first_visit}</FirstVisitDate><StaffID>{staff_id}</StaffID>" \
                          "<OfficeID>{office_id}</OfficeID><ExtensibleNotes>{extensible_notes}</ExtensibleNotes>" \
                          "</record>"

        self.patient_list = []
        self.patient_account_map = {}


    def map_patient(self, customer, address_id, staff_id):
        patient_model = Patient()
        patient_model.id = self.get_item(customer, 'id')
        patient_model.first_name = self.get_item(customer, 'firstName')
        patient_model.last_name = self.get_item(customer, 'lastName')
        patient_model.set_gender(self.get_item(customer, 'gender'))
        patient_model.set_birthdate(self.get_item(customer, 'birthday'))
        patient_model.last_maintenance = self.get_item(customer, 'lastMaintenanceDate')
        patient_model.set_last_visit(self.get_item(customer, 'lastVisit'))
        patient_model.set_first_visit(self.get_item(customer, 'firstVisit'))
        patient_model.status = 'Active'
        patient_model.address_id = address_id
        patient_model.staff_id = staff_id

        self.patient_list.append(patient_model.id)

        patient_string = self.execute_map(patient_model)

        return patient_string, patient_model

    def map_parent_id(self):
        pass

    def map_patient_email_link(self, customer):
        email_id = customer['id']
        email = "<record><ID>{id}</ID><EMail>{email}</EMail><OwnerName>{owner}</OwnerName></record>"\
            .format(id=email_id,
                    email=customer['email'],
                    owner=customer['firstName'] + " " + customer['lastName'])

        link = "<record><ID>{id}</ID><PatientID>{patient_id}</PatientID><EMailID>{email_id}</EMailID><EMailType>1</EMailType></record>"\
            .format(id=email_id,
                    patient_id=customer['id'],
                    email_id=email_id)

        return {'EMails': email, 'PatientEMailLinks': link}

    def map_patient_address(self, customer):
        id = customer['id']
        address = "<record><ID>{id}</ID><State>{state}</State><City>{city}</City><Street>{street}</Street>" \
                  "<ZipCode>{zipcode}</ZipCode><Country>{country}</Country></record>"\
            .format(id=id,
                    state=self.get_dict_item(customer, 'state'),
                    street=self.get_dict_item(customer,'address1'),
                    zipcode=self.get_dict_item(customer, 'zip'),
                    city=self.get_dict_item(customer,'city'),
                    country='')

        customer['AddressID'] = id

        return {'Addresses': address}

    def map_patient_gender(self, customer):
        if customer.has_key('gender'):
            if customer['gender'] == 1:
                customer['gender'] = 2
            elif customer['gender'] == 2:
                customer['gender'] = 1

    def map_patient_insuranceType(self, customer, pat_insurance_type_dict):
        if customer.has_key('insuranceType'):
            pat_insurance_type_dict[customer['id']] = customer['insuranceType']

    def map_patient_account(self, patient_id, responsible_id, responsible):
        responsible_string = "<record><ID>{id}</ID><FirstName>{first_name}</FirstName><LastName>{last_name}</LastName>" \
                      "<BirthDate>{birthday}</BirthDate><AddressID>{address}</AddressID></record>"\
            .format(id=responsible_id,
                    first_name=self.get_dict_item(responsible, 'firstName'),
                    last_name=self.get_dict_item(responsible, 'lastName'),
                    birthday=self.get_dict_item(responsible, 'birthday'),
                    address=self.get_dict_item(responsible, 'address1'))

        link = "<record><ID>{id}</ID><PatientID>{patient_id}</PatientID><ResponsibleID>{responsible_id}</ResponsibleID></record>"\
            .format(id=patient_id + '_' + responsible_id,
                    patient_id=patient_id,
                    responsible_id=responsible_id)

        account_id = patient_id + '_' + responsible_id
        account = "<record><ID>{id}</ID><PatientResponsibleLinkID>{link}</PatientResponsibleLinkID>" \
                  "<InsuranceContractID></InsuranceContractID><CurrentDue>150.12</CurrentDue><Over30>195.84</Over30>" \
                  "<Over60>20.28</Over60><Over90>281.88</Over90><Balance>289.71</Balance><Total>1119.58</Total>" \
                  "<NextPaymentDate></NextPaymentDate><NextPaymentAmount></NextPaymentAmount></record>" \
            .format(id=account_id,
                    link=account_id)

        self.patient_account_map[patient_id] = account_id
        return {"Responsibles": responsible_string, "PatientResponsibleLinks": link, "Accounts": account}
