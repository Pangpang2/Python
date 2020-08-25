
headers = {'Authorization':''}
access_token = '1223'
headers['Authorization'] = "Bear {access_token}".format(access_token=access_token)
print headers
