import sys
import MainWinSignalSlot

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = QMainWindow()
    ui = MainWinSignalSlot.Ui_MainWindow()
    #向主窗口上添加控件
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())

