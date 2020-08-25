import requests

# body="""<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
# <SOAP-ENV:Body>
# <ibex:authenticateMember xmlns:ibex="http://auth.sesamecommunications.com">
# <password>^bwe$5Yn</password>
# <partnerId>?</partnerId>
# <userName>DentrixIBEX@d3one.com</userName>
# </ibex:authenticateMember></SOAP-ENV:Body></SOAP-ENV:Envelope>
# """

body="""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ibex="http://auth.sesamecommunications.com">
   <soapenv:Body>
      <ibex:authenticateMember>
         <partnerId>?</partnerId><userName>ibexdtx01</userName><password>*Fc^Z6).</password>
      </ibex:authenticateMember>
   </soapenv:Body>
</soapenv:Envelope>
"""

# body = """
# <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:auth="http://auth.sesamecommunications.com">
#    <soapenv:Header/>
#    <soapenv:Body>
#       <auth:getVersion>
#       </auth:getVersion>
#    </soapenv:Body>
# </soapenv:Envelope>
# """


from bs4 import BeautifulSoup

headers = {'Content-Type': 'text/xml;charset=utf-8'}
r = requests.post("http://stg-ibex.internetbrands.com/auth/ws", headers=headers, data=body)
bs = BeautifulSoup(r.content, 'html.parser')
nodes = bs.find_all('authtoken')
for node in nodes:
    print node.text
