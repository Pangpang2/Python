
class PatientResponsible(object):

    def __init__(self):
        self.id = ''
        self.patient_id = ''
        self.responsible_id = ''

    def to_dictionary(self):
        pat_resp_dict = {}

        pat_resp_dict['id'] = self.id
        pat_resp_dict['patient_id'] = self.patient_id
        pat_resp_dict['responsible_id'] = self.responsible_id

        return pat_resp_dict
