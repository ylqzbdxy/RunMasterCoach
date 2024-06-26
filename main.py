from PyQt5.QtWidgets import QApplication
from model.my_window_lite import myWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myWindow()
    w.show()
    sys.exit(app.exec_())
