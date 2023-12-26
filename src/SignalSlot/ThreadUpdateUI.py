'''

多线程更新UI数据(在两个线程中传数)

'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time
import sys

class BackenThread(QThread):
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currentTime = data.toString('yyyy-MM-dd hh:mm:ss')
            self.update_date.emit(str(currentTime))
            time.sleep(1)

class ThreadUpdateUI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('多线程更新UI数据')
        self.resize(400,100)
        self.input = QLineEdit(self)
        self.input.resize(400,100)

        self.initUI()

    def initUI(self):
        self.backend = BackenThread()
        self.backend.update_date.connect(self.handleDisplay)

        self.backend.start()

    def handleDisplay(self,data):
        self.input.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = ThreadUpdateUI()
    main.show()
    sys.exit(app.exec_())
