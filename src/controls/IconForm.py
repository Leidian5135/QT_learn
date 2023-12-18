import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


class IconForm(QMainWindow):
    def __init__(self, parent=None):
        super(IconForm, self).__init__(parent)
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 400, 300)
        #设置主窗口的标题
        self.setWindowTitle('设置窗口图标')

        #设置窗口图标
        self.setWindowIcon(QIcon('./images/python.png'))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/python.png"))
    main = IconForm()
    main.show()
    sys.exit(app.exec_())
