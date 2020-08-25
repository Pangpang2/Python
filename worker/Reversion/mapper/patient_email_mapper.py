from mapper import Mapper
import sys
sys.path.append("..")
from model.patient_email import PatientEmail


class PatientEmailMapper(Mapper):

    def __init__(self):
        super(PatientEmailMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><PatientID>{patient_id}</PatientID><EMailID>{email_id}</EMailID>" \
                          "<EMailType>{email_type}</EMailType></record>"

        self.pat_email_list = []

    def map_paitent_email(self, patient_id, email_id, email_type=1):
        pat_email_model = PatientEmail()
        pat_email_model.id = patient_id
        pat_email_model.patient_id = patient_id
        pat_email_model.email_id = email_id
        pat_email_model.email_type = email_type

        self.pat_email_list.append(pat_email_model.id)

        pat_email_string = self.execute_map(pat_email_model)

        return pat_email_string, pat_email_model
