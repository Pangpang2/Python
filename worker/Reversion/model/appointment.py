
class Appointment(object):

    def __init__(self):
        self.id = ''
        self.patient_id = ''
        self.staff_id = ''
        self.office_id = ''
        self.appt_date = ''
        self.duration = ''
        self.amount = ''
        self.status = ''
        self.no_show = ''
        self.created_date = ''
        self.facility = ''
        self.flag = ''
        self.description = ''
        self.confirmed_date = ''


    def set_appt_date(self, d3_appt_date):
        self.appt_date =  '-'.join(d3_appt_date.split('-')[0:3]) + '.000'


    def to_dictionary(self):
        appt_dict = {}

        appt_dict['id'] = self.id
        appt_dict['patient_id'] = self.patient_id
        appt_dict['staff_id'] = self.staff_id
        appt_dict['office_id'] = self.office_id
        appt_dict['appt_date'] = self.appt_date
        appt_dict['duration'] = self.duration
        appt_dict['amount'] = self.amount
        appt_dict['status'] = self.status
        appt_dict['no_show'] = self.no_show
        appt_dict['created_date'] = self.created_date
        appt_dict['facility'] = self.facility
        appt_dict['flag'] = self.flag
        appt_dict['description'] = self.description
        appt_dict['confirmed_date'] = self.confirmed_date

        return appt_dict
