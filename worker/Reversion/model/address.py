
class Address(object):

    def __init__(self):
        self.id = ''
        self.state = ''
        self.city = ''
        self.street = ''
        self.zip_code = ''
        self.country = ''

    def to_dictionary(self):
        address_dict = {}

        address_dict['id'] = self.id
        address_dict['state'] = self.state
        address_dict['city'] = self.city
        address_dict['street'] = self.street
        address_dict['zip_code'] = self.zip_code
        address_dict['country'] = self.country

        return address_dict
