class CustomerGenerator:
    def __init__(self):
        pass

    @staticmethod
    def get_default_customer(customer_id, provider=''):
        data = CustomerGenerator.__get_base_customer(customer_id)
        data.update({
            'Provider': provider
        })
        return data

    @staticmethod
    def get_new_patient(customer_id, provider):
        data = CustomerGenerator.get_default_customer(customer_id, provider)
        data.update({
            'Birthday': '',
            'Type': '',
            'Insurance': ''
        })
        return data

    @staticmethod
    def __get_base_customer(customer_id):
        return {
            'BusinessCustomerID': customer_id,
            'ParentId': customer_id,
            'ChartId': '',
            'Type': '8',
            'Status': 2,
            'Insurance': 'UPTestInsuranceType',
            'InsuranceClass': 'UPTestInsuranceClass',
            'FirstName': 'UPTestFName' + customer_id,
            'LastName': 'UPTestLName' + customer_id,
            'Birthday': '1990-01-01T00:00:00Z',
            'Address1': '600 Harrison Street, 6th Floor',
            'City': 'San Francisco',
            'State': 'CA',
            'ZipCode': '94107',
            'HomePhone': '4152340952',
            'WorkPhone': '',
            'CellPhone': '4083485246',
            'OtherPhone1': '',
            'OtherPhone2': '',
            'Email': 'uptest@d3one.com',
            'NoCorrespondence': 1,
            'FirstApptId': '',
            'FirstVisit': ''
        }
