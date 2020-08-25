
class Email(object):

    def __init__(self):
        self.id = ''
        self.email = ''
        self.owner_name = ''

    def to_dictionary(self):
        email_dict = {}

        email_dict['id'] = self.id
        email_dict['email'] = self.email
        email_dict['owner_name'] = self.owner_name

        return email_dict
