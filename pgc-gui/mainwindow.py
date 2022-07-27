from sys import exit
from time import time

import moviepy.editor as mp
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

theme = open('./theme/pgc.qss').read().strip()


class PGC:
    def __init__(self):
        # ******* global-variables *******
        self.nomevideo = None
        self.infolabel = None
        self.logtext = None
        self.locatevideo = None

        # ******* program-font *******
        QFontDatabase.addApplicationFont("./font/comingsoon.ttf")

        # ******* main-widget *******
        self.ferramentas = QWidget()
        self.ferramentas.setFixedSize(int(1920 / 3), int(1080 / 3))
        self.ferramentas.setWindowTitle("PlayGC")
        self.ferramentas.setWindowIcon(QIcon("./favicon/pgc_icon-256x256.ico"))
        self.ferramentas.setStyleSheet(theme)

        # ******* main-layout *******
        self.layout = QFormLayout()

        # ******* background-image *******
        bg_image = QImage(f"./favicon/bg.jpg").scaled(QSize(int(1920 / 3), int(1080 / 3)))
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
        self.layout.setMenuBar(menu)

        self.mainpage()
        self.ferramentas.setLayout(self.layout)

    def mainpage(self):
        def procurar_video():
            self.locatevideo = QFileDialog.getOpenFileName(self.ferramentas, caption='Select the Video file', filter='Video Files (*.mp4)')[0]
            self.nomevideo.setText(self.locatevideo)
            self.infolabel.setText('<strong><ul><li>Now hit the convert button and let the show begins!</ul></li></strong>')

        def convert():
            if self.nomevideo.text().isspace() or self.nomevideo.text() == "" or self.nomevideo.text() is None:
                QMessageBox.warning(self.ferramentas, "Warning", "Please, locate the video file before to proceed!")
            else:
                inicio = time()
                self.infolabel.setText("<strong><ul><li>Please wait, I'm trying to proccess your request... Done!</ul></li></strong>")
                try:
                    clip = mp.VideoFileClip(f"{self.locatevideo}")
                    clip.audio.write_audiofile(f"{self.locatevideo[:-3]}mp3", write_logfile=True)
                    logtext.setText(open(f"{self.locatevideo[:-3]}mp3.log").read())
                except Exception as error:
                    QMessageBox.critical(self.ferramentas, "Error", f"Am sorry, while converting your file the following error occured:\n\n{error}")
                finally:
                    QMessageBox.information(
                        self.ferramentas, "Successful", f"Operation Concluded in {int(time() - inicio)}s.\n\n"
                                                        f"The audio file was saved in the same location as the video, enjoy!"
                    )

        # ******* main-page *******
        introlabel = QLabel("<h1><i>Convert your Videos to Audio</i></h1><hr>")
        introlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        introlabel.setStyleSheet("color: white;")
        self.layout.addRow(introlabel)

        layoutvideo = QHBoxLayout()
        self.nomevideo = QLineEdit()
        self.nomevideo.setPlaceholderText("Please search to get the location of the video..")
        self.nomevideo.setReadOnly(True)
        layoutvideo.addWidget(self.nomevideo)

        procvideo = QPushButton("Search Video")
        procvideo.clicked.connect(procurar_video)
        layoutvideo.addWidget(procvideo)
        self.layout.addRow(layoutvideo)

        self.infolabel = QLabel("<strong><ul><li>Waiting for the video's name...</ul></li></strong>")
        self.infolabel.setStyleSheet('color: white')
        self.layout.addRow(self.infolabel)

        convertbtn = QPushButton("Convert")
        convertbtn.clicked.connect(convert)
        self.layout.addRow(convertbtn)

        self.logtext = QTextEdit()
        self.logtext.setPlaceholderText("The convertion log will be shown here..")
        self.logtext.setReadOnly(True)
        self.layout.addRow(self.logtext)

        # ******* copyright-label *******
        link = lambda: webbrowser.open_new('https://artesgc.home.blog')
        copyrightlabel = QLabel('<a style="text-decoration: none; color: white;" href="#">&trade;ArtesGC, Inc</a>')
        copyrightlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        copyrightlabel.linkActivated.connect(link)
        copyrightlabel.setToolTip("Open ArtesGC's oficial website!")
        self.layout.addRow(copyrightlabel)

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
