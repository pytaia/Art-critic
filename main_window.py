from data.elements import *
from graph import graph_art
import sys
from PyQt5 import uic
import pygame
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtWidgets


if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window_ui.ui', self)
        self.initUI()
        self.creat_art_btn.clicked.connect(self.creat_art)
        self.creat_room_btn.clicked.connect(self.creat_room)
        self.stat_btn.clicked.connect(self.stat_art)
        self.del_art_btn.clicked.connect(self.del_art)
        self.del_room_btn.clicked.connect(self.del_room)
        self.pushButton.clicked.connect(self.initUI)
        self.sim_btn.clicked.connect(self.sim)

    def initUI(self):
        res = get_names()
        self.name_art.clear()
        self.room.clear()
        for i in res:
            self.name_art.addItem(i)
        res = get_numbers_rooms()
        for i in res:
            self.room.addItem(i)

    def creat_art(self):
        self.add_art = CreatArt(self)
        self.add_art.show()

    def sim(self):
        # pygame
        pass

    def creat_room(self):
        # pygame
        pass

    def stat_art(self):
        self.stat = StatArt(self, self.name_art.currentText())
        self.stat.show()

    def del_art(self):
        delete_art(get_individual_number(self.name_art.currentText()))
        self.initUI()

    def del_room(self):
        delete_room(self.room.currentText())
        self.initUI()


class CreatArt(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.args = args[-1]
        uic.loadUi('creat_art_ui.ui', self)
        self.creat_btn.clicked.connect(self.creat)

    def creat(self):
        res = [self.hall_line.text(), self.author_line.text(), self.name_line.text(),
               self.style_line.text(), self.x_line.text(), self.year_line.text()]
        if '' not in res and res[4].isdigit() and res[0].isdigit():
            create_art(*res)
            self.close()
        else:
            self.name_line.setText('Некорректный ввод.')


class StatArt(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.args = args[-1]
        uic.loadUi('stat_art_ui.ui', self)
        self.initUI(self.args)

    def initUI(self, args):
        res = return_information(get_individual_number(args))
        self.id_line.setText(res['individual_number'])
        self.name_line.setText(res['name'])
        self.author_line.setText(res['author'])
        self.year_line.setText(res['year_of_creation'])
        self.style_line.setText(res['style'])
        self.hall_line.setText(res['hall_number'])
        graph_art(res['individual_number'])
        self.pixmap = QPixmap('chart.png')
        self.image.move(10, 10)
        self.image.resize(384, 288)
        self.image.setPixmap(self.pixmap)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())