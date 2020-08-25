from suds.client import Client as SudsClient

url = 'http://stg-ibex.internetbrands.com:443/auth/ws?wsdl'
client = SudsClient(url=url, cache=None)
r = client.service.getVersion();
print r


# url = 'http://127.0.0.1:5000/upload/ws?wsdl'
# client = SudsClient(url=url, cache=None)
# r = client.service.echo1(str='hello world1', cnt=3)
# print r