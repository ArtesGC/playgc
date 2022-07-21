from random import randint
from sys import argv, exit
from time import sleep

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class PGCINIT:
    def __init__(self):
        self.gc = QApplication(argv)

        # application font
        QFontDatabase.addApplicationFont("./font/lemon.ttf")

        img = QPixmap("./favicon/init.png")
        self.align = int(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignAbsolute)
        self.color = Qt.GlobalColor.white
        self.janela = QSplashScreen(img)
        self.janela.setStyleSheet(
            'font-family: "Lemon";'
            'font-size: 11pt;'
        )
        self.janela.show()
        self.iniciar()

    def iniciar(self):
        load = 0
        while load < 100:
            self.janela.showMessage(f"Loading Package: {load}%", self.align, self.color)
            sleep(0.3)
            load += randint(5, 10)
        self.janela.close()
        app = PGC()


class PGC:
    def __init__(self):
        theme = open('./theme/pgc.qss').read().strip()

        self.ferramentas = QWidget()
        self.ferramentas.setFixedSize(500, 300)
        self.ferramentas.setWindowTitle("PlayGC")
        '''self.ferramentas.setStyleSheet("""
background-image: url("./favicon/bg.jpg");
background-repeat: no-repeat;
background-size: auto;
background-attachment: fixed;
background-position: center;
""")'''

        # ******* background-image *******
        bg_image = QImage(f"./favicon/bg.jpg").scaled(QSize(500, 300))
        palette = QPalette()
        palette.setBrush(palette.ColorGroup.All, palette.ColorRole.Window, QBrush(bg_image))
        self.ferramentas.setPalette(palette)

        self.layout = QFormLayout()
        self.layout.setSpacing(20)

        menu = QMenuBar()
        detalhes = menu.addMenu("Help")
        instr = detalhes.addAction("Instruction")
        sair = detalhes.addAction("Exit")
        sobre = menu.addAction("About")
        self.layout.setMenuBar(menu)

        introlabel = QLabel("<h1>Convert your Videos to Audio</h1><hr>")
        self.layout.addRow(introlabel)

        videolayout = QHBoxLayout()
        self.nomevideo = QLineEdit()
        self.nomevideo.setReadOnly(True)
        videolayout.addWidget(self.nomevideo)
        procvideo = QPushButton("Search Video")
        procvideo.clicked.connect(self.procurar_video)
        videolayout.addWidget(procvideo)
        self.layout.addChildLayout(videolayout)

        convertbtn = QPushButton("Convert")
        convertbtn.clicked.connect(self.convert)
        self.layout.addRow(convertbtn)

        # copyright-label
        link = lambda: webbrowser.open_new('https://artesgc.home.blog')
        copyrightlabel = QLabel('<a style="text-decoration: none; background-color: none;" href="#">&trade;ArtesGC, Inc</a>')
        copyrightlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        copyrightlabel.linkActivated.connect(link)
        copyrightlabel.setToolTip("Open ArtesGC's oficial website!")

        barramenu = QToolBar("Copyright")
        barramenu.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        barramenu.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonFollowStyle)
        barramenu.addWidget(copyrightlabel)
        self.layout.addRow(barramenu)
        self.ferramentas.show()

    def procurar_video(self):
        pass

    def convert(self):
        pass


if __name__ == '__main__':
    pgcApp = PGCINIT()
    pgcApp.gc.exec()
