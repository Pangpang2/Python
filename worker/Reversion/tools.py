import gzip
import shutil


class Tools:

    @staticmethod
    def gzip_file(output_path):
        gz_file_name = '%s.gz' % output_path
        try:
            with open(output_path, 'rb') as f_in, gzip.open(gz_file_name, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
                return gz_file_name
        except Exception as e:
            raise Exception("Error when compress to gz file: " + str(e))