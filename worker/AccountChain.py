import sys
import getopt
from sqlalchemy import create_engine, text


# Reference documents
# http://www.runoob.com/python/python-command-line-arguments.html


def main(argv):
    client_id = ''
    business_id = ''
    user_name = ''

    try:
        opts, args = getopt.getopt(argv, "hc:b:u:")
    except getopt.GetoptError:
        print 'AccountChain.py -c <clientid> -b <businessid> -u <username>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ('AccountChain.py -c <clientid> -b <businessid> -u <username>')
            sys.exit()
        elif opt == '-c':
            client_id = arg
        elif opt == '-b':
            business_id = arg
        elif opt == '-u':
            user_name = arg

    ibex_engine = create_engine('postgresql://ibex_api_user:h0n3YcrEEp3r@stg-ibexpgdb1.internetbrands.com:5432/ibex')
    ibex_conn = ibex_engine.connect()
    ibex_conn.execute('SET search_path TO ibex')
    query = 'SELECT C.ID, CS.USER_NAME,CS.UPLOAD_PASSWORD, CM.EXTERNAL_ID , CM.EXTERNAL_OTHER ' \
            'FROM IBEX.CLIENT C ' \
            'JOIN IBEX.CLIENT_ACCESS CS ON C.CL_USERNAME = CS.USER_NAME ' \
            'JOIN IBEX.CLIENT_MAPPING CM ON C.ID = CM.CLIENT_ID ' \
            'WHERE '
    if client_id:
        query = query + 'C.ID = %s'%client_id
    elif user_name:
        query = query + "CS.USER_NAME = '%s'"%user_name
    elif business_id:
        query = query + 'CM.EXTERNAL_ID = %s'%business_id

    query_results = ibex_conn.execute(text(query).execution_options(autocommit=True))
    if query_results.returns_rows:
        rows = query_results.fetchall()
        if len(rows) > 0:
            print 'ClientID:   ' + str(rows[0]['id'])
            print 'UserName:   ' + str(rows[0]['user_name'])
            print 'Password:   ' + str(rows[0]['upload_password'])
            print 'BusinessID: ' + str(rows[0]['external_id'])
            print 'LicenseKey: ' + str(rows[0]['external_other'])

            business_id = str(rows[0][3])


if __name__ == '__main__':
    main(sys.argv[1:])