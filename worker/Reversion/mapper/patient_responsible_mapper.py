from mapper import Mapper
import sys
sys.path.append("..")
from model.patient_responible import PatientResponsible


class PatientResponsibleMapper(Mapper):

    def __init__(self):
        super(PatientResponsibleMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><PatientID>{patient_id}</PatientID><ResponsibleID>{responsible_id}</ResponsibleID></record>"

        self.pat_responsible_list = []

    def map_paitent_responsible(self, patient_id, responsible_id):
        pat_resp_model = PatientResponsible()
        pat_resp_model.id = patient_id + '_' + responsible_id
        pat_resp_model.patient_id = patient_id
        pat_resp_model.responsible_id = responsible_id

        self.pat_responsible_list.append(pat_resp_model.id)

        pat_responsible_string = self.execute_map(pat_resp_model)

        return pat_responsible_string, pat_resp_model
