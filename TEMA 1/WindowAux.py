from datetime import datetime

from AcercaDe import Ui_ventanaAcercaDe
from VentanaCalendario import Ui_ventanaCalendario
from VentanaSalir import Ui_ventanaDeseaSalir
from MainWindow import *
import sys
import Var
import Drivers


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


class AcercaDe(QtWidgets.QDialog):
    def __init__(self):
        super(AcercaDe, self).__init__()
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year

        Var.acercaDe = Ui_ventanaAcercaDe()
        Var.acercaDe.setupUi(self)
        Var.acercaDe.btnAceptar.clicked.connect(self.on_btnAceptar_clicked)
        Var.acercaDe.lblVersion.setText("Version: " + Var.version)
        Var.acercaDe.lblFecha.setText(str(dia) + "/" + str(mes) + "/" + str(ano) + " - Brais Dominguez Puga")

    def on_btnAceptar_clicked(self):
        # Acción para el botón Aceptar
        self.hide()

# Nota: cogemos la ventana de abrir de windows
class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDialogAbrir, self).__init__()
