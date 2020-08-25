
class Patient(object):

    def __init__(self):
        self.id = ''
        self.first_name = ''
        self.last_name = ''
        self.birth_date = ''
        self.status = ''
        self.address_id = ''
        self.gender = ''
        self.last_visit = ''
        self.last_maintenance = ''
        self.first_visit = ''
        self.staff_id = ''
        self.office_id = ''
        self.extensible_notes = ''


    def set_gender(self, d3_gender):
        gender_mapping = {'1':'2', '2':'1'}
        if d3_gender != '':
            self.gender = gender_mapping.get(d3_gender)

    def set_birthdate(self, d3_birthday):
        self.birth_date = d3_birthday.split('T')[0]

    def set_last_visit(self, d3_last_visit):
        self.last_visit = d3_last_visit.split('T')[0]

    def set_first_visit(self, d3_first_visit):
        self.first_visit = d3_first_visit.split('T')[0]

    def to_dictionary(self):
        patient_dict = {}

        patient_dict['id'] = self.id
        patient_dict['first_name'] = self.first_name
        patient_dict['last_name'] = self.last_name
        patient_dict['birth_date'] = self.birth_date
        patient_dict['status'] = self.status
        patient_dict['address_id'] = self.address_id
        patient_dict['gender'] = self.gender
        patient_dict['last_visit'] = self.last_visit
        patient_dict['last_maintenance'] = self.last_maintenance
        patient_dict['first_visit'] = self.first_visit
        patient_dict['staff_id'] = self.staff_id
        patient_dict['office_id'] = self.office_id
        patient_dict['extensible_notes'] = self.extensible_notes

        return patient_dict
