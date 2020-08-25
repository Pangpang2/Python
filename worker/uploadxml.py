import urllib
import urllib2

# url = "http://stg-ibex.internetbrands.com:80/ws"
#
# soapAction = "http://10.20.0.95:8090/w/authenticate"
# post_data = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:auth="http://auth.sesamecommunications.com">
#    <soapenv:Header/>
#    <soapenv:Body>
#       <auth:authenticate>
#          <userName>dfcxauta6bdca13@d3one.com</userName>
#          <password>password</password>
#       </auth:authenticate>
#    </soapenv:Body>
# </soapenv:Envelope>"""
#
# http_headers = {
#  "User-Agent":"Mozilla/4.0 (compatible; MSIE 5.5;Windows NT)",
#  "Accept" :  "application/soap+xml,multipart/related,text/*",
#  "Cache-Control" :  "no-cache",
#  "Pragma" :  "no-cache",
#  "Content-Type" :  "text/xml; charset=utf-8",
#  "SOAPAction" :  'authenticate'
#
# }
#
# request_object = urllib2.Request(url, post_data, http_headers)
# response = urllib2.urlopen(request_object)
# html_string = response.read()
#
# print html_string


# url = "http://10.20.0.95:8090/ws"
#
# post_data = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:auth="http://auth.sesamecommunications.com">
#    <soapenv:Header/>
#    <soapenv:Body>
#       <auth:authenticateMember>
#          <partnerId>?</partnerId>
#          <userName>ibextdx01</userName>
#          <password>onibex1!</password>
#       </auth:authenticateMember>
#    </soapenv:Body>
# </soapenv:Envelope>"""
#
# http_headers = {
#  "Accept-Encoding": "gzip,deflate",
#  "User-Agent":"Apache-HttpClient/4.1.1 (java 1.5)",
#  "Cache-Control" :  "no-cache",
#  "Pragma" :  "no-cache",
#  "Content-Type" :  "text/xml; charset=UTF-8",
#  "SOAPAction":  'authenticateMember'
#
# }
#
# request_object = urllib2.Request(url, post_data, http_headers)
# response = urllib2.urlopen(request_object)
# html_string = response.read()
#
# print html_string
#
#
# url = "https://stg-ibex.internetbrands.com/auth/ws"
#
# post_data = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:upl="http://upload.sesamecommunications.com">
#    <soapenv:Header/>
#    <soapenv:Body>
#       <upl:getVersion/>
#    </soapenv:Body>
# </soapenv:Envelope>"""
#
# http_headers = {
#  "Accept-Encoding": "gzip,deflate",
#  "User-Agent":"Apache-HttpClient/4.1.1 (java 1.5)",
#  "Cache-Control" :  "no-cache",
#  "Pragma" :  "no-cache",
#  "Content-Type" :  "text/xml; charset=UTF-8",
#  "SOAPAction":  'getUploadXMLStatus',
#  "host":"stg-ibex.internetbrands.com",
#  "port":"443"
#
# }
#
# request_object = urllib2.Request(url, post_data, http_headers)
# response = urllib2.urlopen(request_object)
# print response.en
# html_string = response.read()
#
# import sys
# type = sys.getfilesystemencoding()
# html_string.decode("utf8").encode(type)
#
# print html_string

#
# from httplib import HTTPSConnection
#
# client = HTTPSConnection(host='stg-ibex.internetbrands.com', port=443)
# body = """
# <SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/"><SOAP-ENV:Body><ibex:authenticateMember xmlns:ibex="http://auth.sesamecommunications.com"><password>^bwe$5Yn</password><partnerId>0</partnerId><userName>DentrixIBEX@d3one.com</userName></ibex:authenticateMember></SOAP-ENV:Body></SOAP-ENV:Envelope>"""
# headers={"SOAPAction":  'getUploadXMLStatus',
# "host":"stg-ibex.internetbrands.com"}
# client.request(method='',  url='https://stg-ibex.internetbrands.com/auth/ws',body=body, headers=headers)
# # print response
# # client.connect()
# # r = client.send(body)
# #r = client.connect()
# r= client.getresponse()
# print r
import gzip
import base64

attachment=r"E:\Git\DF_CX_Automation_workspace\library\data\templates\udbf\generate\ibexcxautIlBVo_2019-09-18-23-47-36.xml.gz"
# #print gzip.open(attachment, "rb").read()
# print gzip.open(attachment).read()
# # print open(attachment, mode='rb').read()
# # print open(attachment).read()

with open(attachment, 'rb') as f:
    print base64.b64encode(f.read())

print 'H4sICIgkg10C/2liZXhjeGF1dElsQlZvXzIwMTktMDktMTgtMjMtNDctMzYueG1sAHVT247aMBB9X2n/YX+AdQK9ALIiBQUqtJRWvVD1yTLxpB012Mh2Ij6/k8QhgXbfPOccz314pY7FZJY8Pjw9cQe2xhwE6sLYk/RodEsQhRo9yjKJOeufganBukY4fSauNwJ3NrZxIpT0kEyjeDGJFpP47bfpbPnm/XL27jmKIs5uVOFndf5lpQKh0MljCaoJ/A/WRzk5UYNWxiYZaG/xQj4HrPdI1Wl5ggSPcMkvsvLbcnUw5LYngtBBCbnHGkR1Lo1UooQayoQSfYVpe8deax61jijfe/9MDCXpgk2IhdzYazHbLNmkL2txm6Wg6MQEzQat8/sm5Y38A5u9wFWKPzgb8CDcyZFutxdfYjCOsyscZCu0/nfWdD9ezLsZzTkb0CD76qWvXJK2LeAsmIFMlbLg3DZjPfKB2g+2GVx4jZI6oEOfjbcimnd5DcxI/lGi9qClzuG/n+75cZ/uQ83b4u6oocKiGJXwqShopCNgfaEwDmn79saD60b1sv65bB+HdPd9zdm96PGBs9shs5staE7quiK0+c0ddBG5oo3rDNrT/lL/Albmfl+0AwAA'
