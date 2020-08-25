from flask import Flask
from flask_spyne import Spyne
from spyne.protocol.soap import Soap11, mime
from spyne.protocol.http import HttpRpc
from spyne.model.primitive import Unicode, Integer
from spyne.model.binary import File

app = Flask(__name__)
spyne = Spyne(app)

class Authentication(spyne.Service):
    __service_url_path__ = '/auth/ws'
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()

    @spyne.srpc(Unicode, Unicode, Unicode, _returns=Unicode, _out_variable_name='authToken' )
    def authenticateMember( partnerId, userName, password, ):
        authToken='T0JMTERHaVRnOTI2RE92alJCdzR5UT09'
        return authToken

class Upload(spyne.Service):
    __service_url_path__ = '/upload/ws'
    # __in_protocol__ = Soap11(validator='lxml')
    __in_protocol__ = Soap11(validator='lxml')
    __out_protocol__ = Soap11()

    @spyne.srpc(Unicode, Unicode, _returns=Unicode, _out_variable_name='authToken')
    def uploadXML(authToken, uploadId):
        with open(r'D:\Temp\a.gz', 'wb') as f:
            import base64
            a = base64.b64decode(file.data[0])
            f.write(a)

        authToken='T0JMTERHaVRnOTI2RE92alJCdzR5UT09'

        return authToken

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port='9999')