import os
import time
from zipfile import ZipFile, ZIP_DEFLATED
import os
from datautility import DataUtility
from customergen import CustomerGenerator
from extractgen import ExtractGenerator
from entitygen import EntityGenerator


def generate_upload_message(business_info, file_path):
    """
    Generate Kafka message with upload info
    :param business_info: business information
    :param file_path: full path of the file to upload
    :return: message body in json format
    """
    print("Generate upload message.")
    return {
        'publisher': 'test publisher',
        'businessId': business_info['bid'],
        'nodeGroup': business_info['node'],
        'fileName': os.path.basename(file_path),
        'arrivalTime': int(time.time()),
        'uploadType': 'FULL',
        'fileSizeBytes': int(os.path.getsize(file_path))
    }

def build_simple_account_data(account, upload_scope, is_delete=False):
    account_args = EntityGenerator.get_default_account('1')
    # From basic template
    root_path = r"E:\Git\Python\worker\KafkaMessageCreater\resources\templates"
    DataUtility.from_basic_template(root_path +'/df/BasicUpload.xml',
                                    ExtractGenerator.get_default_extract(account, upload_scope))
    # Add customer data
    customer_args = CustomerGenerator.get_default_customer('1')
    DataUtility.add_entity_from_template('df/CustomerInitial.xml', customer_args, './/Business')
    # Add account data
    DataUtility.add_entity_from_template('df/AccountDelete.xml' if is_delete else 'df/AccountInitial.xml',
                                         account_args,
                                         './/Business/Customer[@id=\'' + '1' + '\']')
    # Write to file
    return DataUtility.write_to_file()

def generate_zip_package(account, data_path, customized_package_name=None, encrypt=True):
    if customized_package_name is None:
        timestamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        suffix = 'p.zip' if encrypt else 'zip'
        customized_package_name = '{business_id}.{node_group}.{timestamp}.{suffix}'.format(
            business_id=account['bid'],
            node_group=account['node_short'],
            timestamp=timestamp,
            suffix=suffix
        )
    package_root = r'E:\Git\upload_processor_docker\docker\usr\local\d3one\in'
    package_path = os.path.join(package_root, account['node_short'], customized_package_name)
    # prepare directory
    package_dir = os.path.join(package_root, account['node_short'])
    if not os.path.exists(package_dir):
        os.makedirs(package_dir)
    # package the data
    if encrypt:
        make_zip_package(data_path, package_path, account['license'])
    else:
        make_zip_package(data_path, package_path)

def make_zip_package(source_file_path, target_package_path, password=None):
    pack = ZipFile(target_package_path, 'w', ZIP_DEFLATED)
    pack.write(source_file_path, os.path.basename(source_file_path))
    if password is not None:
        pack.setpassword(str(password).encode())
    pack.close()

def send_message_avro(self, topic, message):
    print("Send AVRO Kafka message.")
    # Prepare for request
    headers = {
        'Content-Type': 'application/vnd.kafka.avro.v2+json',
        'Accept': 'application/vnd.kafka.v2+json, application/vnd.kafka+json, application/json'
    }
    body = {
        'value_schema': self.__get_latest_schema(topic),
        'records': [
            {
                'value': message
            }
        ]
    }
    response = self.__rest.call_rest_service(endpoint='/topics/' + topic, method='POST', header=headers, data=body)
    print('Kafka message produce returned: {code}'.format(code=response.status_code))
    return response

if __name__ == '__main__':
    topic = 'df_file_uploaded_avro'
    business_info = {
        'bid': '138000213',
        'license': '91D2AF8A-56C7-FE29-301B-C2E44B4C656D',
        'node': 'd338.demandforced3.com',
        'node_short': 'df',
        'api': 'test',
        'pms': 'Dentrix',
        'pms_version': '5.0'
    }
    file_path = build_simple_account_data(business_info, 'full')
    message = generate_upload_message(business_info, file_path)
    print(message)