import imaplib
import re

class GmailClient(object):

    EMAIL_ADDRESS = "dfqa@d3one.com"
    EMAIL_USER = "dfqa1"
    EMAIL_PASSWORD = "H*H1jD4G8"

    SMTP_SERVER = "imap.gmail.com"


    def get_gmail_instance(self):
        count = 0
        max_try = 5
        for i in range(max_try):
            try:
                self.mailbox = imaplib.IMAP4_SSL(self.SMTP_SERVER)
                r, data = self.mailbox.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
                if r == "OK":
                    print("Congrats, you have connected to the gmail server successfully")
                    break
            except Exception as e:
                print("Did not connect to gmail successfully, error number is: " + str(e))
                count += 1
                print(("you can try", max_try - 1 - i, "times"))

        if count == max_try:
            raise Exception("Unable to start IMAP server even after reaching the max try times with " + str(max_try))

    def find_email_by_criteria(self):
        self.mailbox.select(readonly=True, mailbox='Inbox')
        # subject = r"You've Been Invited to PQAAc17045f6'? Patient Portal!"
        # print(subject)
        # updated_criteria_string = '(SUBJECT "{subject}")'.format(subject=subject)
        subject = "You've Been Invited to {business_name}'? Patient Portal!".format(business_name="PQAA82e45d52")
        #updated_criteria_string = '(since "28-Nov-2019" to "consumer-portal-mailcatcher@internetbrands.com" subject "You\'ve Been Invited to PQAA82e45df2\'? Patient Portal!")'
        updated_criteria_string = "(since \"{formatted_date}\" to \"{message_to}\" subject \"{subject}\")".format(
            message_to="consumer-portal-mailcatcher@internetbrands.com", subject=subject, formatted_date="28-Nov-2019")

        print(updated_criteria_string)
        status, email_id_list = self.mailbox.search(None, updated_criteria_string)
        print(status, email_id_list)




client = GmailClient()
client.get_gmail_instance()
client.find_email_by_criteria()