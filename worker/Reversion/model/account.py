
class Account(object):

    def __init__(self):
        self.id = ''
        self.pat_resp = ''
        self.contract_id = ''
        self.current_due = ''
        self.over30 = ''
        self.over60 = ''
        self.over90 = ''
        self.balance = ''
        self.total = ''
        self.next_payment_date = ''
        self.next_payment_amount = ''


    def to_dictionary(self):
        account_dict = {}

        account_dict['id'] = self.id
        account_dict['pat_resp'] = self.pat_resp
        account_dict['contract_id'] = self.contract_id
        account_dict['current_due'] = self.current_due
        account_dict['over30'] = self.over30
        account_dict['over60'] = self.over60
        account_dict['over90'] = self.over90
        account_dict['balance'] = self.balance
        account_dict['total'] = self.total
        account_dict['next_payment_date'] = self.next_payment_date
        account_dict['next_payment_amount'] = self.next_payment_amount

        return account_dict
