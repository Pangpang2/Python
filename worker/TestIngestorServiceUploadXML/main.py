from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import requests
import time
import os
import gzip
import shutil
import json


def upload_xml(url, auth_token, filepath):
    envelope = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:upl="http://upload.sesamecommunications.com">
       <soapenv:Header/>
       <soapenv:Body>
          <upl:uploadXML>
             <authToken>{auth_token}</authToken>
          </upl:uploadXML>
       </soapenv:Body>
    </soapenv:Envelope>
    """.format(auth_token=auth_token)

    #################
    mtompkg = MIMEMultipart('related',boundary='------=_Part_0_56989739.1555465344345', type='text/xml')

    del(mtompkg['mime-version'])
    del(mtompkg['User-Agent'])
    del(mtompkg['Accept-Encoding'])

    ###########################
    rootpkg = MIMEText(envelope, 'xml')
    rootpkg.set_charset('utf-8')

    del(rootpkg['Content-Transfer-Encoding'])
    del(rootpkg['mime-version'])

    mtompkg.attach(rootpkg)

    ##############################
    filename = os.path.abspath(filepath).split('\\')[-1]

    with open(filepath, 'rb') as fp:
        msg = MIMEBase('application', 'octet-stream')
        # import codecs
        # data = .load(fp, encoding='ascii')
        data = fp.read()
        # print(data)
        msg.set_payload(data)
        encoders.encode_base64(msg)
    msg.add_header('Content-ID', filename)

    del(msg['mime-version'])

    mtompkg.attach(msg)

    #############################################
    bound = '--%s' % (mtompkg.get_boundary(), )
    marray = mtompkg.as_string().split(bound)
    mtombody = bound
    mtombody += bound.join(marray[1:])

    mtompkg.add_header("Content-Length", str(len(mtombody)))

    # print(mtombody)

    headers = dict(mtompkg.items())
    body = mtompkg.as_string().split('\n\n', 1)[1]
    body = body.replace('\n', '\r\n', 5)
    response = requests.post(url, data=body, headers=headers)

    return response


def parse_soap_response_content(response, node_name, first_only=True):
    if response:
        bs = BeautifulSoup(response.content, 'html.parser')
        nodes = bs.find_all(node_name.lower())

        if first_only:
            return nodes[0]
        else:
            return nodes

    return None

def get_upload_status(url, auth_token):
    headers = {'Content-Type': 'text/xml;charset=UTF-8'}
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:upl="http://upload.sesamecommunications.com">
           <soapenv:Header/>
           <soapenv:Body>
              <upl:getUploadXMLStatus>
                 <authToken>{auth_token}</authToken>
              </upl:getUploadXMLStatus>
           </soapenv:Body>
        </soapenv:Envelope>""".format(auth_token=auth_token)

    response = requests.post(url, data=body, headers=headers)
    status = parse_soap_response_content(response, 'status')
    error = parse_soap_response_content(response, 'errorMessage')
    print(status, error)
    return status.text


def get_auth_token(url, username, password):
    headers = {'Content-Type': 'text/xml;charset=UTF-8'}
    body = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:auth="http://auth.sesamecommunications.com">
                   <soapenv:Header/>
                   <soapenv:Body>
                      <auth:authenticateMember>
                         <userName>{username}</userName>
                         <password>{password}</password>
                      </auth:authenticateMember>
                   </soapenv:Body>
                </soapenv:Envelope>""".format(username=username, password=password)

    response = requests.post(url, data=body, headers=headers)
    print(response.status_code)
    print(response.content)
    status = parse_soap_response_content(response, 'authToken')
    return status.text

def compress_to_gz_file(file_name):
    """
    compress xml file to gz file
    :param str file_name:
    :rtype: str
    :return: gz file full path
    """
    gz_file_name = '%s.gz' % file_name
    try:
        with open(file_name, 'rb') as f_in, gzip.open(gz_file_name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            return gz_file_name
    except Exception as e:
        raise Exception("Error when compress to gz file: " + str(e))


if __name__ == '__main__':

    folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')
    upload_file = 'test_delta.xml'
    env = 'stg'
    env = 'prod'

    if env == 'stg':
        # # staging
        auth_url = 'http://stg-ibex.internetbrands.com/auth/ws'
        up_url = 'http://stg-ibex.internetbrands.com/upload/ws'


        # account = {'username': '138056253', 'password': 'CEBF9AB5-9D79-A2B3-94BE-1E62233742DD'}  # 91954
        # account = {'username': 'J_dentrixqatest2_1@d3one.com', 'password': 'Abc1234!') #57566
        account = {'username': 'ibexmaualcreate04', 'password': 'onibex1!'}  # 107117 license key: 04

        ####################### Lighthouse lg_initial lg_delta
        # account = {'username': 'ibexcxaut0xbig', 'password': 'onibex1!'}  # 107214  7306BA28-FF73-6D8E-44AE-01C8606C3942

        #################### used for large file
        # account = {'username': '138054833', 'password': '09C88ED2-8F63-CB5E-BDDA-1E857536A0E8'} # 91954
        # account = {'username': '138049948', 'password': 'C545F25C-3E3B-55D9-8227-7B9975FAF6C7'} # 86325

    else:
        # prod
        auth_url = 'https://ibex.internetbrands.com/auth/ws'
        up_url = 'https://ibex.internetbrands.com/upload/ws'

        # account = {'username': 'IBEXtest04@d3one.com', 'password': 'nG2b5d:6'}  # 15
        account = {'username': 'IBEXtest05@d3one.com', 'password': 'gL(D@4Kp'}  # 16 CF3FFA82-921E-D5BB-65A9-DEB33C89B5E2
        # account = {'username': 'IBEXtest07@d3one.com', 'password': '98Wk:2Dx'}  # 18


    print('env: {env} username: {username} password:{password}'.format(env=env, username=account['username'], password=account['password']))
    print('upload file: {upload_file}'.format(upload_file=upload_file))
    auth_token = get_auth_token(auth_url, account['username'], account['password'])
    print(auth_token)
    gz_file = compress_to_gz_file( "{folder}/{file_name}".format(folder=folder, file_name=upload_file))
    # print(gz_file)

    response = upload_xml(up_url, auth_token, gz_file)

    if response.status_code == 200 :
        status = 'in_progress'
        while status == 'in_progress':
            time.sleep(5)
            status = get_upload_status(up_url, auth_token)
    else :
        faultstring = parse_soap_response_content(response, 'faultstring')
        print(response.content)

    ################
    # couple uploads
    # !!!!!!! NOTE: make sure the upload is delta initial = 0 or  small files
    # !!!!!! 135000001-135000100 test.xml
    # !!!!!! 135000101-135000200 large.xml

    # auth_url = 'http://stg-ibex.internetbrands.com/auth/ws'
    # up_url = 'http://stg-ibex.internetbrands.com/upload/ws'
    #
    # for i in range(1,16):
    #     upload_list = []
    #     for username in range(135000001,135000101,1):
    #         upload_info = {}
    #         # print('Round:' + str(i))
    #         auth_token = get_auth_token(auth_url, str(username), 'onibex1!')
    #         # print('username:' + str(username))
    #         # print(auth_token)
    #         gz_file = compress_to_gz_file("./data/test.xml")
    #         # print(gz_file)
    #         # response = upload_xml(up_url, upload_info['token'], upload_info['file'])
    #         # print(response.status_code)
    #         upload_info['username'] = str(username)
    #         upload_info['token'] = auth_token
    #         upload_info['file'] = gz_file
    #         upload_list.append(upload_info)
    #
    #         # 10 files upload at the same time
    #         if len(upload_list)%10 == 0:
    #             for upload_info in upload_list:
    #                 print('Upload round {0} for {1}'.format(i, upload_info['username']))
    #                 response = upload_xml(up_url, upload_info['token'], upload_info['file'])
    #                 print(response.status_code)
    #             upload_list = []
    ###############