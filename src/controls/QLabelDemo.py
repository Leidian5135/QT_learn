'''
QLabel常用的信号（事件）:
1. 当鼠标滑过QLabel控件时触发:linkHovered
2. 当鼠标单击QLabel控件时触发:linkActivated
'''

import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QLabel, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QPalette,QPixmap
from PyQt5.QtCore import Qt

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText('<font color=yellow>这是一个文本标签</font>')
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.yellow)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)

        label3.setToolTip('这是一个图片标签')

        label3.setPixmap(QPixmap('./images/python.jpg'))
        label4.setOpenExternalLinks(True)
        label4.setText('<a href="https://www.baidu.com">百度一下')

        label4.setAlignment(Qt.AlignCenter)

        label4.setToolTip('这是一个图片标签')

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)

        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')


    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    def linkClicked(self):
        print('当鼠标单机label4标签时，触发事件')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())
