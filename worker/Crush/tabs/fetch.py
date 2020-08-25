import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os
from tools import Tools
from config import Config


class Fetch(QDialog):

    def __init__(self):
        super(Fetch, self).__init__()
        self.init_UI()
        self._upload_path = {}
        self._upload_path['10.20.0.98'] = r'\\10.20.0.98\var\nfs\ingestor\storage\sesame\common\storage\backup'
        self._upload_path['127.0.0.1'] = r'\\127.0.0.1\storage\common\storage\backup'
        self._upload_path['10.20.0.121'] = r'\\10.20.0.121\var\nfs\ingestor\storage\sesame\common\storage\backup'
        self._local_path = {}
        self.max_row = 30

    def init_UI(self):
        h1_ly = QHBoxLayout()
        # server combobox
        self.sev_cb = QComboBox()
        self.sev_cb.setFixedSize(150, 20)
        self.sev_cb.addItems(['10.20.0.121', '10.20.0.98', '127.0.0.1'])
        h1_ly.addWidget(self.sev_cb)
        # user combobox
        self.usr_cb = QComboBox()
        self.usr_cb.setFixedSize(100, 20)
        self.usr_cb.addItems(['ibexdtx01','ibexdtx02','ibexegs01','ibexsfd01','ibexabd01','ibexgen01','ibexopd01',
                              'ibexpwk01','ibexvwp01','ibexoas01'])
        h1_ly.addWidget(self.usr_cb)
        # fetch button
        self.fetch_bt = QPushButton('Fetch', self)
        self.fetch_bt.setFixedSize(70, 20)
        self.connect(self.fetch_bt, SIGNAL('clicked()'), self.on_fetch_button)
        h1_ly.addWidget(self.fetch_bt)
        # result
        self.result_ly = QTableWidget()
        self.result_ly.setColumnCount(4)
        column_width = [100, 300, 100, 100]
        for column in range(4):
            self.result_ly.setColumnWidth(column, column_width[column])
        headerlabels = ['date', 'file name', '', '']
        self.result_ly.setHorizontalHeaderLabels(headerlabels)
        self.result_ly.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.result_ly.setSelectionBehavior(QAbstractItemView.SelectRows)

        # status bar
        self.status_bar = QStatusBar()
        self.status_bar.showMessage('Ready')
        v = QVBoxLayout()
        v.addLayout(h1_ly)
        v.addWidget(self.result_ly)
        v.addWidget(self.status_bar)
        self.setLayout(v)


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_fetch_button(self):
        self.status_bar.showMessage('Processing... This might take few seconds. Please wait.')
        server = str(self.sev_cb.currentText())
        user = str(self.usr_cb.currentText())
        os.system('net use \\{0}'.format(server))
        f_list = os.listdir(os.path.join(self._upload_path[server], user))
        row = 0
        self.result_ly.setRowCount(self.max_row)
        for folder in f_list[::-1]:
            # cell 1 ,2
            folder_path = os.path.join(self._upload_path[server], user, folder)
            self.result_ly.setItem(row, 0, QTableWidgetItem(folder))
            file_name = [gz for gz in os.listdir(folder_path) if gz.endswith('gz')][0]
            self.result_ly.setItem(row, 1, QTableWidgetItem(file_name))
            # cell 3 download
            self.dwn_btn = QPushButton('Download')
            self.connect(self.dwn_btn, SIGNAL('clicked()'), self.on_dwn_button)
            self.dwn_btn.setProperty('path', os.path.join(folder_path, file_name))
            self.dwn_btn.setProperty('folder', folder)
            self.result_ly.setCellWidget(row, 2, self.dwn_btn)
            # cell 4 open
            self.open_btn = QPushButton('Open')
            self.connect(self.open_btn, SIGNAL('clicked()'), self.on_open_button)
            self.open_btn.setProperty('folder', folder)
            self.result_ly.setCellWidget(row, 3, self.open_btn)
            row += 1
            if row == self.max_row:
                break
        self.result_ly.show()

    def on_dwn_button(self):
        # absolute_path is a QString object
        source_path = str(self.sender().property('path').toPyObject())
        target_path = os.path.join(Config.get_public_item('output_path'), source_path.split('\\')[-1])
        Tools.copy_file(source_path, target_path)
        file_name = Tools.unzip_gz_file(target_path)
        self.status_bar.showMessage('Download completed. {0}'.format(target_path))

        self._local_path[str(self.sender().property('folder').toPyObject())] = file_name

    def on_open_button(self):
        # absolute_path is a QString object
        key = str(self.sender().property('folder').toPyObject())
        if self._local_path.has_key(key):
            file_path = self._local_path[key]
            e = Tools.open_xml_with_notepad(file_path)
            if e != None:
                msg = QMessageBox()
                msg.setText(e.message)
                msg.setWindowTitle('Error')
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
                self.status_bar.showMessage(e.message)
            else:
                self.status_bar.showMessage('Opened {0} with notepad++'.format(file_path))
        else:
            self.status_bar.showMessage('Please download file first.')