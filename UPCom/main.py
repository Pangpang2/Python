from xmlWriter import *
from dbWriter import *

class main(object):
    def __init__(self, file):
        self.file_path = self.get_file_path()
        self.xml_writer = xmlWriter(self.file_path)
        self.xml_writer.output_from_db()
        self.xml_writer.output_from_xml()

    def get_file_path(self):
        f_dir = 'E:\\May\\UP\\TestData\\'
        for file in os.listdir(f_dir):
            if os.path.splitext(file)[1] == '.xml':
                return os.path.abspath(f_dir+file)



# if(__name__ == 'main'):
#     main()
def get_file_path():
    f_dir = 'C:\\usr\\local\\d3one\\in\\d30\\'
    for file in os.listdir(f_dir):
        if os.path.splitext(file)[1] == '.xml':
            return os.path.abspath(f_dir+file)

file_path = get_file_path()
business_id = file_path.split('\\')[-1].split('.')[0]
output_path = os.getcwd() + '/Output/'

db_writer = dbWriter(business_id, output_path)
db_writer.output_from_db()

industry = db_writer.get_industry()


xml_writer = xmlWriter(file_path, industry, business_id, output_path)
xml_writer.output_from_xml()


