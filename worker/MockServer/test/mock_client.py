from suds.client import Client

auth_wsdl_url = "http://localhost:8000/auth/ws?wsdl"
upload_wsdl_url = "http://localhost:8000/upload/ws?wsdl"

def auth_test(url, partnerid, name, password):
    client = Client(url)
    client.service.authenticateMember(partnerid, name, password)
    req = str(client.last_sent())
    response = str(client.last_received())
    print req
    print response

def upload_test(url, partnerid, name):
    client = Client(url)
    client.service.uploadXML(partnerid, name)
    req = str(client.last_sent())
    response = str(client.last_received())
    print req
    print response

if __name__ == '__main__':
    #auth_test(auth_wsdl_url, '?', 'ibextdx01', 'onibex1!')
    upload_test(upload_wsdl_url,'?','?')