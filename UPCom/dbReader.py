from sqlalchemy import Column,create_engine
from sqlalchemy.orm import sessionmaker

class dbReader(object):
    def __init__(self, business_id):
        self.engine = create_engine('mysql://root:ondemand@127.0.0.1:3306/df')
        self.DBsession = sessionmaker(bind = self.engine)
        self.session = self.DBsession()
        self.business_id = business_id

    #DenandForce Entities
    def query_demandforce_entities(self):
        demandforce_entities = self.session.execute('\
            SELECT BusinessID, \
                   SystemOS ,\
                   SystemName,\
                   SystemUser,\
                   SystemIPAddress,\
                   AntivirusSystemName,\
                   DotNETFrameworkVersion,\
                   MACAddress\
            FROM BusinessSystem\
            WHERE BusinessID={0}'.format(self.business_id))
        return demandforce_entities

    #DFLinkSetting entities
    def query_dflink_settings_entities(self):
        dflink_setting_entities = self.session.execute('\
            SELECT BI.BusinessID,\
                   UH.LogDate,\
                   BI.StartTimeFromTask,\
                   BI.EndTimeFromTask,\
                   BI.IntervalFromTask,\
                   BI.TwoWayInterval,\
                   BI.DFUpdateInterval,\
                   UH.LastRunDFUpdate,\
                   UH.LastRunHourlySetting,\
                   BD.RestUrl,\
                   BD.DeleteXML,\
                   BD.InstallDir,\
                   BD.URL\
            FROM   BusinessInterval AS BI,\
                   UploadHistory AS UH,\
                   (SELECT RU.BusinessID,RestUrl,DeleteXML,InstallDir,UR.URL\
                  FROM (SELECT BusinessID , VALUE AS RestUrl\
                       FROM BusinessDFLinkProperties\
                      WHERE property = "RESTURL") AS RU,\
                    (SELECT BusinessID , VALUE AS DeleteXML\
                       FROM BusinessDFLinkProperties\
                      WHERE property = "DeleteXML") AS DX,\
                    (SELECT BusinessID , VALUE AS InstallDir\
                       FROM BusinessDFLinkProperties\
                      WHERE property = "InstallDir") AS ID,\
                    (SELECT BusinessID , VALUE AS URL\
                       FROM BusinessDFLinkProperties\
                      WHERE property = "URL") AS UR\
                 WHERE RU.BusinessID= DX.BusinessID AND \
                           RU.BusinessID = ID.BusinessID AND\
                           RU.BusinessID = UR.BusinessID) AS BD\
            WHERE BI.BusinessID = UH.BusinessID AND\
                  BI.BusinessID = BD.BusinessID AND\
                  BI.BusinessID = {0} \
            ORDER BY UH.LogDate DESC \
            LIMIT 1'.format(self.business_id))

        return dflink_setting_entities

    #Account -id,overdueBalance,openBalance,totalRevenue
    def query_accounts(self):
        accounts = self.session.execute('\
            SELECT ManagementSystemID,\
                   Integer1,\
                   Integer2,\
                   Integer3,\
                   Status \
            FROM Entity \
            WHERE TYPE = "4" AND BusinessID={0}'.format(self.business_id))
        return accounts

    #Animal
    def query_animals(self):
        animals = self.session.execute('\
            SELECT ManagementSystemID,\
                   String1,\
                   String2,\
                   String3,\
                   String4,\
                   String9,\
                   String5,\
                   String6,\
                   Anniversary,\
                   FirstVisit,\
                   LastVisit,\
                   Double1,\
                   String7,\
                   Status \
            FROM Entity \
            WHERE TYPE = "1" AND BusinessID={0}'.format(self.business_id))
        return animals

    #Custom -- ID, name, value
    def query_customs(self):
        customs = self.session.execute('\
            SELECT ManagementSystemID,\
                   String1,\
                   String2,\
                   Status \
            FROM Entity \
            WHERE TYPE = "5" AND BusinessID={0}'.format(self.business_id))
        return customs

    #Diagnosis
    def query_diagnosis(self):
        diagnosis = self.session.execute('\
            SELECT ManagementSystemID,\
                   Date1,\
                   String1,\
                   String2,\
                   String4,\
                   String3,\
                   Boolean1,\
                   Status \
            FROM Entity \
            WHERE TYPE = "3" AND BusinessID={0}'.format(self.business_id))
        return diagnosis

    #Eyewear
    def query_eyewears(self):
        eyewears = self.session.execute('\
            SELECT  ManagementSystemID,\
                    Boolean2,\
                    String1,\
                    Date2,\
                    Boolean1,\
                    Date1,\
                    Status \
            FROM Entity \
            WHERE TYPE = "2" AND BusinessID={0}'.format(self.business_id))
        return eyewears

    #Membership
    def query_memberships(self):
        memberships = self.session.execute('\
            SELECT ManagementSystemID,\
                   Boolean1,\
                   Date1,\
                   Date2,\
                   String2,\
                   String1, \
                   Status \
            FROM Entity \
            WHERE TYPE = "7" AND BusinessID={0}'.format(self.business_id))
        return memberships

    #Tax
    def query_taxes(self):
        taxes = self.session.execute('\
            SELECT ManagementSystemID,\
                   Status,\
                   String1,\
                   Integer1,\
                   Integer2,\
                   Integer3,\
                   Integer4,\
                   Integer5,\
                   Integer6,\
                   Integer7,\
                   Integer8,\
                   Integer9,\
                   Integer10,\
                   Integer11,\
                   Integer12,\
                   Integer13,\
                   Integer14,\
                   Status \
            FROM Entity \
            WHERE TYPE = "6" AND BusinessID={0}'.format(self.business_id))
        return taxes

    #Appointment
    def query_appointments(self):
        appointments = self.session.execute('\
            SELECT BusinessAppointmentID,\
                   Provider,\
                   ProviderName,\
                   Services,\
                   Duration,\
                   ScheduledDate,\
                   ExternalConfirmedTime,\
                   Facility,\
                   code,\
                   ProviderID, \
                   ID,\
                   Status \
            FROM Appointment \
            WHERE BusinessID={0}'.format(self.business_id))
        return appointments

    #ApptCode
    def query_apptcodes(self, appt_code):
        appt_codes = self.session.execute('\
            SELECT BusinessApptCodeID,\
                   CODE,\
                   Description,\
                   ExternalCode,\
                   ApptCodeStatus \
            FROM ApptCode \
            WHERE BusinessID={0}\
            AND AppointmentID={1}\
            ORDER BY ID DESC'.format(self.business_id, appt_code))
        return appt_codes

    #CalendarBlock (optionToday -31/+ 181)
    def query_calendarblocks (self):
        calendarblocks = self.session.execute('\
            SELECT BusinessBlockID,\
                   ScheduledDate,\
                   Title,\
                   Duration,\
                   Facility,\
                   Notes,\
                   Status \
            FROM CalendarBlock \
            WHERE BusinessID={0}'.format(self.business_id))
        return calendarblocks

    #Customer
    def query_customers(self):
        customers = self.session.execute('\
            SELECT C.BusinessCustomerId,\
                   C.HoHID,\
                   C.FirstVisit,\
                   C.LastVisit,\
                   C.Type,\
                   C.Insurance,\
                   C.PatientType,\
                   C.LastMaintenance,\
                   C.OptedIn,\
                   C.MaintenanceInterval,\
                   C.MaintenanceIntervalUnit,\
                   C.Referral,\
                   CP.Points,\
                   C.Status \
            FROM Customer AS C LEFT JOIN CustomerPoints AS CP ON C.ID = CP.CustomerID  \
            WHERE C.BusinessID={0}'.format(self.business_id))
        return customers

    #PatientAlert
    def query_patientalerts(self):
        patient_alerts = self.session.execute('\
            SELECT PatientAlertID,\
                   StartDate,\
                   EndDate,\
                   Description,\
                   Status \
            FROM PatientAlert \
            WHERE BusinessID={0}'.format(self.business_id))
        return patient_alerts

    #Provider
    def query_providers(self):
        providers = self.session.execute('\
            SELECT BusinessProviderID,\
                   FirstName,\
                   MiddleName,\
                   LastName,\
                   BookingName,\
                   CODE,\
                   IdentificationNumber,\
                   Active,\
                   Type,\
                   Status \
            FROM Provider \
            WHERE BusinessID={0}'.format(self.business_id))
        return providers

    #Recall
    def query_recalls(self):
        recalls = self.session.execute('\
            SELECT RecallStatus,\
                   BusinessRecallDueDateID,\
                   date,\
                   type,\
                   provider,\
                   status,\
                   RecallStatus \
            FROM RecallDueDate \
            WHERE BusinessID={0}'.format(self.business_id))
        return recalls

    #Recommendation
    def query_recommendations(self):
        recommendations = self.session.execute('\
            SELECT BusinessRecommendationID,\
                   Date,\
                   Description,\
                   Type,\
                   Status \
            FROM Recommendation \
            WHERE BusinessID={0}'.format(self.business_id))
        return recommendations

    #Vehicle
    def query_vehicles(self):
        vehicles = self.session.execute('\
            SELECT ShopVehicleID,\
                   ModelYear,\
                   Make,\
                   Model,\
                   DriverType,\
                   MilesAtUpdate,\
                   LastMileageDate,\
                   EngineType,\
                   VIN,\
                   LastMileageDate,\
                   MilesAtUpdate,\
                   License,\
                   LicenseState,\
                   Status \
            FROM Vehicle \
            WHERE BusinessId={0}'.format(self.business_id))
        return vehicles

    #Transaction(Visit)
    def query_transactions(self):
        transactions = self.session.execute('\
            SELECT Type,\
                   ExternalVisitID,\
                   VisitDate,\
                   Revenue,\
                   Provider,\
                   ProviderName,\
                   Category,\
                   Subcategory,\
                   Subcategory,\
                   CustomField2,\
                   ServiceDescription,\
                   VisitStatus,\
                   ProviderID \
            FROM Visit \
            WHERE BusinessID={0}'.format(self.business_id))
        return transactions

    #Transaction(AutoVisit)
    def query_auto_transactions(self):
        auto_transactions = self.session.execute('\
            SELECT RepairID,\
                   RepairDate,\
                   RepairAmount,\
                   Provider,\
                   ProviderName,\
                   Type,\
                   Category,\
                   ServiceCode,\
                   RepairDescription,\
                   NoticeType,\
                   VehicleMileage \
            FROM AutoVisit \
            WHERE BusinessID={0}'.format(self.business_id))
        return auto_transactions

    #Transaction(DentalVisit)
    def query_dental_transactions(self):
        dental_transactions = self.session.execute('\
            SELECT PracticeVisitID,\
                   VisitDate,\
                   Revenue,\
                   Provider,\
                   ProviderName,\
                   Type,\
                   Category,\
                   CustomField1,\
                   Procedures,\
                   VisitStatus,\
                   ProviderID,\
                   FamilyMemberID,\
                   ProviderID \
            FROM DentalVisit \
            WHERE BusinessID={0}'.format(self.business_id))
        return dental_transactions


    def query_industry_from_db(self):
        industry = self.session.execute('\
          SELECT Industry \
          FROM Business \
          WHERE ID = {0}'.format(self.business_id))
        return industry
