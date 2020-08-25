from mapper import Mapper
import sys
sys.path.append("..")
from model.ledger import Ledger


class LedgerMapper(Mapper):

    def __init__(self):
        super(LedgerMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><AccountID>{account_id}</AccountID>" \
                          "<LedgerDateTime>{date}</LedgerDateTime><Amount>{amount}</Amount>" \
                          "<Description>{description}</Description><LedgerType>{type}</LedgerType><Due>{due}</Due>" \
                          "<Balance>{balance}</Balance><StaffID>{staff_id}</StaffID><Category>{category}</Category>" \
                          "<SubCategory>{sub_category}</SubCategory><ProcedureID>{proc_id}</ProcedureID></record>"

        self.ledger_list = []

    def map_ledger(self, trans, account_id, staff_id, proc_id):
        ledger_model = Ledger()
        ledger_model.id = self.get_item(trans, 'id')
        ledger_model.account_id = account_id
        trans_date = self.get_item(trans, 'date')
        if trans_date:
            date_list = trans_date.split('-')[0:3]
            trans_date = '-'.join(date_list) + '.000'
        ledger_model.date = trans_date
        ledger_model.amount = self.get_item(trans, 'charge')
        ledger_model.description = self.get_item(trans, 'description')
        ledger_model.type = 'C'
        ledger_model.staff_id = staff_id
        ledger_model.category = 'Diagnostic'
        ledger_model.proc_id = proc_id

        self.ledger_list.append(ledger_model.id)

        ledger_string = self.execute_map(ledger_model)
        return ledger_string, ledger_model