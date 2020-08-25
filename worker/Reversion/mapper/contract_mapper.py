from mapper import Mapper
import sys
sys.path.append("..")
from model.contract import Contract


class ContractMapper(Mapper):

    def __init__(self):
        super(ContractMapper, self).__init__()
        self.entity_str = "<record><ID>{id}</ID><Carrier>{carrier}</Carrier><IID>{iid}</IID>" \
                          "<InsurancePlan>{plan}</InsurancePlan><InsurancePlanType>{plan_type}</InsurancePlanType>" \
                          "<Rank>{rank}</Rank><DentalBenefit>{dental_benefit}</DentalBenefit><DentalUsed>{dental_used}</DentalUsed>" \
                          "<OrthoBenefit>{other_benefit}</OrthoBenefit><OrthoUsed>{other_used}</OrthoUsed>" \
                          "<BenefitMonth>{benefit_month}</BenefitMonth><EmployerID>{employer_id}</EmployerID></record>"

        self.contract_list = []
        self.contract_contract_map = {}


    def map_contract(self, customer):
        contract_model = Contract()
        contract_model.id = self.get_item(customer, 'insuranceType')
        contract_model.carrier = self.get_item(customer, 'insuranceType')
        contract_model.plan = self.get_item(customer, 'insuranceType')
        contract_model.plan_type = 0
        contract_model.rank = 2

        self.contract_list.append(contract_model.id)

        contract_string = self.execute_map(contract_model)

        return contract_string, contract_model
