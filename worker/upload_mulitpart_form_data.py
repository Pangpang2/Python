import requests


business_name = 'J_image_servicebb8210a5_1@d3one.com'
business_password = 'ondemand1!QAM'
smb_guid = '4c05abff-f5cf-4c27-b11a-01214a9fd67e'

session = requests.session()
body = {"grant_type": "password", "client_id": "demandforce", "client_secret": '325c26b7-f98d-4692-9139-017942feba21',
                "username": business_name, "password": business_password}
response_json = session.post('https://stg-ibcv2.internetbrands.com/auth/realms/demandforce/protocol/openid-connect/token',
                            body,verify=False).json()

access_token = response_json['access_token']


url = "https://stg-image-service.internetbrands.com/business/{smb_guid}/v1/images/user/1/category/2".format(smb_guid=smb_guid)

files = {'image':('Spa-Breaks-Tile.jpg', open("Spa-Breaks-Tile.jpg", 'rb'), 'image/jpeg')}

headers = {
    'authorization': "Bearer {access_token}".format(access_token=access_token)
}

response = requests.session().post(url=url, files=files, headers=headers)
print(response.text)