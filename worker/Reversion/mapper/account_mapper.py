from mapper import Mapper
import sys
sys.path.append("..")
from model.account import Account


class AccountMapper(Mapper):

    def __init__(self):
        super(AccountMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><PatientResponsibleLinkID>{pat_resp}</PatientResponsibleLinkID>" \
                          "<InsuranceContractID>{contract_id}</InsuranceContractID><CurrentDue>{current_due}</CurrentDue><" \
                          "Over30>{over30}</Over30><Over60>{over60}</Over60><Over90>{over90}</Over90>" \
                          "<Balance>{balance}</Balance><Total>{total}</Total>" \
                          "<NextPaymentDate>{next_payment_date}</NextPaymentDate>" \
                          "<NextPaymentAmount>{next_payment_amount}</NextPaymentAmount>" \
                          "</record>"

        self.account_list = []
        self.account_account_map = {}


    def map_account(self, pat_resp_id, contract_id):
        account_model = Account()
        account_model.id = pat_resp_id
        account_model.pat_resp = pat_resp_id
        account_model.contract_id = contract_id
        account_model.current_due = 300.01
        account_model.over30 = 50.1
        account_model.over60 = 100.01
        account_model.over90 = 150.01
        account_model.balance = 200.01
        account_model.total = 1240.01

        self.account_list.append(account_model.id)

        account_string = self.execute_map(account_model)

        return account_string, account_model

    def map_parent_id(self):
        pass

    def map_account_email_link(self, customer):
        email_id = customer['id']
        email = "<record><ID>{id}</ID><EMail>{email}</EMail><OwnerName>{owner}</OwnerName></record>"\
            .format(id=email_id,
                    email=customer['email'],
                    owner=customer['firstName'] + " " + customer['lastName'])

        link = "<record><ID>{id}</ID><AccountID>{account_id}</AccountID><EMailID>{email_id}</EMailID><EMailType>1</EMailType></record>"\
            .format(id=email_id,
                    account_id=customer['id'],
                    email_id=email_id)

        return {'EMails': email, 'AccountEMailLinks': link}

    def map_account_address(self, customer):
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

    def map_account_gender(self, customer):
        if customer.has_key('gender'):
            if customer['gender'] == 1:
                customer['gender'] = 2
            elif customer['gender'] == 2:
                customer['gender'] = 1

    def map_account_insuranceType(self, customer, pat_insurance_type_dict):
        if customer.has_key('insuranceType'):
            pat_insurance_type_dict[customer['id']] = customer['insuranceType']

    def map_account_account(self, account_id, responsible_id, responsible):
        responsible_string = "<record><ID>{id}</ID><FirstName>{first_name}</FirstName><LastName>{last_name}</LastName>" \
                      "<BirthDate>{birthday}</BirthDate><AddressID>{address}</AddressID></record>"\
            .format(id=responsible_id,
                    first_name=self.get_dict_item(responsible, 'firstName'),
                    last_name=self.get_dict_item(responsible, 'lastName'),
                    birthday=self.get_dict_item(responsible, 'birthday'),
                    address=self.get_dict_item(responsible, 'address1'))

        link = "<record><ID>{id}</ID><AccountID>{account_id}</AccountID><ResponsibleID>{responsible_id}</ResponsibleID></record>"\
            .format(id=account_id + '_' + responsible_id,
                    account_id=account_id,
                    responsible_id=responsible_id)

        account_id = account_id + '_' + responsible_id
        account = "<record><ID>{id}</ID><AccountResponsibleLinkID>{link}</AccountResponsibleLinkID>" \
                  "<InsuranceContractID></InsuranceContractID><CurrentDue>150.12</CurrentDue><Over30>195.84</Over30>" \
                  "<Over60>20.28</Over60><Over90>281.88</Over90><Balance>289.71</Balance><Total>1119.58</Total>" \
                  "<NextPaymentDate></NextPaymentDate><NextPaymentAmount></NextPaymentAmount></record>" \
            .format(id=account_id,
                    link=account_id)

        self.account_account_map[account_id] = account_id
        return {"Responsibles": responsible_string, "AccountResponsibleLinks": link, "Accounts": account}
