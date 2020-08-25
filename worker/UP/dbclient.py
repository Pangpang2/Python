from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from common import Environment


class DBClient:

    def __init__(self, env=Environment.STG):

        if env == Environment.STG:
            connection_string =  "mysql://sms:ondemand@stg-dfngdb38.internetbrands.com:3306/df"
        if env == Environment.LOCAL:
            connection_string = "mysql://root:ondemand@127.0.0.1:3306/df"

        self.engine = create_engine(connection_string)

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

            query_results = self.connection.execute(text(query).execution_options(autocommit=True))

            # MYSQL/POSTGRESQL: "SELECT ..." - Return rows
            if query_results.returns_rows:
                results = []
                for row in query_results:
                    result = {}
                    for column, value in row.items():
                        result[str(column)] = str(value)
                    results.append(result)
                return results
            # MYSQL - "INSERT ..." - Return last primary key value
            elif query_results.lastrowid:
                return query_results.lastrowid
            else:
                return None
        except Exception as e:
            ex_msg = "The query \"{query}\" was not able to be run on db 'df' - Error:{err_msg}"
            ex_msg = ex_msg.format(query=query, err_msg=e.message)
            raise SQLAlchemyError(ex_msg)

def run_query(query, env=Environment.STG):
    try:
        print(query)
        db_client = DBClient(env=env)
        return db_client.execute(query)
    except (KeyError, SQLAlchemyError) as e:
        print(type(e).__name__ + ": " + e.message)
        return None


# if __name__ == '__main__':
#
#     table_names = run_query("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
#     for table in table_names:
#         query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'{name}'".format(name=table['TABLE_NAME'])
#         print table['TABLE_NAME'] + ":"
#         column_names = run_query(query)
#         for column in column_names:
#              print column['COLUMN_NAME'] + ',    '
#
#         try:
#             query = "select * from {table} where id='3136a847-92e0-4451-ba70-2635c46c41bc'".format(table=table['TABLE_NAME'])
#             results = run_query(query)
#             if len(results) >0:
#                 print 'Find'
#         except:
#             print table['TABLE_NAME'] + 'do not have id'
#             continue
#         print '\r\n'
