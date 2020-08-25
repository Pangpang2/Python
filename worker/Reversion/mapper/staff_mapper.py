from mapper import Mapper
import sys
sys.path.append("..")
from model.staff import Staff


class StaffMapper(Mapper):

    def __init__(self):
        super(StaffMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><FirstName>{first_name}</FirstName><LastName>{last_name}</LastName>" \
                          "<Speciality>{speciality}</Speciality><Gender>{gender}</Gender><LicenseNumber>{license_num}</LicenseNumber>" \
                          "<BirthDate><{brith_date}/BirthDate><EMail>{email}</EMail>" \
                          "<NationalProviderID>{provider_id}</NationalProviderID><StaffStatus>{status}</StaffStatus>" \
                          "<Code>{code}</Code></record>"

        self.staff_list = []


    def map_staff(self, entity):
        staff_model = Staff()
        staff_model.id = self.get_item(entity, 'provider')
        provider_name = self.get_item(entity, 'providerName')
        name_list = provider_name.split(' ')
        staff_model.first_name = name_list[0]
        staff_model.last_name = name_list[1] if len(name_list) > 1  else ''
        staff_model.speciality= 'Dentist'
        staff_model.gender = 0
        staff_model.status = 1
        staff_model.code = self.get_item(entity, 'provider')

        self.staff_list.append(staff_model.id)

        staff_string = self.execute_map(staff_model)

        return staff_string, staff_model

