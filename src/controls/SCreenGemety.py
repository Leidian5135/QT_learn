import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QLineEdit, QMessageBox


def onClick_Button():
    print("按钮被点击了")
    print('1')
    print('widget.x() = %d' % widget.x())
    print('widget.y() = %d' % widget.y())
    print('widget.width() = %d' % widget.width())
    print('widget.height() = %d' % widget.height())

    print('2')
    print('widget.geometry().x()' % widget.geometry().x())
    print('widget.geometry().y()' % widget.geometry().y())
    print('widget.geometry().width()' % widget.geometry().width())
    print('widget.geometry().height()' % widget.geometry().height())


app = QApplication(sys.argv)

widget = QWidget()
btn = QPushButton(widget)
btn.setText("按钮")
btn.clicked.connect(onClick_Button)

btn.move(24, 52)

widget.resize(300, 240) #设置工作区的尺寸

widget.move(250, 200)

widget.setWindowTitle('屏幕坐标系')

widget.show()
sys.exit(app.exec_())

btn.clicked.connect(onClick_Button)
