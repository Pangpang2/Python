
class Alert(object):

    def __init__(self):
        self.id = ''
        self.description = ''

    def to_dictionary(self):
        alert_dict = {}

        alert_dict['id'] = self.id
        alert_dict['description'] = self.description

        return alert_dict
