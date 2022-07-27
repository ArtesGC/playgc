from random import randint
from sys import argv
from time import sleep

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from mainwindow import PGC


class PGCINIT:
    def __init__(self):
        QFontDatabase.addApplicationFont("./font/comingsoon.ttf")

        img = QPixmap("./favicon/bg.jpg").scaled(int(1920/2), int(1080/2))
        self.align = int(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignAbsolute)
        self.janela = QSplashScreen(img)
        self.janela.show()
        self.iniciar()

    def iniciar(self):
        load = 0
        while load < 100:
            self.janela.showMessage(f"<h1>PlayGC</h1><hr>"
                                    f"<h2><i>Video to Audio Converter</i></h2>"
                                    f"<p>Loading Packages: {load}%</p>", self.align)
            sleep(0.2)
            load += randint(1, 10)
        self.janela.close()
        app = PGC()
        app.ferramentas.show()


if __name__ == '__main__':
    theme = open('theme/pgc.qss').read().strip()
    gcApp = QApplication(argv)
    pgcApp = PGCINIT()
    gcApp.exec()
