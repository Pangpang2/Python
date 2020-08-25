#http://blog.csdn.net/lotfee/article/details/57406450
from sqlalchemy import create_engine,Column,text,desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import \
    BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
    DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
    LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
    NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
    TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR


engine = create_engine('mysql://root:ondemand@127.0.0.1:3306/df', echo=False)

#1.Using session
#declare mapping
Base = declarative_base()
class Appointment(Base):
    __tablename__ = 'Appointment'
    id                    = Column(INTEGER(11),primary_key=True)
    businessID            = Column(VARBINARY(255))
    businessAppointmentID = Column(VARBINARY(255))
    provider              = Column(VARBINARY(255))
    providerName          = Column(VARBINARY(255))
    services              = Column(MEDIUMTEXT)
    duration              = Column(INTEGER(11))
    scheduledDate         = Column(DATETIME)
    externalConfirmedTime = Column(DATETIME)
    facility              = Column(VARBINARY(64))
    code                  = Column(VARBINARY(255))
    providerID            = Column(VARBINARY(64))


DBsession = sessionmaker(bind = engine)
session = DBsession()

#Query
appointments = session.query(Appointment).order_by(desc(Appointment.id)).filter(Appointment.id.in_([1,2,3]))

for appt in appointments:
    print(appt.id)
    print(appt.businessAppointmentID)

#Another way
appointments = session.query(Appointment).order_by(desc(Appointment.id)).filter(Appointment.id.in_([1,2,3])).all()   #.first() .last()  .one()

#Add
# new_appt = Appointment(id = 7, businessAppointmentID ='445', provider = 'May', providerName = 'May Li', businessID='130000003')
# session.add(new_appt)
# session.commit()

#Using Sql statement
session.query(Appointment).from_statement(text("Select * from Apppointment"))

#Roll back
session.rollback()

#2.using connection
connection = engine.connect()
query_results = connection.execute(text('Select * from Appointment').execution_options(autocommit=True))

if query_results.returns_rows:
    print(query_results.rowcount > 0 and query_results.fetchall() or None)
elif query_results.lastrowid:
    print(query_results.lastrowid)
else:
    print(None)
