from mapper import Mapper
import sys
sys.path.append("..")
from model.address import Address


class AddressMapper(Mapper):

    def __init__(self):
        super(AddressMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><State>{state}</State><City>{city}</City><Street>{street}</Street>" \
                          "<ZipCode>{zip_code}</ZipCode><Country>{country}</Country></record>"

        self.address_list = []


    def map_address(self, customer):
         address_model = Address()

         address_model.id = self.get_item(customer, 'id')
         address_model.state = self.get_item(customer, 'state')
         address_model.street = self.get_item(customer, 'address1')
         address_model.zip_code = self.get_item(customer, 'zip')
         address_model.city = self.get_item(customer, 'city')

         self.address_list.append(address_model.id)

         address_string = self.execute_map(address_model)

         return address_string, address_model

