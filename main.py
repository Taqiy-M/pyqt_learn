

from PyQt5.QtWidgets import QPushButton, QLabel, QLineEdit, QTextEdit, QApplication
ilova = QApplication([])
a = QPushButton("Meni Bos!")
a.setFixedSize(600, 600)
b = QLabel("Bu shunchaki oddiy yozuv!!")
b.setFixedSize(400, 300)
a.show()
b.show()
ilova.exec()
