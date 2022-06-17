# main
import sys 
from PyQt5.QtWidgets import QApplication
from MDCinemaSystem import MDCSystem

app = QApplication(sys.argv)

cinema  = MDCSystem()

sys.exit(app.exec())




