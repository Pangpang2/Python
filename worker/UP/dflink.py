import requests


class DFLink:
    """ Upload file through dflink service"""

    @staticmethod
    def upload(url, license, file_path):

        files = {'upload': open(file_path, 'rb')}
        data = {'license': license, 'Content-Type': 'multipart/mixed'}
        session = requests.session()

        print('Request to %s'%url)
        print('license_key: %s'%license)
        response = session.post(url=url, files=files, data=data)

        if response.status_code == 200:
            if response.text == 'Upload successful.':
                print('Upload to dflink service successful')
            else:
                raise Exception('Upload to dflink service failed with error: \r\n %s'%response.text)
        else:
            raise Exception('Upload to dflink service failed with error %s' %str(response.status_code))




# if __name__ == '__main__':
#     Upload.upload_xml_through_ingestor('95F59D26-DBEE-9B78-D346-928806A2381E', r'C:\usr\local\d3one\in\d30\130000001.ng30D1_Full.2019-05-04-14-33-33.zip')
