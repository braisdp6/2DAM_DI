from datetime import datetime
from VentanaCalendario import Ui_ventanaCalendario
from VentanaSalir import Ui_ventanaDeseaSalir
from MainWindow import *
import sys
from container import Var, Drivers


class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        Var.calendar = Ui_ventanaCalendario()
        Var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year
        Var.calendar.calendario.setSelectedDate(QtCore.QDate(ano, mes, dia))
        Var.calendar.calendario.clicked.connect(Drivers.Drivers.cargaFecha)
class VentanaSalir(QtWidgets.QDialog):
    def __init__(self):
        super(VentanaSalir, self).__init__()
        Var.ventanaSalir = Ui_ventanaDeseaSalir()
        Var.ventanaSalir.setupUi(self)
        Var.ventanaSalir.btnAceptar.clicked.connect(self.on_btnAceptar_clicked)
        Var.ventanaSalir.btnCancelar.clicked.connect(self.on_btnCancelar_clicked)

    def on_btnAceptar_clicked(self):
        # Acción para el botón Aceptar
        sys.exit()

    def on_btnCancelar_clicked(self):
        # Acción para el botón Cancelar
        self.hide()
