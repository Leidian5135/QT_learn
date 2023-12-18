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
        # Create labels
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        # Set text of label1
        label1.setText('<font color=yellow>这是一个文本标签</font>')
        # Set background color of label1
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.yellow)
        label1.setPalette(palette)
        # Set alignment of label1
        label1.setAlignment(Qt.AlignCenter)

        # Set text of label2
        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        # Set alignment of label3
        label3.setAlignment(Qt.AlignCenter)

        # Set tooltip of label3
        label3.setToolTip('这是一个图片标签')

        # Set pixmap of label3
        label3.setPixmap(QPixmap('./images/python.jpg'))
        # Set openExternalLinks of label4,如果设置为True，则点击标签时会打开链接
        label4.setOpenExternalLinks(True)
        # Set text of label4
        label4.setText('<a href="https://www.baidu.com">百度一下')

        # Set alignment of label4
        label4.setAlignment(Qt.AlignCenter)

        # Set tooltip of label4
        label4.setToolTip('这是一个图片标签')

        # Create a vertical box layout
        vbox = QVBoxLayout()

        # Add labels to the box layout
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        # Connect the linkHovered signal to the linkHovered function
        label2.linkHovered.connect(self.linkHovered)

        # Connect the linkActivated signal to the linkClicked function
        label4.linkActivated.connect(self.linkClicked)

        # Set the layout of the window
        self.setLayout(vbox)
        # Set the title of the window
        self.setWindowTitle('QLabel控件演示')


    # Function to be called when the mouse is hovering over label2
    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    # Function to be called when the mouse is clicked on label4
    def linkClicked(self):
        print('当鼠标单机label4标签时，触发事件')

if __name__ == '__main__':
    # Create an application instance
    app = QApplication(sys.argv)
    # Create an instance of the QLabelDemo class
    main = QLabelDemo()
    # Show the window
    main.show()
    # Exit the application
    sys.exit(app.exec_())
