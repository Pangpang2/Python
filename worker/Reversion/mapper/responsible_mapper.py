from mapper import Mapper
import sys
sys.path.append("..")
from model.responsible import Responsible


class ResponsibleMapper(Mapper):

    def __init__(self):
        super(ResponsibleMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><FirstName>{first_name}</FirstName><LastName>{last_name}</LastName>" \
                          "<BirthDate>{birth_date}</BirthDate><AddressID>{address_id}</AddressID></record>"

        self.responsible_list = []


    def map_responsible(self, demographics, resp_id):
        responsible_model = Responsible()
        responsible_model.id = resp_id
        responsible_model.first_name = self.get_item(demographics, 'firstName')
        responsible_model.last_name = self.get_item(demographics, 'lastName')
        responsible_model.set_gender(self.get_item(demographics, 'gender'))
        responsible_model.set_birthdate( self.get_item(demographics, 'birthday'))

        self.responsible_list.append(responsible_model.id)

        responsible_string = self.execute_map(responsible_model)

        return responsible_string, responsible_model

