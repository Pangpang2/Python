from mapper import Mapper
import sys
sys.path.append("..")
from model.appointment import Appointment


class AppointmentMapper(Mapper):

    def __init__(self):
        super(AppointmentMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><PatientID>{patient_id}</PatientID><StaffID>{staff_id}</StaffID>" \
                            "<OfficeID>{office_id}</OfficeID><AppointmentDateTime>{appt_date}</AppointmentDateTime>" \
                            "<Duration>{duration}</Duration><Amount>{amount}</Amount><Status>{status}</Status>" \
                            "<Noshow>{no_show}</Noshow><CreatedDate>{created_date}</CreatedDate><Facility>{facility}</Facility>" \
                            "<Flag>{flag}</Flag><Description>{description}</Description>" \
                            "<ConfirmedDate>{confirmed_date}</ConfirmedDate>" \
                            "</record>"

        self.appt_list = []

    def map_appointment(self, appt, patient_id, staff_id):
        appt_model = Appointment()
        appt_model.id = self.get_item(appt, 'id')
        appt_model.patient_id = patient_id
        appt_model.staff_id = staff_id
        appt_model.office_id = 'FAKE_OFFICE'
        appt_date = self.get_item(appt, 'date')
        if appt_date:
            date_list = appt_date.split('-')[0:3]
            appt_date = '-'.join(date_list) + '.000'
        appt_model.appt_date = appt_date
        appt_model.duration = self.get_item(appt, 'duration')
        appt_model.status = 'new'
        appt_model.no_show = 0
        appt_model.flag = 0
        appt_model.description = self.get_item(appt, 'description')

        self.appt_list.append(appt_model.id)

        appt_string = self.execute_map(appt_model)

        return appt_string, appt_model
