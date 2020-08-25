import subprocess
import time
from pywinauto.application import Application

file = subprocess.Popen('C:\Program Files (x86)\Tencent\WeChat\WeChat.exe')

time.sleep(1)

app = Application(backend = 'uia').connect(process=12632)

wxWindow = app[u'WeChat']
# wxWindow.print_control_identifiers()
print('--------------------')

#wxWindow.print_control_identifiers()
txlBtn = wxWindow.child_window(title="Contacts", control_type="Button", top_level_only=False)

txlBtn.print_control_identifiers()
txlBtn.click()
