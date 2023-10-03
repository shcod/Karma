import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPainter, QPolygon, QColor
from PyQt5.QtCore import Qt, QTimer, QPoint, QRect
from PyQt5 import QtWidgets



class MyMainWindow(QtWidgets.QMainWindow):

    def __init__(self, app):
        super(MyMainWindow, self).__init__()

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Sancak Teknoloji Takımı")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.ucgen = QPolygon([QPoint(100, 500), QPoint(150, 400), QPoint(200, 500)])

        #oyunun akıcı olmasını sağlamak için oyun döngüsünü sürekli yeniden çizilmesini sağlayan animasyonların pürüssüzlüğünü sağlayan kod
        self.timer = QTimer(self)
        self.timer.start(16)  # 60 FPS

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing) #daha kaliteli bir görünüm
        painter.fillRect(self.centralWidget().rect(), Qt.white) #arkaplan rengi
        painter.setPen(QColor(0, 0, 0)) #üçgen kenarlarının beyaz olmasını sağlıyor
        painter.setBrush(QColor(0, 0, 255)) #üçgen iç rengi
        painter.drawPolygon(self.ucgen)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.ucgen.translate(-5, 0)
        elif event.key() == Qt.Key_Right:
            self.ucgen.translate(5, 0)
        elif event.key() == Qt.Key_Up:
            self.ucgen.translate(0, -5)
        elif event.key() == Qt.Key_Down:
            self.ucgen.translate(0, 5)

        self.update()


