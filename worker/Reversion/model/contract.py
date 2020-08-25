
class Contract(object):

    def __init__(self):
        self.id = ''
        self.carrier = ''
        self.iid = ''
        self.plan = ''
        self.plan_type = ''
        self.rank = ''
        self.dental_benefit = ''
        self.dental_used = ''
        self.other_benefit = ''
        self.other_used = ''
        self.benefit_month = ''
        self.employer_id = ''

    def to_dictionary(self):
        contract_dict = {}

        contract_dict['id'] = self.id
        contract_dict['carrier'] = self.carrier
        contract_dict['iid'] = self.iid
        contract_dict['plan'] = self.plan
        contract_dict['plan_type'] = self.plan_type
        contract_dict['rank'] = self.rank
        contract_dict['dental_benefit'] = self.dental_benefit
        contract_dict['dental_used'] = self.dental_used
        contract_dict['other_benefit'] = self.other_benefit
        contract_dict['other_used'] = self.other_used
        contract_dict['benefit_month'] = self.benefit_month
        contract_dict['employer_id'] = self.employer_id

        return contract_dict
