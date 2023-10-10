from datetime import datetime

import Drivers
from VentanaCalendario import Ui_ventanaCalendario
from VentanaSalir import Ui_ventanaDeseaSalir
from MainWindow import *
import sys,Var,Eventos

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

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        Var.ui = Ui_MainWindow()
        Var.ui.setupUi(self) # encargado de generar la interfaz
        Var.calendar = Calendar()
        Var.ventanaSalir = VentanaSalir()


        '''
        zona de eventos de botones
        '''
        Var.ui.btnCalendar.clicked.connect(Eventos.Eventos.abrirCalendar)
        '''
        zona de eventos del menubar
        '''
        Var.ui.actionSalir.triggered.connect(Eventos.Eventos.abrirVentanaSalir)
        '''
        zona de eventos de las cajas de texto
        '''
        Var.ui.txtDni.editingFinished.connect(Drivers.Drivers.validarDNI)
        '''
        zona de eventos del toolbar
        '''
        Var.ui.actionBarSalir.triggered.connect(Eventos.Eventos.abrirVentanaSalir)
        Var.ui.actionLimpiarPanel.triggered.connect(Drivers.Drivers.limpiarPanel)

if __name__ == "__main__": # evita que haya dos funciones iguales que se lanzen
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())
