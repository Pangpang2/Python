from sqlalchemy import create_engine, text
from sqlalchemy.pool import NullPool
from sqlalchemy.exc import SQLAlchemyError
import sys

class DBClient:
    """ Database agnostic client which can connect to various types of databases, and execute queries using SQL strs.

    db_name = Which database to connect to. Options: keys in vars/db_connection_info.ini (ie. 'd3', 'mcs', 'qaa', ...)
    """

    DB_FILENAME = r'E:\Git\Python\tools\python3\db_connection_info.ini'
    db_client_pool = dict()

    def __init__(self, db_name, env=None):
        """ The value db_name + env need to match values from the db_connection_info.ini and the value
        in the db_connection_info.ini have to be lowercase

        [df_stg] db_name = df and env STG

        [df_dev_ng6] db_name = df and env = DEV_NG6

        :param str db_name: the db_name is the first part used to build a key for the db connection values

            Allowed strings: "dev", "mcs", "qaa", "templateapi"

            The db_name values have to be matched to the correct environment values.
            The db_name "dev" can only be matched to "DEV_NG6", "DEV_NG30", and "STG"
        """

        # try:
        #     ##
        #     print("Setting up db client - "+db_name+" :: " + env)
        #     ##
        #     db_info = self.__get_db_info(db_name, env)
        # except Exception as exception:
        #     print(exception)
        #     exc_msg = "The key '{db_name}' was not a valid database name.".format(db_name=db_name)
        #     raise KeyError(exc_msg)
        # db_type = mysql: //
        # user = sms
        # password = ondemand
        # host = stg - dfcldb1.internetbrands.com
        # port = 3306
        # db_name = cluster

        # db_info = {'db_type': 'mysql://', 'user': 'sms', 'password': 'ondemand',
        #            'host': 'stg - dfcldb1.internetbrands.com',
        #            'port': '3306',
        #            'db_name': 'cluster'}

        db_info = {'db_type': 'postgresql://', 'user': 'ibex_api_user', 'password': 'h0n3YcrEEp3r',
                   'host': 'stg-ibexpgdb1.internetbrands.com',
                   'port': '5432',
                   'db_name': 'ibex'}

        self.db_type = db_info['db_type']
        user = db_info['user']
        password = db_info['password']
        host = db_info['host']
        port = db_info['port']
        self.db_name = db_info['db_name']

        if self.db_type == "postgresql://":
            print("Connected to postgresql")
            self._create_sql_alchemy_connection(host, port, user, password, db_name)

        if self.db_type == "mysql://":
            #print("Connected to mysql")
            self._create_pymql_connection(host, port, user, password, db_name)

        if 'schema' in db_info.keys():
            self.schema = db_info['schema']


    def _create_pymql_connection(self, host, port, user, password, db_name):
        import pymysql
        self.connection = pymysql.connect(host=host,
                                          port=int(port),
                                          user=user,
                                          password=password,
                                          db=db_name,
                                          cursorclass=pymysql.cursors.DictCursor)

    def _create_sql_alchemy_connection(self, host, port, user, password, db_name):
        convert_unicode = True
        sql_debug = False
        self.engine = create_engine(self.db_type + user + ":" + password + "@" + host + ":" + port + "/" + db_name,
                                    convert_unicode=convert_unicode,
                                    echo=sql_debug,
                                    poolclass=NullPool)
        self.connection = self.engine.connect()


    def execute(self, query):
        """Execute the SQL query on the db currently connected to.

        :param str query: SQL query to execute

        :rtype: list<sqlalchemy.engine.ResultProxy> or int
        :return: resultset holding results of executed query
            for SELECT queries = ResultSet if query has results; otherwise None

            for INSERT - MySQL = Primary Key value for created row.

            for INSERT - PostgreSQL - ending in 'RETURNING *' = ResultSet if query has results; otherwise None

            for INSERT - PostgreSQL - not ending in 'RETURNING *' = None

            for UPDATE/DELETE queries = None
        """

        try:
            if self.db_type == "postgresql://":
                # get postgresql result
                if hasattr(self, 'schema'):  # schema needs to be set for some dbs.
                    self.connection.execute('SET search_path TO ' + self.schema)

                query_results = self.connection.execute(text(query).execution_options(autocommit=True))

                if query_results.returns_rows:
                    return query_results.fetchall()

            elif self.db_type == "mysql://":
                with self.connection.cursor() as cursor:
                    cursor.execute(query)
                    if cursor.lastrowid is None:
                        # sql select return
                        return cursor.fetchall()
                    elif cursor.lastrowid == 0 and cursor.rowcount == 1:
                        # delete/update has occurred
                        return None
                    else:
                        # insert return
                        return cursor.lastrowid
            else:
                print("Error running query")
                return None

        except Exception as exception:
            ex_msg = "The query \"{query}\" was not able to be run on db '{db_name}' - Error:{err_msg}"
            ex_msg = ex_msg.format(query=query, db_name=self.db, err_msg=exception)
            print(ex_msg)


def run_query(query, db_name, env=None):
    """Run SQL query on specified db/environment and return results when appropriate.

    :param str query: SQL query to execute
    :param str db_name: Which database to execute on.
    :param str env: Which environment to execute on

        Options are the first part of sections in vars/db_connection_info.ini

        Example: section = df_stg => db_name = df, main.txt.${ENV} = stg)

        Example: section = mcs_dev => db_name = mcs, main.txt.${ENV} = dev)

    :rtype: list<sqlalchemy.engine.ResultProxy> or int
    :return:
        for SELECT queries = ResultSet if query has results; otherwise None

        for INSERT - MySQL = Primary Key value for created row.

        for INSERT - PostgreSQL - ending in 'RETURNING *' = ResultSet if query has results; otherwise None

        for INSERT - PostgreSQL - not ending in 'RETURNING *' = None

        for UPDATE/DELETE queries = None
    """
    try:
        db_client = _get_db_client(db_name, env)
        return db_client.execute(query)
    except (KeyError) as e:
        print("db error")
        print(type(e).__name__ + ": " + e.message)
        return None


def _get_db_client(db_name, env):
    """ return db client with db_name and env combination, create a new db client if it's not already pooled.

    :param db_name:
    :param env:
    :rtype: DBClient
    :return: the db client
    """
    key = db_name + env
    #print(key)
    pool = DBClient.db_client_pool
    if key in pool:
        return pool[key]
    else:
        print(key)
        pool[key] = DBClient(db_name, env)
        return pool[key]

query = """SELECT  emv.id, emv.extractor_module_id,
                em.name || ' - ' ||emv.version as name, 
                emv.released,
                status,
                downgrade,
                array_to_string(array_agg(cl.cl_username), ',') as clients_name
        FROM     ibex.extractor_module AS em 
        JOIN     ibex.extractor_module_version AS emv ON em.id = emv.extractor_module_id
        LEFT JOIN     ibex.extractor_module_client_link AS emc ON emv.id=emc.extractor_module_version_id
        LEFT JOIN     ibex.client AS cl ON emc.client_id=cl.id GROUP BY emv.id, em.name, emv.version, status, downgrade
        
        order by emv.extractor_module_id, emv.id desc"""
results = run_query(query, 'ibex', 'stg')
print(results)
module_list = []
released_list = []
# Filter out old versions
for result in results:
    if result['extractor_module_id'] == 27:
        print('hi')
    if result['released'] == "false":
        module_list.append(result)
    elif result['extractor_module_id'] not in released_list:
        module_list.append(result)
        released_list.append(result['extractor_module_id'])

print(module_list)





