import logging
from threading import Thread
from wsgiref.simple_server import make_server
from spyne import Application
from spyne.protocol.soap.soap12 import Soap12
from spyne.server.wsgi import WsgiApplication

from server.server import AuthenticationSOAPPortBinding
from server.upload_server import UploadSOAPPortBinding


class AuthenticationThread(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        auth_wsgi_app = self.get_auth_service_instance()
        auth_server = make_server('127.0.0.1', 9999, auth_wsgi_app)
        auth_server.serve_forever()

    def get_auth_service_instance(self):
        #Glue the service definition, input and output protocols
        auth_soap_app = Application([AuthenticationSOAPPortBinding],
                               'http://auth.sesamecommunications.com',
                               name='Authentication',
                               in_protocol=Soap12(validator='lxml'),
                               out_protocol=Soap12())

        # Wrap the Spyne application with its wsgi wrapper
        auth_wsgi_app = WsgiApplication(auth_soap_app)

        return auth_wsgi_app

class UploadThread(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        upload_wsgi_app = self.get_upload_service_instance()
        upload_server = make_server('127.0.0.1', 9999, upload_wsgi_app)
        upload_server.serve_forever()

    def get_upload_service_instance(self):
        #Glue the service definition, input and output protocols
        upload_soap_app = Application([UploadSOAPPortBinding],
                               'http://upload.sesamecommunications.com',
                               name='Upload',
                               in_protocol=Soap12(validator='lxml'),
                               out_protocol=Soap12())

        # Wrap the Spyne application with its wsgi wrapper
        upload_wsgi_app = WsgiApplication(upload_soap_app)

        return upload_wsgi_app


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

    logging.info("wsdl is at: http://localhost:9999/auth/ws?wsdl")
    auth_thread = AuthenticationThread()
    auth_thread.start()

    logging.info("wsdl is at: http://localhost:9999/upload/ws?wsdl")
    upload_thread = UploadThread()
    upload_thread.start()
    # try:
    #     logging.info("wsdl is at: http://localhost:8000/auth/ws?wsdl")
    #     thread.start_new_thread(IngesterService.start_auth_server, ('name'))
    #
    #     # logging.info("wsdl is at: http://localhost:8001/upload/ws?wsdl")
    #     # thread.start_new_thread(IngesterService.start_upload_server, ('name'))
    # except:
    #     print 'Error: unable to start thread'