
class Responsible(object):

    def __init__(self):
        self.id = ''
        self.first_name = ''
        self.last_name = ''
        self.birth_date = ''
        self.address_id = ''

    def set_gender(self, d3_gender):
        gender_mapping = {'1':'2', '2':'1'}
        if d3_gender != '':
            self.gender = gender_mapping.get(d3_gender)

    def set_birthdate(self, d3_birthday):
        self.birth_date = d3_birthday.split('T')[0]


    def to_dictionary(self):
        responsible_dict = {}

        responsible_dict['id'] = self.id
        responsible_dict['first_name'] = self.first_name
        responsible_dict['last_name'] = self.last_name
        responsible_dict['birth_date'] = self.birth_date
        responsible_dict['address_id'] = self.address_id
        
        return responsible_dict
