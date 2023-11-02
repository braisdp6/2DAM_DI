import locale

import Conexion
import Eventos

locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
locale.setlocale(locale.LC_MONETARY, "es_ES.UTF-8")

from WindowAux import *


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        Var.ui = Ui_MainWindow()
        Var.ui.setupUi(self)  # encargado de generar la interfaz
        Var.calendar = Calendar()
        Var.ventanaSalir = VentanaSalir()
        Var.acercaDe = AcercaDe()
        Conexion.Conexion.conexion()
        Conexion.Conexion.cargaProv()
        Conexion.Conexion.mostrarDrivers()

        '''
        ejecucion de diferentes al ejecutar la aplicacion
        '''
        rbtDriver = [Var.ui.rbtTodos, Var.ui.rbtAlta, Var.ui.rbtBaja]
        for i in rbtDriver:
            i.toggled.connect(Eventos.Eventos.selHistorico)

        '''
        STATUS BAR
        '''
        # formateamos la fecha
        fechaActual = datetime.now()
        fechaFormateada = fechaActual.strftime('%A - %d/%m/%Y')

        # añadimos la fecha al status bar
        self.labelStatus = QtWidgets.QLabel(fechaFormateada, self)
        self.labelStatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        Var.ui.statusbar.addPermanentWidget(self.labelStatus, 1)

        # añadimos la version al status bar
        self.labelStatusVersion = QtWidgets.QLabel("Version: " + Var.version, self)
        self.labelStatusVersion.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        Var.ui.statusbar.addPermanentWidget(self.labelStatusVersion, 0)

        '''
        zona de eventos de tablas
        '''
        Eventos.Eventos.resizeTabDrivers(self)

        '''
        zona de eventos de comboBox
        '''
        Var.ui.cmbProvincia.currentIndexChanged.connect(Conexion.Conexion.selMuni)

        '''
        zona de eventos de botones
        '''
        Var.ui.btnCalendar.clicked.connect(Eventos.Eventos.abrirCalendar)
        Var.ui.btnAltaDriver.clicked.connect(Drivers.Drivers.altaDriver)

        '''
        zona de eventos del menubar
        '''
        Var.ui.actionBarSalir.triggered.connect(Eventos.Eventos.abrirVentanaSalir)
        Var.ui.actionAcercaDe.triggered.connect(Eventos.Eventos.abrirAcercaDe)

        '''
        zona de eventos de las cajas de texto
        '''
        Var.ui.txtDni.editingFinished.connect(Drivers.Drivers.validarDNI)
        Var.ui.txtMovil.editingFinished.connect(Drivers.Drivers.validarMovil)
        Var.ui.txtNombre.editingFinished.connect(Eventos.Eventos.formatCajaTexto)
        Var.ui.txtApel.editingFinished.connect(Eventos.Eventos.formatCajaTexto)
        Var.ui.txtSalario.editingFinished.connect(Eventos.Eventos.formatCajaTexto)

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
