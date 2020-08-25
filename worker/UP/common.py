
class Scope:
    FULL = 'Full'
    DELTA = 'Delta'
    TRUEDELTA = 'TrueDelta'

class Action:
    INSERT = 'insert'
    UPDATE = 'update'
    DELETE = 'delete'

class Industry:
    DENTAL = 'dental'
    AUTO = 'auto'
    OTHER = 'other'

class Environment:
    STG = 'STG'
    LOCAL = 'LOCAL'

class Constants:
    FILE_DATE_TIME = "%Y-%m-%d-%H-%M-%S"
    COMMON_DATE_FORMAT_T = "%Y-%m-%dT%H:%M:%S"
    COMMON_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    SIMPLE_DATE_FORMAT = "%Y-%m-%d %H:%M"
    YEAR_FORMAT = "%Y"
    DAY_FORMAT = "%Y-%m-%d"
    TIMEZONE_DATE_FORMAT = "%a\r\n    %d %b %Y %H:%M:%S +0000 (%Z)"
    CONVERSION_TIMEZONE_DATE_FORMAT = "%Y-%m-%d %H:%M:%S %Z%z"
    TEMPLATE_TIMEZONE_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.000Z"
    EMAIL_DATE_FORMAT = "%a\r\n    %d %b %Y"
    REMINDER_EMAIL_DATE = "%A\r\n    %B %d\r\n    %Y"
    REMINDER_EMAIL_DATE_TIME = "%I:%M %p"
    VET_RECOMMENDATON_DATE_FORMAT = "%m/%d/%Y"
    REMINDER_VOICE_DATE = "%A %B %#d %#I:%M %p"
    REMINDER_VOICE_DATE_LINUX = "%A %B %-d %-I:%M %p"
    DATE_DAY_OF_WEEK = "%A"
    DATE_DAY_OF_WEEK_BRIEF = "%a"
    DATE_NAME_OF_MONTH = "%B"
    DATE_NAME_OF_MONTH_LOW = "%b"
    DATE_DAY_OF_MONTH = "%#d"
    DATE_DAY_OF_MONTH_LINUX = "%-d"
    
class Entity:
    CALENDARBLOCK = 'CalendarBlock'
    PROVIDER = 'Provider'
    CUSTOMER = 'Customer'
    DEMOGRAPHICS = 'Demographics'
    APPOINTMENT = 'Appointment'
    APPTCODE = 'ApptCode'
    TRANSACTION = 'Transaction'
    PATIENTALERT = 'PatientAlert'
    RECALL = 'Recall'
    EYEWEAR = 'Eyewear'
    DIAGNOSIS = 'Diagnosis'
    ACCOUNT = 'Account'
    CUSTOM = 'Custom'
    TAX = 'Tax'
    MEMBERSHIP = 'Membership'
    VEHICLE = 'Vehicle'
    ANIMAL = 'Animal'
    RECOMMENDATION = 'Recommendation'
