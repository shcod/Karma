import sys

from PyQt5.QtWidgets import QApplication

from main import MyMainWindow

def main():
    app = QApplication(sys.argv)
    #app.setStyle('fusion')
    #app.setStyleSheet(open("style.qss").read())
    main = MyMainWindow(app)
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
