from lxml import etree
from StringIO import StringIO

class xmlReader(object):

    def __init__(self, file):
        self.tree = etree.parse(file)
        self.root = self.tree.getroot()

    def read_option_today(self):
        return self.root.iter('Extract')

    def read_demandforce_entities(self):
        return self.root.iter('DemandForce')

    def read_dflink_settings_entities(self):
        element = etree.Element('DFLinkSettings')
        for elem in self.root.findall('.//DFLinkSettings/BusinessList/Business'):
            element.attrib['StartTimeFromTask'] = self.read_dflink_settings_entity_text(elem, 'StartTimeFromTask')
            element.attrib['EndTimeFromTask']   = self.read_dflink_settings_entity_text(elem, 'EndTimeFromTask')
            element.attrib['IntervalFromTask']  = self.read_dflink_settings_entity_text(elem, 'IntervalFromTask')
            element.attrib['TwoWayInterval']    = self.read_dflink_settings_entity_text(elem, 'TwoWayInterval')
            element.attrib['DFUpdateInterval']  = self.read_dflink_settings_entity_text(elem, 'DFUpdateInterval')

        for elem in self.root.findall('.//DFLinkSettings/GlobalSettings'):
            element.attrib['LastRunDFUpdate']      = self.read_dflink_settings_entity_text(elem, 'LastRunDFUpdate')
            element.attrib['LastRunHourlySetting'] = self.read_dflink_settings_entity_text(elem, 'LastRunHourlySetting')
            element.attrib['RESTURL']              = self.read_dflink_settings_entity_text(elem, 'RESTURL')
            element.attrib['DeleteXML']            = self.read_dflink_settings_entity_text(elem, 'DeleteXML')
            element.attrib['InstallDir']           = self.read_dflink_settings_entity_text(elem, 'InstallDir')
            element.attrib['URL']                  = self.read_dflink_settings_entity_text(elem, 'URL')
        return element

    def read_dflink_settings_entity_text(self, parent, elem_name):
        if(parent.find(elem_name) is not None):
            return parent.find(elem_name).text
        else:
            return ''

    def read_accounts(self):
        return self.root.iter('Account')

    def read_animals(self):
        return self.root.iter('Animal')

    def read_customs(self):
        return self.root.iter('Custom')

    def read_diagnosis(self):
        return self.root.iter('Diagnosis')

    def read_eyewears(self):
        return self.root.iter('Eyewear')

    def read_memberships(self):
        return self.root.iter('Membership')

    def read_taxes(self):
        return self.root.iter('Tax')

    def read_appointments(self):
        return self.root.iter('Appointment')

    def read_apptcodes(self):
        return self.root.iter('ApptCode')

    def read_facilities(self):
        return self.root.iter('Facility')

    def read_customers(self):
        return self.root.iter('Customer')

    def read_patientalerts(self):
        return self.root.iter('PatientAlert')

    def read_providers(self):
        return self.root.iter('Provider')

    def read_recalls(self):
        return self.root.iter('Recall')

    def read_recommendations(self):
        return self.root.iter('Recommendation')

    def read_vehicles(self):
        return self.root.iter('Vehicle')

    def read_transcations(self):
        return self.root.iter('Transaction')



