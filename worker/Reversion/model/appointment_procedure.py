
class AppointmentProcedure(object):

    def __init__(self):
        self.id = ''
        self.appt_id = ''
        self.proc_id = ''

    def to_dictionary(self):
        appt_proc_dict = {}

        appt_proc_dict['id'] = self.id
        appt_proc_dict['appt_id'] = self.appt_id
        appt_proc_dict['proc_id'] = self.proc_id

        return appt_proc_dict
