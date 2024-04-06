from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QTextEdit, QApplication


ilova = QApplication([])

lbl = QPushButton("Bu Shunchaki Yozuv!!")
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

lbl.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
lbl.show()
ilova.exec()





