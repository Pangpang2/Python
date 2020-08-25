from mapper import Mapper
import sys
sys.path.append("..")
from model.patient_alert import PatientAlert


class PatientAlertMapper(Mapper):

    def __init__(self):
        super(PatientAlertMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><PatientID>{patient_id}</PatientID><AlertID>{alert_id}</AlertID></record>"

        self.pat_alert_list = []

    def map_paitent_alert(self, patient_id, alert_id):
        pat_alert_model = PatientAlert()
        pat_alert_model.id = patient_id + '_' + alert_id
        pat_alert_model.patient_id = patient_id
        pat_alert_model.alert_id = alert_id

        self.pat_alert_list.append(pat_alert_model.id)

        pat_alert_string = self.execute_map(pat_alert_model)

        return pat_alert_string, pat_alert_model
