from mapper import Mapper
import sys
sys.path.append("..")
from model.appointment_procedure import AppointmentProcedure


class AppointmentProcedureMapper(Mapper):

    def __init__(self):
        super(AppointmentProcedureMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><AppointmentID>{appt_id}</AppointmentID><ProcedureID>{proc_id}</ProcedureID></record>"

        self.pat_alert_list = []

    def map_appt_proc(self, appt_id, proc_id):
        appt_proc_model = AppointmentProcedure()
        appt_proc_model.id = appt_id + '_' + proc_id
        appt_proc_model.appt_id = appt_id
        appt_proc_model.proc_id = proc_id

        self.pat_alert_list.append(appt_proc_model.id)

        pat_alert_string = self.execute_map(appt_proc_model)

        return pat_alert_string, appt_proc_model
