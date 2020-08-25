import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from tools import Tools
from config import Config


class Setting(QDialog):

    def __init__(self):
        super(Setting, self).__init__()
        self.init_UI()

    def init_UI(self):
        # upload path
        h1_ly = QHBoxLayout()
        up_pth_1b = QLabel('Select output path:')
        self.up_pth_edit = QLineEdit()
        self.up_pth_edit.setText(Config.get_public_item('output_path'))
        self.browse_btn = QPushButton()
        self.browse_btn.setText("Browse")
        self.connect(self.browse_btn, SIGNAL("clicked()"), self.on_browse_button)
        h1_ly.addWidget(up_pth_1b)
        h1_ly.addWidget(self.up_pth_edit)
        h1_ly.addWidget(self.browse_btn)

        # Apply Cancel button
        btn_ly = QHBoxLayout()
        self.apply_btn = QPushButton()
        self.apply_btn.setText('Apply')
        self.connect(self.apply_btn, SIGNAL('clicked()'), self.on_apply_button)
        btn_ly.addStretch(1)
        btn_ly.addWidget(self.apply_btn)

        v = QVBoxLayout()
        v.addLayout(h1_ly)
        v.addLayout(btn_ly)
        self.setLayout(v)

    def on_browse_button(self):
        # absolute_path is a QString object
        absolute_path = QFileDialog.getExistingDirectory(self, 'Open a folder',
                                                    '.', QFileDialog.ShowDirsOnly)
        if absolute_path:
            self.up_pth_edit.setText(absolute_path)

    def on_apply_button(self):
        Config.set_public_item('output_path', str(self.up_pth_edit.text()))
        msg = QMessageBox()
        msg.setText('New config takes effect.')
        msg.setWindowTitle('Conifrm')
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

