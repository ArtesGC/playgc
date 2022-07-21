from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class PGC:
    def __init__(self):
        self.ferramentas = QWidget()
        self.ferramentas.setFixedSize(500, 300)
        self.ferramentas.setWindowTitle("PlayGC")
        self.ferramentas.setStyleSheet("QLabel{color: white;}")

        # ******* background-image *******
        bg_image = QImage(f"./favicon/bg.jpg").scaled(QSize(500, 300))
        palette = QPalette()
        palette.setBrush(palette.ColorGroup.All, palette.ColorRole.Window, QBrush(bg_image))
        self.ferramentas.setPalette(palette)

        self.mainpage()

    def mainpage(self):
        def procurar_video():
            pass

        def convert():
            pass

        layout = QFormLayout()
        layout.setSpacing(20)

        menu = QMenuBar()
        detalhes = menu.addMenu("Help")
        instr = detalhes.addAction("Instruction")
        sair = detalhes.addAction("Exit")
        sobre = menu.addAction("About")
        layout.setMenuBar(menu)

        introlabel = QLabel("<h1>Convert your Videos to Audio</h1><hr>")
        layout.addRow(introlabel)

        layoutvideo = QHBoxLayout()
        nomevideo = QLineEdit()
        nomevideo.setPlaceholderText("Please [type or paste] the location of the video..")
        nomevideo.setReadOnly(True)
        layoutvideo.addWidget(nomevideo)
        procvideo = QPushButton("Search Video")
        procvideo.clicked.connect(procurar_video)
        layoutvideo.addWidget(procvideo)
        layout.addRow(layoutvideo)

        convertbtn = QPushButton("Convert")
        convertbtn.clicked.connect(convert)
        layout.addRow(convertbtn)

        # copyright-label
        link = lambda: webbrowser.open_new('https://artesgc.home.blog')
        copyrightlabel = QLabel('<a style="text-decoration: none; background-color: none;" href="#">&trade;ArtesGC, Inc</a>')
        copyrightlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        copyrightlabel.linkActivated.connect(link)
        copyrightlabel.setToolTip("Open ArtesGC's oficial website!")

        barraferramentas = QToolBar("Copyright")
        barraferramentas.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        barraferramentas.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonFollowStyle)
        barraferramentas.addWidget(copyrightlabel)
        layout.addRow(barraferramentas)
        self.ferramentas.setLayout(layout)


'''
if __name__ == '__main__':
    gcApp = QApplication([])
    app = PGC()
    app.ferramentas.show()
    gcApp.exec()
'''
