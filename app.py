from fenetre_convertisseur import Ma_fenetre
from PySide2.QtWidgets import QApplication
import sys
from currency_converter import CurrencyConverter

app = QApplication(sys.argv)

window = Ma_fenetre()
window.show()

app.exec_()