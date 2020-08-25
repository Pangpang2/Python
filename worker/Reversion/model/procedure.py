
class Procedure(object):

    def __init__(self):
        self.id = ''
        self.code = ''
        self.description = ''
        self.duration = ''
        self.amount = ''

    def to_dictionary(self):
        proc_dict = {}

        proc_dict['id'] = self.id
        proc_dict['code'] = self.code
        proc_dict['description'] = self.description
        proc_dict['duration'] = self.duration
        proc_dict['amount'] = self.amount

        return proc_dict
