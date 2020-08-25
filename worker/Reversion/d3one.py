from lxml import etree
from document import Document


class D3One:

    def __init__(self, file_name):
        self.xml_path = "data"
        self.file_name = file_name  #dental.xml

        self.parse_xml(self.file_name)


    def parse_xml(self, file_path):
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(file_path)
        self.document = {}

        customer_id = None

        for element in tree.iter():
            if element.tag in ['DemandForce', 'Business', 'Extract', 'DFLinkSettings',
                               'Param', 'Firmographics', 'Facility']:
                continue

            if element.tag == 'Customer':
                customer_id = element.attrib['id']

            if element.tag == 'Appointment':
                appointment_id = element.attrib['id']

            if element.tag == 'Demographics':
                id = customer_id
            else:
                id = element.attrib['id']

            if not self.document.has_key(element.tag):
                self.document[element.tag] = {}

            self.document[element.tag][id] = element.attrib
            self.document[element.tag][id]['customer_id'] = customer_id

            if element.tag == 'ApptCode':
                self.document[element.tag][id]['appointment_id'] = appointment_id



    def get_demandforce(self):
        if self.document.has_key('DemandForce'):
            return self.document['DemandForce']
        return {}

    def get_customers(self):
        return self.document['Customer']

    def get_demographics(self):
        if self.document.has_key('Demographics'):
            return self.document['Demographics']
        return {}

    def get_patient_alerts(self):
        if self.document.has_key('PatientAlert'):
            return self.document['PatientAlert']
        return {}

    def get_transaction(self):
        if self.document.has_key('Transaction'):
            return self.document['Transaction']
        return {}

    def get_appointment(self):
        if self.document.has_key('Appointment'):
            return self.document['Appointment']
        return {}

    def get_appt_code(self):
        if self.document.has_key('ApptCode'):
            return self.document['ApptCode']
        return {}
