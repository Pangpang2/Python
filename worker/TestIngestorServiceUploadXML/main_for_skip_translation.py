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
        print(data)
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

    # staging
    auth_url = 'http://stg-ibex.internetbrands.com/auth/ws'
    up_url = 'http://stg-ibex.internetbrands.com/upload/ws'
    # successed

    # 86325 138049948
    auth_token = get_auth_token(auth_url, 'ibexcxautCAedQ', 'onibex1!')
    print(auth_token)
    gz_file = compress_to_gz_file("./data/skip.xml")
    print(gz_file)

    # prod
    # auth_url = 'https://ibex.internetbrands.com/auth/ws'
    # up_url = 'https://ibex.internetbrands.com/upload/ws'
    # # successed
    # auth_token = get_auth_token(auth_url, 'IBEXtest07@d3one.com', '98Wk:2Dx')
    # print(auth_token)
    # gz_file = compress_to_gz_file( "./data/test.xml")
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

