import _winreg
import os
import shutil
import stat
import gzip
import subprocess


class Tools:


    @staticmethod
    def get_app_install_path(app_name):
        try:
            root = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, '')
            sub_key = _winreg.OpenKey(root, r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\{0}'.format(app_name))
            if sub_key is not None:
                return _winreg.QueryValueEx(sub_key, '')[0]
        except Exception as e:
            raise Exception('Please install {0} first.'.format(app_name))

    @staticmethod
    def copy_file(source, target):
        directory_ath = os.path.dirname(target)
        if not os.path.exists(directory_ath):
            os.makedirs(directory_ath)
        if os.path.exists(target):
            os.chmod(target, stat.S_IWRITE)
        shutil.copyfile(source, target)

    @staticmethod
    def unzip_gz_file(file_name):
        unzip_file_name = file_name.replace('.gz', '')
        with gzip.open(file_name, 'rb') as f_in, open(unzip_file_name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            return unzip_file_name

    @staticmethod
    def open_xml_with_notepad(file_path):
        try:
            subprocess.call([Tools.get_app_install_path('notepad++.exe'), file_path])
        except Exception as e:
            return e
        return None


