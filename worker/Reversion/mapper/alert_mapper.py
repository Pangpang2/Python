from mapper import Mapper
import sys
sys.path.append("..")
from model.alert import Alert


class AlertMapper(Mapper):

    def __init__(self):
        super(AlertMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><Description>{description}</Description></record>"

        self.alert_list = []


    def map_alert(self, alert):
         alert_model = Alert()

         alert_model.id = self.get_item(alert, 'id')
         alert_model.description = self.get_item(alert, 'description')

         self.alert_list.append(alert_model.id)

         alert_string = self.execute_map(alert_model)

         return alert_string, alert_model

