from subprocess import getoutput
from time import sleep, time

import moviepy.editor as mp
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

theme = open('./theme/pgc.qss').read().strip()


class PGC:
    def __init__(self):
        self.locatevideo = None

        QFontDatabase.addApplicationFont("./font/comingsoon.ttf")

        self.ferramentas = QWidget()
        self.ferramentas.setFixedSize(int(1920/3), int(1080/3))
        self.ferramentas.setWindowTitle("PlayGC")
        self.ferramentas.setWindowIcon(QIcon("./favicon/pgc_icon-256x256.ico"))
        self.ferramentas.setStyleSheet(theme)

        # ******* background-image *******
        bg_image = QImage(f"./favicon/bg.jpg").scaled(QSize(int(1920/3), int(1080/3)))
        palette = QPalette()
        palette.setBrush(palette.ColorGroup.All, palette.ColorRole.Window, QBrush(bg_image))
        self.ferramentas.setPalette(palette)

        self.mainpage()

    def mainpage(self):
        def procurar_video():
            self.locatevideo = QFileDialog.getOpenFileName(self.ferramentas, caption='Select the Video file', filter='Video Files (*.mp4)')[0]
            nomevideo.setText(self.locatevideo)
            infolabel.setText('<strong><ul><li>Now hit the convert button and let the show begins!</ul></li></strong>')

        def convert():
            if nomevideo.text().isspace() or nomevideo.text() == "" or nomevideo.text() is None:
                QMessageBox.warning(self.ferramentas, "Warning", "Please, locate the video file before to proceed!")
            else:
                inicio = time()
                infolabel.setText("<strong><ul><li>Please wait, I'm trying to proccess your request... Done!</ul></li></strong>")
                try:
                    clip = mp.VideoFileClip(f"{self.locatevideo}")
                    clip.audio.write_audiofile(f"{self.locatevideo[:-3]}mp3", write_logfile=True)
                    logtext.setText(open(f"{self.locatevideo[:-3]}mp3.log").read())
                    sleep(2.0)
                except Exception as error:
                    QMessageBox.critical(self.ferramentas, "Error", f"Am sorry, while converting your file the following error occured:\n\n{error}")
                QMessageBox.information(self.ferramentas, "Successful", f"Operation Concluded in {int(time() - inicio)}s.\n\n"
                                                                        f"The audio file was saved in the same location as the video, enjoy!")

        layoutvideo = QHBoxLayout()
        layout = QFormLayout()

        menu = QMenuBar()
        detalhes = menu.addMenu("Help")
        instr = detalhes.addAction("Instruction")
        sair = detalhes.addAction("Exit")
        sobre = menu.addAction("About")
        layout.setMenuBar(menu)

        introlabel = QLabel("<h1><i>Convert your Videos to Audio</i></h1><hr>")
        introlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        introlabel.setStyleSheet("color: white;")
        layout.addRow(introlabel)

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

        # copyright-label
        link = lambda: webbrowser.open_new('https://artesgc.home.blog')
        copyrightlabel = QLabel('<a style="text-decoration: none; color: white;" href="#">&trade;ArtesGC, Inc</a>')
        copyrightlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        copyrightlabel.linkActivated.connect(link)
        copyrightlabel.setToolTip("Open ArtesGC's oficial website!")
        layout.addRow(copyrightlabel)

        self.ferramentas.setLayout(layout)
