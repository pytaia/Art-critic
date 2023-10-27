from data.elements import get_names
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPainter, QColor, QPen
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
import sys
from PyQt5 import uic


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('creat_room_ui.ui', self)
        res = get_names(1)
        for i in res:
            self.names_arts.addItem(i)
        self.x =
        #self.creat_btn.clicked.connect()

    def paintEvent(self, e):
        #v = int(300 * text2 / text1)

        painter = QPainter(self)
        painter.setPen(QColor(0, 0, 222))
        #painter.drawRect(10, 10, 300, v)
        painter.drawRect(50, 40, 300, 300)

        #painter = QPainter()
        #painter.begin(self)
        #painter.setPen(QPen(QtCore.Qt.red, 5, QtCore.Qt.SolidLine))
        #painter.drawLine(350, 50, 325, 50)
        #painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
