### urllib3
import certifi
import urllib3
import json


# client_id = 63063
# smb_guid = 0dbfba2f-0e5f-4697-849d-5ba087ae50ab
# username/password =dfcxauta6bdca13@d3one.com/password
# appointment_id = afb94c328f2f8ce9c8227531a82b3499e4f6df12b4ad767a9ab6114f4e73a
http = urllib3.PoolManager()

# get access token
print '1.Get access token:'
url_1 = 'https://stg-ibcv2.internetbrands.com/auth/realms/demandforce/protocol/openid-connect/token'
headers_1 = {'Content-Type': 'application/x-www-form-urlencoded',
           'Postman-Token': 'e2f8c436-2d7d-4200-abab-7cc30723fa3c'}

# fields is for query parameters
#body_1 = 'grant_type=client_credentials&client_id=ibex&client_secret=40479efe-e0fe-4d9a-b927-bc8e2cbab95c&username=dfcxauta6bdca13@d3one.com&password=password'
body_1 = 'grant_type=password&client_id=demandforce&client_secret=325c26b7-f98d-4692-9139-017942feba21&username=dfcxauta6bdca13@d3one.com&password=password'
print 'url:' + url_1
print 'headers:' + str(headers_1)
print 'body:' + body_1

r = http.request('POST', url=url_1, headers=headers_1, body=body_1)
if r.status == 200:
    access_token = str(json.loads(r.data.decode('utf-8'))[u'access_token'])
    print access_token
else:
    print r.status
    print r.data

print '2.Request to Appointment endpoint'
#access_token='a516a9e2-852e-4b73-959a-de8da8467d08'
url_2 = 'http://stg-df-dkr3.internetbrands.com:10001/business/0dbfba2f-0e5f-4697-849d-5ba087ae50ab/appointment/afb94c328f2f8ce9c8227531a82b3499e4f6df12b4ad767a9ab6114f4e73a'
headers_2 = {'Authorization': 'Bearer %s'%access_token}
r = http.request('GET', url=url_2, headers=headers_2)
print 'url:' + url_2
print 'headers:' + str(headers_2)
if r.status ==200:
    data = str(json.loads(r.data.decode('utf-8')))
    print data
else:
    print r.status
    print r.data


### http

# import requests
# data =
# r = requests.post(url_1, body)


# import requests
# site_url = 'https://stg.demandforced3.com/bp2/index.jsp'
# file_url = 'https://www.marketing.org.nz/Folder?Action=Download&Folder_id=67&File=NZDI.zip'
#
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
# login_info = {'username':'dfcxauta1b041df@d3one.com',
#              'password':'F.85M4p*'}
#
# s = requests.Session()
# s.get(site_url)
# r = s.post(site_url,
#            data=login_info,
#            headers=headers
#            )
# print(r.status_code)
# print(r.text)

