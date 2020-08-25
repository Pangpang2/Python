
class Staff(object):

    def __init__(self):
        self.id = ''
        self.first_name = ''
        self.last_name = ''
        self.speciality = ''
        self.gender = ''
        self.license_num = ''
        self.brith_date = ''
        self.email = ''
        self.provider_id = ''
        self.status = ''
        self.code = ''


    def to_dictionary(self):
        staff_dict = {}

        staff_dict['id'] = self.id
        staff_dict['first_name'] = self.first_name
        staff_dict['last_name'] = self.last_name
        staff_dict['speciality'] = self.speciality
        staff_dict['gender'] = self.gender
        staff_dict['license_num'] = self.license_num
        staff_dict['brith_date'] = self.brith_date
        staff_dict['email'] = self.email
        staff_dict['provider_id'] = self.provider_id
        staff_dict['status'] = self.status
        staff_dict['code'] = self.code

        return staff_dict
