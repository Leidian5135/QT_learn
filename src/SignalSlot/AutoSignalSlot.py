'''
信号与槽自动连接

'''

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import sys

class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot, self).__init__()
        self.okButton = QPushButton('ok',self)
        self.okButton.setObjectName('okButton')
        self.okButton1 = QPushButton('cancel',self)
        #自动绑定槽函数方法，名字要一样
        self.okButton1.setObjectName('cancelButton')

        layout = QHBoxLayout()
        layout.addWidget(self.okButton)
        self.setLayout(layout)
        #连接方法
        QtCore.QMetaObject.connectSlotsByName(self)
        # self.okButton.clicked.connect(self.on_okButton_clicked)


    #标注为槽
    @QtCore.pyqtSlot()
    def on_okButton_clicked(self):
        print('点击了OK按钮')

    # 标注为槽
    @QtCore.pyqtSlot()
    def on_cancelButton_clicked(self):
        print('点击了cancel按钮')



if __name__ =='__main__':
    app = QApplication(sys.argv)
    example = AutoSignalSlot()
    example.show()
    sys.exit(app.exec_())
