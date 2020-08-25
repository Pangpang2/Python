
class Ledger(object):

    def __init__(self):
        self.id = ''
        self.account_id = ''
        self.date = ''
        self.amount = ''
        self.description = ''
        self.type = ''
        self.due = ''
        self.balance = ''
        self.staff_id = ''
        self.category = ''
        self.sub_category = ''
        self.proc_id = ''

    def to_dictionary(self):
        ledger_dict = {}

        ledger_dict['id'] = self.id
        ledger_dict['account_id'] = self.account_id
        ledger_dict['date'] = self.date
        ledger_dict['amount'] = self.amount
        ledger_dict['description'] = self.description
        ledger_dict['type'] = self.type
        ledger_dict['due'] = self.due
        ledger_dict['balance'] = self.balance
        ledger_dict['staff_id'] = self.staff_id
        ledger_dict['category'] = self.category
        ledger_dict['sub_category'] = self.sub_category
        ledger_dict['proc_id'] = self.proc_id

        return ledger_dict
