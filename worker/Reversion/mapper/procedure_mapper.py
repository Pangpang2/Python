from mapper import Mapper
import sys
sys.path.append("..")
from model.procedure import Procedure


class ProcedureMapper(Mapper):

    def __init__(self):
        super(ProcedureMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><ProcedureCode>{code}</ProcedureCode><Description>{description}</Description>" \
                          "<Duration>{duration}</Duration><Amount>{amount}</Amount></record>"

        self.procedure_list = []


    def map_procedure_from_appt_code(self, appt_code, appt_id):
        proc_model = Procedure()

        proc_model.id = self.get_item(appt_code, 'id')
        proc_model.code = self.get_item(appt_code, 'code')
        proc_model.description = self.get_item(appt_code, 'description')

        proc_model.amount = 0
        proc_model.duration = 30

        self.procedure_list.append(proc_model.id)

        procedure_string = self.execute_map(proc_model)

        return procedure_string, proc_model

    def map_procedure_from_transaction(self, trans):
        proc_model = Procedure()

        proc_model.id = self.get_item(trans, 'id')
        proc_model.code = self.get_item(trans, 'code')
        proc_model.description = self.get_item(trans, 'description')

        self.procedure_list.append(proc_model.id)

        procedure_string = self.execute_map(proc_model)

        return procedure_string, proc_model


