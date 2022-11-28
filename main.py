import webbrowser
from sys import exit, argv
from time import time
from random import randint
from time import sleep

import moviepy.editor as mp
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


def initwindow():
    def iniciar():
        load = 0
        while load < 100:
            janela.showMessage(f"<h1><i>Video to Audio Converter</i></h1>"
                               f"<p>Loading Packages: {load}%</p>", align)
            sleep(0.2)
            load += randint(1, 10)
        janela.close()
        app = PGC()
        app.ferramentas.show()

    # ******* program-font *******
    QFontDatabase.addApplicationFont("./font/comingsoon.ttf")

    img = QPixmap("./favicon/favicon-512x512.png")
    align = int(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignAbsolute)
    janela = QSplashScreen(img)
    janela.show()
    iniciar()


class PGC:
    def __init__(self):
        # ******* global-variables *******
        self.locatevideo = None

        # ******* main-widget *******
        self.ferramentas = QMainWindow()
        self.ferramentas.setFixedSize(int(1920/2), int(1080/2))
        self.ferramentas.setWindowTitle("PlayGC")
        self.ferramentas.setWindowIcon(QIcon("favicon/favicon-256x256.ico"))
        self.ferramentas.setStyleSheet(theme)

        # ******* background-image *******
        bg_image = QImage(f"./favicon/bg.jpg").scaled(QSize(int(1920/2), int(1080/2)))
        palette = QPalette()
        palette.setBrush(palette.ColorGroup.All, palette.ColorRole.Window, QBrush(bg_image))
        self.ferramentas.setPalette(palette)

        # ******* menu-bar *******
        menu = QMenuBar()
        detalhes = menu.addMenu("Help")
        instr = detalhes.addAction("Instruction")
        _sair = lambda: exit(0)
        sair = detalhes.addAction("Exit")
        sair.triggered.connect(_sair)
        sobre = menu.addAction("About")
        sobre.triggered.connect(self._sobre)

        self.ferramentas.setMenuBar(menu)
        self.mainpage()

    def mainpage(self):
        def procurar_video():
            self.locatevideo = QFileDialog.getOpenFileName(self.ferramentas, caption='Select the Video file',
                                                           filter='Video Files (*.mp4)')[0]
            nomevideo.setText(self.locatevideo)
            if self.locatevideo.isspace() or self.locatevideo == "":
                infolabel.setText("<strong><ul><li>File not found or process canceled!</ul></li></strong>")
            infolabel.setText(
                '<strong><ul><li>Now hit the convert button and let the show begins!</ul></li></strong>')

        def convert():
            if nomevideo.text().isspace() or nomevideo.text() == "" or nomevideo is None:
                QMessageBox.warning(self.ferramentas, "Warning", "Please, locate the video file before to proceed!")
            else:
                inicio = time()
                infolabel.setText(
                    "<strong><ul><li>Please wait, I'm trying to proccess your request...</ul></li></strong>")
                try:
                    clip = mp.VideoFileClip(f"{self.locatevideo}")
                    clip.audio.write_audiofile(f"{self.locatevideo[:-3]}mp3", write_logfile=True)
                    logtext.setText(open(f"{self.locatevideo[:-3]}mp3.log").read())
                except Exception as error:
                    QMessageBox.critical(self.ferramentas, "Error",
                                         f"Am sorry, while converting your file the following error occured:\n{error}")
                finally:
                    infolabel.setText("<strong><ul><li>Done!</ul></li></strong>")
                    QMessageBox.information(
                        self.ferramentas, "Successful",
                        f"Operation Concluded in {int(time() - inicio)}s.\n\n"
                        f"The audio file was saved in the same location as the video, enjoy!"
                    )

        janela = QWidget()
        layout = QFormLayout()

        # ******* main-page *******
        introlabel = QLabel("<h1>PlayGC</h1><hr><i>Convert your Videos to Audio</i>")
        introlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        introlabel.setStyleSheet("color: white;")
        layout.addRow(introlabel)

        layoutvideo = QHBoxLayout()
        nomevideo = QLineEdit()
        nomevideo.setPlaceholderText("Please search to get the location of the video..")
        nomevideo.setReadOnly(True)
        layoutvideo.addWidget(nomevideo)

        procvideo = QPushButton("Search Video")
        procvideo.clicked.connect(procurar_video)
        layoutvideo.addWidget(procvideo)
        layout.addRow(layoutvideo)

        infolabel = QLabel("<strong><ul><li>Waiting for the video's name...</ul></li></strong>")
        infolabel.setStyleSheet('color: white')
        layout.addRow(infolabel)

        convertbtn = QPushButton("Convert")
        convertbtn.clicked.connect(convert)
        layout.addRow(convertbtn)

        logtext = QTextEdit()
        logtext.setPlaceholderText("The convertion log will be shown here..")
        logtext.setReadOnly(True)
        layout.addRow(logtext)

        # ******* copyright-label *******
        link = lambda: webbrowser.open_new('https://artesgc.home.blog')
        copyrightlabel = QLabel('<a style="text-decoration: none; color: white;" href="#">&trade;ArtesGC, Inc</a>')
        copyrightlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        copyrightlabel.linkActivated.connect(link)
        copyrightlabel.setToolTip("Open ArtesGC's oficial website!")
        layout.addRow(copyrightlabel)
        janela.setLayout(layout)
        self.ferramentas.setCentralWidget(janela)

    def _sobre(self):
        QMessageBox.information(
            self.ferramentas,
            "About",
            "<h2>Information about the Program</h2><hr>"
            "<p><ul><li><b>Name</b>: PlayGC</li>"
            "<li><b>Version</b>: 0.1-072022</li>"
            "<li><b>Programmer & Design</b>: Nurul-GC</li>"
            "<li><b>Company</b>: ArtesGC Inc</li></ul></p>"
        )

    def _instr(self):
        QMessageBox.information(self.ferramentas, )


if __name__ == '__main__':
    theme = open('theme/pgc.qss').read().strip()
    gcApp = QApplication(argv)
    initwindow()
    gcApp.exec()
