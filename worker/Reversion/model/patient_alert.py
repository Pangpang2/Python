
class PatientAlert(object):

    def __init__(self):
        self.id = ''
        self.patient_id = ''
        self.alert_id = ''

    def to_dictionary(self):
        pat_alert_dict = {}

        pat_alert_dict['id'] = self.id
        pat_alert_dict['patient_id'] = self.patient_id
        pat_alert_dict['alert_id'] = self.alert_id

        return pat_alert_dict
