import sys
import MainWinHori

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create a QMainWindow object
    mainWindow = QMainWindow()

    # Create a Ui_MainWindow object
    ui = MainWinHori.Ui_MainWindow()

    # Setup the UI
    ui.setupUi(mainWindow)

    # Show the window
    mainWindow.show()

    # Start the application
    sys.exit(app.exec_())
