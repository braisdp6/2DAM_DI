import locale

import Clientes
import Conexion
import Eventos

# Establecer la configuración regional en español
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
locale.setlocale(locale.LC_MONETARY, "es_ES.UTF-8")

from WindowAux import *


# TODO ALL:
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        Var.ui = Ui_MainWindow()
        Var.ui.setupUi(self)  # encargado de generar la interfaz
        Var.calendarAlta = CalendarAlta()  # Nota: instancia de la clase "calendar"
        Var.calendarBaja = CalendarBaja()  # Nota: instancia de la clase "calendar"
        Var.acercaDe = AcercaDe()  # Nota: instancia de la clase "acercaDe"
        Var.dlgAbrir = FileDialogAbrir()
        Conexion.Conexion.conexion()
        Conexion.Conexion.cargaProv()
        Conexion.Conexion.cargaProvCli() # EXAMEN

        estado = 1
        Conexion.Conexion.selectDrivers(estado)  # funcionamiento mostrar Histórico
        Conexion.Conexion.selectClientes(estado)  # EXAMEN
        '''
        STATUS BAR      NOTA: parte de abajo de la ventana
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
        Var.ui.tabDrivers.clicked.connect(
            Drivers.Drivers.cargaDriver)  # nota: Metodo para cargar driver en la tabla cuando se haga click en el "tabDriver"

        '''
        zona de eventos de comboBox       NOTA: sirve para que cargue los datos en el comboBox
        '''
        Var.ui.cmbProvincia.currentIndexChanged.connect(Conexion.Conexion.selMuni)
        Var.ui.rbtGroup.buttonClicked.connect(Drivers.Drivers.selEstado)

        '''
        zona de eventos de botones
        '''
        Var.ui.btnCalendarAlta.clicked.connect(Eventos.Eventos.abrirCalendarAlta)
        Var.ui.btnCalendarBaja.clicked.connect(Eventos.Eventos.abrirCalendarBaja)
        Var.ui.btnAltaDriver.clicked.connect(Drivers.Drivers.altaDriver)
        Var.ui.btnBuscarDni.clicked.connect(Drivers.Drivers.buscarDriverLupa)
        Var.ui.btnModificarDriver.clicked.connect(Drivers.Drivers.modifDri)  # NOTA: metodo modificar driver
        Var.ui.btnBajaDriver.clicked.connect(Drivers.Drivers.borraDriv)  # nota: metodo borrar driver

        '''
        zona de eventos de las cajas de texto
        '''
        Var.ui.txtDni.editingFinished.connect(lambda: Drivers.Drivers.validarDNI(Var.ui.txtDni.displayText()))
        Var.ui.txtMovil.editingFinished.connect(Drivers.Drivers.validarMovil)
        Var.ui.txtNombre.editingFinished.connect(Eventos.Eventos.formatCajaTexto)
        Var.ui.txtApel.editingFinished.connect(Eventos.Eventos.formatCajaTexto)
        Var.ui.txtSalario.editingFinished.connect(Eventos.Eventos.formatCajaTexto)
        Var.ui.txtDireccion.editingFinished.connect(Eventos.Eventos.formatCajaTexto)

        '''
        zona de eventos del menubar  NOTA: parte de arriba de la ventana donde hay desplegables (Archivo, Herramientas, Ayuda...)
        '''
        Var.ui.actionBarSalir.triggered.connect(Eventos.Eventos.abrirVentanaSalir)
        Var.ui.actionAcercaDe.triggered.connect(Eventos.Eventos.abrirAcercaDe)
        Var.ui.actionCrear_Copia_Seguridad.triggered.connect(Eventos.Eventos.crearBackup)
        Var.ui.actionRestaurar_Copia_Seguridad.triggered.connect(Eventos.Eventos.restaurarBackup)
        Var.ui.actionExportar_Datos_XLS.triggered.connect(Eventos.Eventos.exportarDatosXLS)
        Var.ui.actionImportar_Datos_XLS.triggered.connect(Eventos.Eventos.importarDatosXLS)

        '''
        zona de eventos del toolbar   NOTA: parte de arriba de la ventana donde estan los iconos ejecutables (backups, limpiar, etc...)
        '''
        Var.ui.actionLimpiarPanel.triggered.connect(Drivers.Drivers.limpiarPanel)



        '''
        ***************************************************** ZONA DE EXAMEN 05/12/2023 *****************************************************
        '''

        '''
        zona de eventos de tablas
        '''
        Eventos.Eventos.resizeTabClientes(self)
        Var.ui.tabClientes.clicked.connect(Clientes.Clientes.cargaClientes)
        Var.ui.tabDrivers.clicked.connect(Drivers.Drivers.cargaDriver)

        '''
        zona de eventos de las cajas de texto
        '''
        Var.ui.txtDniCliente.editingFinished.connect(lambda: Clientes.Clientes.validarDNI(Var.ui.txtDniCliente.displayText()))

        '''
        zona de eventos de botones
        '''
        Var.ui.btnAltaCliente.clicked.connect(Clientes.Clientes.altaClientes)
        Var.ui.btnBajaCliente.clicked.connect(Clientes.Clientes.borrarCliente)
        Var.ui.btnModificarCliente.clicked.connect(Clientes.Clientes.modifCli)

        '''
        zona de eventos de comboBox       NOTA: sirve para que cargue los datos en el comboBox
        '''
        Var.ui.cmbProvCliente.currentIndexChanged.connect(Conexion.Conexion.selMuniCli)
        Var.ui.rbtGroupCliente.buttonClicked.connect(Clientes.Clientes.selEstado)

        '''
        zona de eventos del menubar  NOTA: parte de arriba de la ventana donde hay desplegables (Archivo, Herramientas, Ayuda...)
        '''
        Var.ui.actionImportar_Datos_Cliente_XLS.triggered.connect(Eventos.Eventos.importarDatosXLSClientes)













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
