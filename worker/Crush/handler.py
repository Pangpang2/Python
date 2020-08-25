import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from tabs import Crush, Fetch, Setting


class Handler(QTabWidget):

    def __init__(self):
        super(Handler, self).__init__()
        self.crush = Crush()
        self.fetch = Fetch()
        self.setting = Setting()
        self.addTab(self.crush, 'Crush')
        self.addTab(self.fetch, 'Fetch')
        self.addTab(self.setting, 'Setting')
        self.setWindowTitle('UDBF Processor')



def main():

    app = QApplication(sys.argv)
    ex = Handler()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()