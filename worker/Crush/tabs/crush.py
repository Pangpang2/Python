import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import subprocess
from reader import Reader
from tools import Tools
import os


class Crush(QDialog):

    def __init__(self):
        super(Crush, self).__init__()
        self.entities = []
        self.init_UI()

    def init_UI(self):
        # Checkbox Layout
        ck_ly = QGridLayout()
        names = ['Accounts', 'Addresses', 'Alerts', 'Appointments', 'AppointmentProcedureLinks', 'CalendarBlocks',
                 'EMails', 'InsuranceContracts', 'Ledgers', 'Offices', 'Recalls', 'Referrings', 'Responsibles',
                 'ResponsibleEMailLinks', 'ResponsiblePhoneLinks', 'Patients', 'PatientAlertLinks', 'PatientEMailLinks',
                 'PatientPhoneLinks', 'PatientReferrignLinks', 'PatientResponsibleLinks', 'PatientStaffLinks', 'Phones',
                 'Procedures', 'Staff', 'TreatmentPlans']
        positions = [(i, j) for i in range(6) for j in range(5)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            checkbox = QCheckBox(name)
            self.connect(checkbox, SIGNAL('clicked()'), self.on_checkbox)
            ck_ly.addWidget(checkbox, *position)

        #File Layout
        self.file_edit = QLineEdit()
        self.browse_btn = QPushButton()
        self.browse_btn.setText("Browse")
        self.connect(self.browse_btn, SIGNAL("clicked()"), self.on_browse_button)

        file_ly = QHBoxLayout()
        file_ly.addWidget(self.file_edit)
        file_ly.addWidget(self.browse_btn)
        self.crush_bt = QPushButton('Crush', self)
        self.connect(self.crush_bt, SIGNAL('clicked()'), self.on_crush_button)
        file_ly.addWidget(self.crush_bt)
        self.load_bt = QPushButton('Load', self)
        self.connect(self.load_bt, SIGNAL('clicked()'), self.on_load_button)
        file_ly.addWidget(self.load_bt)

        self.result_ly = QTableWidget()
        self.result_ly.setColumnCount(4)
        column_width = [300, 200, 100, 100]
        for column in range(4):
            self.result_ly.setColumnWidth(column, column_width[column])
        headerlabels = ['file name', 'entity', 'count', '']
        self.result_ly.setHorizontalHeaderLabels(headerlabels)
        self.result_ly.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.result_ly.setSelectionBehavior(QAbstractItemView.SelectRows)

        # status bar
        self.status_bar = QStatusBar()
        self.status_bar.showMessage('Ready')

        v = QVBoxLayout()
        v.addLayout(ck_ly)
        v.addLayout(file_ly)
        v.addWidget(self.result_ly)
        v.addWidget(self.status_bar)
        self.setLayout(v)

    def closeEvent(self, event):
        pass
        # reply = QtGui.QMessageBox.question(self, 'Message',
        #                                    "Are you sure to quit?", QtGui.QMessageBox.Yes |
        #                                    QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        #
        # if reply == QtGui.QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_checkbox(self):
        checkbox = self.sender()
        entity_name = str(checkbox.text())
        if checkbox.isChecked():
            self.entities.append(entity_name)
            self.status_bar.showMessage('Check {0}.'.format(entity_name))
        else:
            self.entities.remove(entity_name)
            self.status_bar.showMessage('Uncheck {0}.'.format(entity_name))

    def on_browse_button(self):
        # absolute_path is a QString object
        absolute_path = QFileDialog.getOpenFileName(self, 'Open file',
                                                    '.', "XML files (*.xml)")
        if absolute_path:
            self.file_edit.setText(absolute_path)
            self.status_bar.showMessage('File {0} selected'.format(absolute_path))
        else:
            self.status_bar.showMessage('Went Error, Please select a file again.')

    def on_crush_button(self):
        self.status_bar.showMessage('Processing... This might take few minutes. Please wait.')
        file_path = str(self.file_edit.text())
        reader = Reader(file_path)
        xml_dict = reader.get_utility_by_name(self.entities)
        self.result_ly.setRowCount(len(xml_dict))
        row = 0
        for key, value in xml_dict.items():
            self.result_ly.setItem(row, 0, QTableWidgetItem(key.split('\\')[-1]))
            self.result_ly.setItem(row, 1, QTableWidgetItem(key.split('_')[-1].replace('.xml', '')))
            self.result_ly.setItem(row, 2, QTableWidgetItem(str(value)))
            self.open_btn = QPushButton('Open')
            self.open_btn.setProperty('path', key)
            self.connect(self.open_btn, SIGNAL('clicked()'), self.on_open_button)
            self.result_ly.setCellWidget(row, 3, self.open_btn)

            row += 1
        self.result_ly.show()
        self.status_bar.showMessage('{0}'.format(file_path))

    def on_load_button(self):
        self.status_bar.showMessage('Loading... This might take few seconds. Please wait.')
        file_name = os.path.basename(str(self.file_edit.text()))
        folder_path = str(self.file_edit.text()).rstrip('.xml')
        if os.path.exists(folder_path):
            f_list = [f for f in os.listdir(folder_path) if f.startswith(file_name.rstrip('.xml'))]
            self.result_ly.setRowCount(len(f_list))
            row = 0
            for f_name in f_list:
                self.result_ly.setItem(row, 0, QTableWidgetItem(f_name))
                self.result_ly.setItem(row, 1, QTableWidgetItem(f_name.split('_')[-1].rstrip('.xml')))
                reader = Reader(os.path.join(folder_path, f_name))
                self.result_ly.setItem(row, 2, QTableWidgetItem(str(reader.get_records_count())))
                self.open_btn = QPushButton('Open')
                self.open_btn.setProperty('path', os.path.join(folder_path, f_name))
                self.connect(self.open_btn, SIGNAL('clicked()'), self.on_open_button)
                self.result_ly.setCellWidget(row, 3, self.open_btn)

                row += 1
            self.result_ly.show()
            self.status_bar.showMessage('Load {0} completed.'.format(folder_path))
        else:
            self.status_bar.showMessage('Folder not exists. Click Crush button.')

    def on_open_button(self):
        # absolute_path is a QString object
        file_path = str(self.sender().property('path').toPyObject())
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


