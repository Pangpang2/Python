import requests
import os
import shutil
import time
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText


class IngestorService:
    AUTH = 'auth'
    UPLOAD = 'upload'


class AuthenticationAction:
    AUTHENTICATE = 'authenticate'
    AUTHENTICATEMEMBER = 'authenticateMember'
    AUTHENTICATEUSER = 'authenticateUser'
    CLEARCACHE = 'clearCache'
    GETAUTHSESSION = 'getAuthSession'
    GETVERSION = 'getVersion'
    INVALIDATE = 'invalidate'
    SETSESSIONATTRIBUTE = 'setSessionAttribute'
    SETSESSIONATTRIBUTES = 'setSessionAttributes'
    VALIDATE = 'validate'

class UploadAction:
    GETACCESSTOKEN = 'getAccessToken'
    GETCOMMANDS = 'getCommands'
    GETCONFIGURATION = 'getConfiguration'
    GETFULLCONFIGURATION = 'getFullConfiguration'
    GETLASTSUCCESSFULUPLOADID = 'getLastSuccessfulUploadId'
    GETPATIENTRESPONSIBLELINKS = 'getPatientResponsibleLinks'
    GETPATIENTS = 'getPatients'
    GETRESPONSIBLES = 'getResponsibles'
    GETSATELLITECONFIGURATION = 'getSatelliteConfiguration'
    GETUPLOADXMLACCEPTANCE = 'getUploadXMLAcceptance'
    GETUPLOADXMLSTATUS = 'getUploadXMLStatus'
    GETVERSION = 'getVersion'
    GETWRITEBACKXML = 'getWritebackXML'
    PUTFILE = 'putFile'
    UPDATECONFIGURATION = 'updateConfiguration'
    UPLOADLOG = 'uploadLog'
    UPLOADMAILLIST = 'uploadMailList'
    UPLOADMODULES = 'uploadModules'
    UPLOADXML = 'uploadXML'
    UPLOADXMLINLINE = 'uploadXMLInline'


class UploadXMLStatus:
    SUCCESSFUL = 'successful'
    FAILED = 'failed'
    IN_PROGRESS = 'in_progress'
    DELAYED = 'delayed'


class IngestorUpload:

    @staticmethod
    def upload(username, password, upload_file, env):
        """ Generate udbf with simple patients, upload to IBEX and verify upload status

        :param str username:
        :param str password:
        :return:
        """
        # get auth token
        auth_response = IngestorUpload.request_auth_authenticate(username, password, env=env)
        if auth_response.status_code == 200:
            auth_token_node = IngestorUpload.parse_soap_response_content(auth_response, 'authToken')
            auth_token = auth_token_node.text if auth_token_node else ''
        else:
            print auth_response.content
            raise Exception('Get auth token for user:{username} failed'.format(username=username))

        # perform uploadXML action and check upload status
        IngestorUpload.perform_upload_xml_and_check_upload_status(auth_token, upload_file, env=env)
        print('Upload patients for username : {username} is successful'.format(username=username))

    @staticmethod
    def perform_soap_request(srv, action, params=None, attachment=None, env=None):
        """  Create envelop message and send soap request to service

        :param IngestorService srv: service
        :param str action:
        :param dict params:
        :param str attachment:
        :param env:
        :return:
        """
        if attachment:
            message, headers = IngestorUpload.create_soap_message_with_attachment(srv, action, attachment,
                                                                                         params=params)
        else:
            message = IngestorUpload.create_soap_message(srv, action, params=params)
            headers = {'Content-Type': 'text/xml;charset=utf-8'}

        print('Send soap request to action {action} with params {params}.'.format(action=action, params=params))
        response = IngestorUpload.send_soap_request(srv, message, headers=headers, env=env)

        return response

    @staticmethod
    def create_soap_message(srv, action, params=None):
        """ Create soap message

        :param IngestorService srv: service
        :param action:
        :param dict args:
        :return:
        """

        soap_message = """
            <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ibex="http://{srv}.sesamecommunications.com">
                <soapenv:Header/>
                <soapenv:Body>
                    <ibex:{action}>
                        {params}
                    </ibex:{action}>
                </soapenv:Body>
            </soapenv:Envelope>"""

        params_string = ''
        sub_node = ''
        if params:
            for name, value in params.items():
                if type(value) is dict:
                    for sub_name, sub_value in value.items():
                        sub_node = sub_node + '<{sub_name}>{sub_value}</{sub_name}>' \
                            .format(name=name, sub_name=sub_name, sub_value=sub_value)
                    params_string = params_string + '<{name}>'.format(name=name) + sub_node + '</{name}>'.format(
                        name=name)
                else:
                    params_string = params_string + '<{name}>{value}</{name}>'.format(name=name, value=value)
        return soap_message.format(srv=srv, action=action, params=params_string)

    @staticmethod
    def create_soap_message_with_attachment(srv, action, attachment, params=None):
        """ Create soap message with attachment

        :param IngestorService srv: service
        :param str action:
        :param str attachment:
        :param dict args:
        :return: soap message and header info
        """

        # setup multipart
        mtompkg = MIMEMultipart('related', boundary='------=_Part_0_56989739.1555465344345', type='text/xml')

        del (mtompkg['mime-version'])
        del (mtompkg['User-Agent'])
        del (mtompkg['Accept-Encoding'])

        # setup root part
        envelope_message = IngestorUpload.create_soap_message(srv, action, params)
        rootpkg = MIMEText(envelope_message, 'xml')
        rootpkg.set_charset('utf-8')

        del (rootpkg['Content-Transfer-Encoding'])
        del (rootpkg['mime-version'])

        mtompkg.attach(rootpkg)

        # setup attachment part
        filename = os.path.abspath(attachment).split('\\')[-1]
        with open(attachment, 'rb') as fp:
            data = fp.read()

        msg = MIMEBase('application', 'octet-stream')
        msg.set_payload(data)

        msg.add_header('Content-ID', filename)
        del (msg['mime-version'])

        mtompkg.attach(msg)

        # extract body string from MIMEMultipart message
        bound = '--%s' % (mtompkg.get_boundary(),)
        marray = mtompkg.as_string().split(bound)
        mtombody = bound
        mtombody += bound.join(marray[1:])

        mtompkg.add_header("Content-Length", str(len(mtombody)))

        headers = dict(mtompkg.items())
        body = mtompkg.as_string().split('\n\n', 1)[1]
        body = body.replace('\n', '\r\n', 5)

        return body, headers

    @staticmethod
    def send_soap_request(srv, message, env, headers=None):
        """ Send soap request

        :param IngestorService srv: service
        :param str message:
        :param dict headers:
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        """

        if headers is None:
            headers = {'Content-Type': 'text/xml;charset=utf-8'}

        if str(env).lower() == 'stg':
            ingestor_host = "http://stg-ibex.internetbrands.com"

        else:
            ingestor_host = 'http://10.20.0.121:9999'

        url = "{ingestor_host}/{srv}/ws".format(ingestor_host=ingestor_host, srv=srv)

        response = requests.post(url, headers=headers, data=message)

        return response

    ###############
    ##
    # Common used methods
    ##
    ###############

    @staticmethod
    def parse_soap_response_content(response, node_name, limit=1):
        """ Get the value of the node

        :param response:
        :param node_name:
        :return:
        """

        if response is not None and type(response) is not str:
            bs = BeautifulSoup(response.content, 'html.parser')
        elif response is not None:
            bs = BeautifulSoup(response, 'html.parser')

        nodes = bs.find_all(node_name.lower(), limit=limit)

        if limit == 1:
            return nodes[0] if len(nodes) == 1 else None
        else:
            return nodes

        return None

    @staticmethod
    def get_upload_xml_status(auth_token, retry=5, env=None):
        """  Get uploadXML status after retry times

        :param str auth_token:
        :param int retry:
        :param str env:
        :return:
        """

        status = ''
        while retry:
            time.sleep(3)
            response = IngestorUpload.request_upload_get_upload_xml_status(auth_token, env=env)
            if response.status_code == 200:
                status_node = IngestorUpload.parse_soap_response_content(response, 'status')
                if status_node.text == UploadXMLStatus.IN_PROGRESS:
                    continue
                else:
                    break
            else:
                continue

            retry -= 1

        print response.content
        return status_node.text

    @staticmethod
    def perform_upload_xml_and_check_upload_status(auth_token, upload_file, retry=5, env=None):
        """ Upload xml and check upload status

        :param auth_token:
        :param upload_file:
        :param retry:
        :param env:
        :return:
        """

        print('Perform uploadXML action.')
        response = IngestorUpload.request_upload_upload_xml(auth_token, upload_file, env=env)
        if response.status_code != 200:
            raise Exception('Request to uploadXML failed.')

        status = IngestorUpload.get_upload_xml_status(auth_token, retry=retry, env=env)
        if status != UploadXMLStatus.SUCCESSFUL:
            raise Exception('UploadXML failed with status {0}'.format(status))


    ###############
    ##
    # Request ingestor service action methods
    ##
    ###############

    @staticmethod
    def request_auth_authenticate(username, password, auth_action=AuthenticationAction.AUTHENTICATEMEMBER, env=None):
        """ Send request to authenticate or authenticateMember or authenticateUser action

        :param str username:
        :param str password:
        :param str auth_action: 'authenticate', 'authenticateMember' or 'authenticateUser'
        :param str env:
        :return:
        """

        params = {'userName': username,
                  'password': password}

        response = IngestorUpload.perform_soap_request(IngestorService.AUTH, auth_action, params=params, env=env)
        return response

    @staticmethod
    def request_upload_upload_xml(auth_token, attachment, env):
        """ Send request to uploadXML action

        :param str auth_token:
        :param str attachment:
        :param str env:
        :return:
        """

        params = {'authToken': auth_token}

        response = IngestorUpload.perform_soap_request(IngestorService.UPLOAD, UploadAction.UPLOADXML,
                                                              params=params, attachment=attachment, env=env)
        return response

    @staticmethod
    def request_upload_get_upload_xml_status(auth_token, env):
        """ Send request to getUploadXMLStatus action

        :param str auth_token:
        :param str env:
        :return:
        """

        params = {'authToken': auth_token}

        response = IngestorUpload.perform_soap_request(IngestorService.UPLOAD, UploadAction.GETUPLOADXMLSTATUS
                                                              , params=params, env=env)
        return response





