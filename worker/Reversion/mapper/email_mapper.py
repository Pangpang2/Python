from mapper import Mapper
import sys
sys.path.append("..")
from model.email import Email


class EmailMapper(Mapper):

    def __init__(self):
        super(EmailMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><EMail>{email}</EMail><OwnerName>{owner_name}</OwnerName></record>"

        self.email_list = []


    def map_email(self, customer):
         email_model = Email()

         email_model.id = self.get_item(customer, 'email')
         email_model.email = self.get_item(customer, 'email')
         email_model.owner_name = self.get_item(customer, 'firstName') + ' ' + self.get_item(customer, 'lastName')

         self.email_list.append(email_model.id)

         email_string = self.execute_map(email_model)

         return email_string, email_model

