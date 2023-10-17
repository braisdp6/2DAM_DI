import locale
from datetime import datetime

import Drivers
from VentanaCalendario import Ui_ventanaCalendario
from VentanaSalir import Ui_ventanaDeseaSalir
from MainWindow import *
import sys, Var, Eventos

from WindowAux import *

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
        Var.ui = Ui_MainWindow()
        Var.ui.setupUi(self)  # encargado de generar la interfaz
        Var.calendar = Calendar()
        Var.ventanaSalir = VentanaSalir()
        Eventos.Eventos.cargaProv(self)
        rbtDriver = [Var.ui.rbtTodos, Var.ui.rbtAlta, Var.ui.rbtBaja]
        for i in rbtDriver:
            i.toogled.connect(Eventos.Eventos.selEstado)

        '''
        ejecucion de diferentes al ejecutar la aplicacion
        '''


        '''
        STATUS BAR
        '''
        #formateamos la fecha
        fechaActual = datetime.now()
        fechaFormateada = fechaActual.strftime('%A - %d/%m/%Y')

        #añadimos la fecha al status bar
        self.labelStatus = QtWidgets.QLabel(fechaFormateada, self)
        self.labelStatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        Var.ui.statusbar.addPermanentWidget(self.labelStatus, 1)

        #añadimos la version al status bar
        self.labelStatusVersion = QtWidgets.QLabel("Version: " + Var.version, self)
        self.labelStatusVersion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        Var.ui.statusbar.addPermanentWidget(self.labelStatusVersion, 0)



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

    def closeEvent(self, event):
        mbox = QtWidgets.QMessageBox.information(self, "Salir", "¿Estás seguro de que quieres salir?",
                                                 QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

        if mbox == QtWidgets.QMessageBox.StandardButton.Yes:
            app.quit()
        if mbox == QtWidgets.QMessageBox.StandardButton.No:
            event.ignore()


if __name__ == "__main__":  # evita que haya dos funciones iguales que se lanzen
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())

