
class PatientEmail(object):

    def __init__(self):
        self.id = ''
        self.patient_id = ''
        self.email_id = ''
        self.email_type = ''

    def to_dictionary(self):
        pat_email_dict = {}

        pat_email_dict['id'] = self.id
        pat_email_dict['patient_id'] = self.patient_id
        pat_email_dict['email_id'] = self.email_id
        pat_email_dict['email_type'] = self.email_type

        return pat_email_dict
