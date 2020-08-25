import datetime


class ExtractGenerator:
    def __init__(self):
        pass

    @staticmethod
    def get_default_extract(business_info, scope='full'):
        us_time_now = datetime.datetime.now()
        apptCutOff = us_time_now + datetime.timedelta(days=365)
        return {
            'License': business_info['license'],
            'DFLinkVersion': '1.1.0.0',
            'DFAPI': business_info['api'],
            'DFAPIVersion': '1.2.3.4',
            'Scope': scope,
            'SystemOS': 'Windows 7',
            'DataLocation': 'UPTestDataLocation',
            'SyncClient': 'DFLink 1.0',
            'ManagementSystemName': business_info['pms'],
            'ManagementSystemVersion': business_info['pms_version'],
            'Extract': us_time_now.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'TwoWayApptConfirmEnabled': 'false',
            'ApptCutOff': apptCutOff.strftime('%Y-%m-%dT%H:%M:%S')
        }
