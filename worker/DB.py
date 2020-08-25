import sqlalchemy as db
from sqlalchemy.engine.reflection import Inspector
from enum import Enum
from datetime import datetime


class Tables(object):
    CLIENT = 'client'
    CLIENT_ACCESS= 'client_access'
    CLIENT_FEATURE = 'client_feature'
    CLIENT_CURRENT_DATASET = 'client_current_dataset'
    EXTRACTOR_SETTINGS = 'extractor_settings'
    EXTRACTOR_COMMAND = 'extractor_command'
    EXTRACTOR_ACTIVE_COMMAND = 'extractor_active_command'
    APPOINTMENT_VERSIONED = 'appointment_versioned'
    APPOINTMENT_AMENDED = 'appointment_amended'
    APPOINTMENT_CONFIRMATION_HISTORY = 'appointment_confirmation_history'
    VISITOR_VERSIONED = 'visitor_versioned'
    VISITOR_AMENDED = 'visitor_amended'
    PMS_SOFTWARE = 'pms_software'


class ColType(object):
    TEXT = 'TEXT'
    INTEGER = 'INTEGER'
    BIGINT = 'BIGINT'
    NUMERIC = 'NUMERIC'
    DATE = 'DATE'
    TIMESTAMP_WITHOUT_TIMEZONE = 'TIMESTAMP WITHOUT TIME ZONE'
    BOOLEAN = 'BOOLEAN'


class Processor(object):

    engine = db.create_engine('postgresql://postgres:postgres@10.20.0.121:5433/ibex')
    conn = engine.connect()
    metadata = db.MetaData(schema='ibex')
    tables = engine.table_names(schema='ibex', connection=conn)
    insp = Inspector.from_engine(engine)


    @classmethod
    def generate_for_table(cls, table):
        cls.generate_model(table)
        print('\r\n')
        cls.generate_model_factory(table)
        print('\r\nSQL CLAUSE:')
        cls.generate_insert_sql(table)

    @classmethod
    def generate_model(cls, table):
        census = db.Table(table, Processor.metadata, autoload=True, autoload_with=Processor.engine)
        checks  = cls.translate_check_constraints(table)

        print('class ' + ''.join([l.capitalize() for l in table.split('_')]) + ':')
        print('    def __init__(self):')

        for col in census.columns:
            type = str(col.type)

            if col.name in checks.keys():
                value = checks[col.name][0]
                cls.print_column_with_comment(col.name, "'%s'"%value, '%s ,OPTION:%s '%(type, checks[col.name]))
                continue

            if type == ColType.TEXT:
                value = "''"
            elif type == ColType.INTEGER or type == ColType.BIGINT:
                value = 0
            elif type.__contains__(ColType.NUMERIC):
                value = 0.0
            elif type == ColType.BOOLEAN:
                value = False
            elif type == ColType.DATE:
                value = "'%s'"%datetime.utcnow()
            elif type == ColType.TIMESTAMP_WITHOUT_TIMEZONE:
                value = "'%s'" % datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            else:
                if col.nullable == True and col.primary_key != True:
                    value = "'null'"
                else:
                    value = "''"

            comment = type
            if col.primary_key == True:
                comment = comment + ' ,PRIMARY KEY'
            if col.nullable == True:
                comment = comment + ' ,NULLABLE'
            cls.print_column_with_comment(col.name, value, comment)

    @classmethod
    def generate_model_factory(cls, table):
        census = db.Table(table, Processor.metadata, autoload=True, autoload_with=Processor.engine)

        print('class ' + ''.join([l.capitalize() for l in table.split('_')]) + 'Factory:')
        print('\r')
        print('    @staticmethod')
        print('    def get_default_%s_model():'%table)
        print('        model = %s()'%(''.join([l.capitalize() for l in table.split('_')])))
        print('\r')
        for col in census.columns:

            print('        model.%s = '%(col.name))

        print('\r')
        print('        return model')

    @classmethod
    def translate_check_constraints(cls, table):
        checks = Processor.insp.get_check_constraints(table, schema='ibex')
        checks_dict = {}
        for check in checks:
            key = check['name'].replace('%s_'%table, '').replace('_check', '')
            sqltext = check['sqltext']
            values = sqltext[sqltext.find('[') + 1 : sqltext.find('}') - 1].split(',')
            v_list = []
            for value in values:
                value = value.split('::')[0].strip('\'')
                v_list.append(value)
            checks_dict[key] = v_list
        return checks_dict

    @classmethod
    def print_column_with_comment(cls, col_name, col_value, comment):
        num = 65
        col_assignment = '        self.' + col_name + ' = ' + str(col_value)
        line = col_assignment + ' '*(num -len(col_assignment)) + '# ' +comment
        print(line)


    @classmethod
    def generate_insert_sql(cls, table):
        census = db.Table(table, Processor.metadata, autoload=True, autoload_with=Processor.engine)
        columns = ''
        values = ''
        formats = ''
        for col in census.columns:
            type = str(col.type)
            columns = columns + ',' + col.name
            if type != ColType.INTEGER and type!=ColType.BIGINT and type != ColType.BOOLEAN and not type.__contains__(ColType.NUMERIC):
                values = values + ",'{" +col.name + "}'"
            else:
                values = values + ',{' + col.name + '}'

            if formats == '':
                formats = col.name + '={table}_model.{col}'.format(table=table, col=col.name)
            else:
                formats = formats + ', \r\n' + ' '*len('.format(')+ col.name + '={table}_model.{col}'.format(table=table, col=col.name)

        columns = columns.lstrip(',')
        values = values.lstrip(',')
        sql = '\"INSERT INTO ibex.{table}({columns}) VALUES({values})\".format({formats})'.format(table=table, columns=columns, values=values, formats=formats)
        print(sql)






if __name__ == '__main__':
    tables = ['client','client_access','client_feature','client_current_dataset','extractor_settings','extractor_command','extractor_active_command','appointment_versioned','appointment_amended','appointment_confirmation_history','visitor_versioned','visitor_amended','pms_software']
    for table in tables:
        print("===========================%s===============================" % table)
        Processor.generate_for_table(table)





