from PySide2 import QtWidgets, QtGui
from currency_converter import CurrencyConverter


class Ma_fenetre(QtWidgets.QWidget):
    c = CurrencyConverter()
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        
        self.create_widgets()
        self.add_widgets_to_layout()
        self.customise_widgets()
        self.setup_connections()
        self.load_default_values()
        self.compute()
        self.inverser_devises()
        
    
    def create_widgets(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.cbb_devise_from= QtWidgets.QComboBox()
        self.cbb_devise_to= QtWidgets.QComboBox()
        self.spn_montant= QtWidgets.QSpinBox()
        self.spn_montant_converti = QtWidgets.QSpinBox()
        self.btn_inverser= QtWidgets.QPushButton()
        self.text = QtWidgets.QLabel("Convertisseur de devise by Lucas")
           
    def add_widgets_to_layout(self):
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.cbb_devise_from)
        self.layout.addWidget(self.spn_montant)
        self.layout.addWidget(self.cbb_devise_to)
        self.layout.addWidget(self.spn_montant_converti)
        self.layout.addWidget(self.btn_inverser)

    def customise_widgets(self):
        self.setWindowTitle("Convertisseur de devise")
        self.btn_inverser.setText("Inverser les devises")
        self.setStyleSheet('background-color: #A3B0B7;')


    def setup_connections(self):
        self.btn_inverser.clicked.connect(self.inverser_devises)
        self.spn_montant_converti.valueChanged.connect(self.compute)
        self.spn_montant.valueChanged.connect(self.compute)
        self.cbb_devise_from.activated.connect(self.compute)
        self.cbb_devise_to.activated.connect(self.compute)

    def load_default_values(self):
        devises = list(self.c.currencies)
        self.cbb_devise_from.addItems(devises)
        self.cbb_devise_to.addItems(devises)
        self.cbb_devise_from.setCurrentText('EUR')
        self.cbb_devise_to.setCurrentText("USD")
        self.spn_montant.setRange(0,100000)
        self.spn_montant_converti.setRange(0,100000)
        self.spn_montant.setValue(100)
        self.spn_montant_converti.setValue(100)

    def compute(self):
        devise_from= self.cbb_devise_from.currentText()
        devise_to= self.cbb_devise_to.currentText()
        montant_a_convertir = self.spn_montant.value()
        resultat = self.c.convert(montant_a_convertir,devise_from,devise_to)
        self.spn_montant_converti.setValue(resultat)
    

    def inverser_devises(self):
        ex_dev_dep = self.cbb_devise_from.currentText()
        self.cbb_devise_from.setCurrentText(self.cbb_devise_to.currentText())
        self.cbb_devise_to.setCurrentText(ex_dev_dep)
        self.compute()
    
    