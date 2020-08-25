
import datetime


class EntityGenerator:
    def __init__(self):
        pass

    @staticmethod
    def get_default_account(account_id):
        return {
            'ManagementSystemID': account_id,
            'Integer1': 0,  # overdueBalance
            'Integer2': 0,  # openBalance
            'Integer3': 0,  # totalRevenue
            'Deleted': 0
        }

    @staticmethod
    def get_default_animal(animal_id):
        today =  datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-8)))
        birthday = datetime.datetime.combine(today.date(), datetime.time(0, 0, 0)) + datetime.timedelta(weeks=-96)
        return {
            'ManagementSystemID': animal_id,
            'Deleted': 0,
            'String1': 'UPTestPet',  # name
            'String2': 'Avian',  # species
            'String3': 'African Grey Parrot',  # breed
            'String4': 'Blue and Gold',  # coatColor
            'String9': 'F',  # sex
            'String5': '',  # provider
            'String6': '',  # providerName
            'Anniversary': birthday.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'FirstVisit': '',
            'LastVisit': '',
            'Double1': 2,  # weight
            'String7': 'lbs',  # weightUnits
        }

    @staticmethod
    def get_default_diagnosis(diagnosis_id):
        return {
            'ManagementSystemID': diagnosis_id,
            'Deleted': 0,
            'Date1': '',  # date
            'String1': 'UPTestPet',  # internalCode
            'String2': 'Avian',  # externalCode
            'String4': 'Blue and Gold',  # description
            'String3': 'African Grey Parrot',  # category
            'Boolean1': 0,  # dismissed
        }

    @staticmethod
    def get_default_membership(membership_id):
        return {
            'ManagementSystemID': membership_id,
            'Deleted': 0,
            'Boolean1': 1, # member
            'Date1': '2011-01-11T00:00:00-08:00', # startDate
            'Date2': '2021-12-30T00:00:00-08:00', # expirationDate
            'String2': '', # cancelReason
            'String1': 'sliver card' # memberType
        }

    @staticmethod
    def get_default_eyewear(eyewear_id):
        return {
            'ManagementSystemID': eyewear_id,
            'Deleted': 0,
            'String1': '',  # type
            'Boolean1': True,  # received
            # 'Date1': '',  # receivedDate
            'Boolean2': False,  # dispensed
            # 'Date2': '',  # dispensedDate
        }

    @staticmethod
    def get_default_custom(custom_id):
        return {
            'ManagementSystemID': custom_id,
            'Deleted': 0,
            'String1': 'UPCustomName',  # name
            'String2': 'UPCustomValue'  # value
        }

    @staticmethod
    def get_default_tax(tax_id):
        return {
            'ManagementSystemID': tax_id,
            'Deleted': 0,
            'String1': 'UPTaxFilingStatus',  # pyFilingStatus
            'Integer1': 0,  # cyEstimatedQ1
            'Integer2': 0,  # cyEstimatedQ2
            'Integer3': 0,  # cyEstimatedQ3
            'Integer4': 0,  # cyEstimatedQ4
            'Integer5': 0,  # pyIncomeWages
            'Integer6': 0,  # pyIncomeInterest
            'Integer7': 0,  # pyIncomeRefund
            'Integer8': 0,  # pyIncomeDividend
            'Integer9': 0,  # pyIncomeAlimony
            'Integer10': 0,  # pyIncomeBusiness
            'Integer11': 0,  # pyIncomeCapitalGL
            'Integer12': 0,  # pyIncomeTaxableIRA
            'Integer13': 0,  # pyIncomeOther
            'Integer14': 0,  # pyIncomeTotal
        }
