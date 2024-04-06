from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QPushButton, QLabel, \
    QLineEdit, QTextEdit, QApplication, QCheckBox, QComboBox, QRadioButton, QMainWindow

ilova = QApplication([])

class Oyna(QMainWindow):
    def __init__(self):
        super().__init__()
        self.le = QTextEdit()
        self.le.setPlaceholderText("enter your name")
        self.le.textChanged.connect(self.le_changed)
        self.setCentralWidget(self.le)

    def le_changed(self):
        print(self.le.toPlainText())

        # self.btn = QPushButton("Click")
        # self.btn.clicked.connect(self.btn_clicked)
        # self.btn.setStyleSheet("font-size:45px;")
        # self.btn.setFixedSize(400, 260)
        # self.setCentralWidget(self.btn)
        # self.c = 0
    # def btn_clicked(self):
        # self.c += 1
        # self.btn.setText(f"{self.c}")
        # self.btn.setEnabled(False)

# a = QComboBox()
# a.addItems(["O'zbekiston", "Qirg'iziston", "Ozarbayjon", "Turkmaniston"])
a = QRadioButton()
b = QPushButton("Bos")
a.show()
b.show()
def bosildi():
    a.setAutoExclusive(False)
    a.setChecked(False)
    a.setAutoExclusive(True)
b.clicked.connect(bosildi)

# a = Oyna()
# a.show()
ilova.exec()



























# a = QComboBox()
# a.setPlaceholderText("Mamlakat tanlang!")
# a.addItems(['salom', 'alik', "O'zbekiston", "Qirg'iziston", "Ozarbayjon"])
# a.addItem("Turkiya")
# a.show()
# a = QCheckBox(" Salomat")
# a.setStyleSheet("font-size: 40px;")
# a.show()
# a = QLineEdit()
# a.setPlaceholderText("Login")
# a.setStyleSheet("font-size:40px;")
# a.show()

# lbl = QPushButton("Bu Shunchaki Yozuv!!")
# lbl.setStyleSheet("""
#                         QPushButton {
#                             background-color: red;
#                             font-size: 40px;
#                         }
#
#                         QPushButton:hover {
#                             background-color: black;
#                             font-size: 50px;
#                             color: white;
#                         }
#
#                         QPushButton:pressed {
#                             background-color: white;
#                             color: black;
#                             font-size: 50px;
#                         }
# """)
# lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
# lbl.show()

# ilova.exec()









