from datetime import datetime

from PyQt6 import QtSql, QtWidgets, QtCore, QtGui

import Clientes
import Drivers
import Var


class Conexion():
    def conexion(self=None):
        Var.bbdd = "bbdd.sqlite"
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName(Var.bbdd)
        if not db.open():
            print("Error de conexion")
            return False
        else:
            print("Base de datos conectada")
            return True

    def cargaProv(self=None):
        try:
            Var.ui.cmbProvincia.clear()
            query = QtSql.QSqlQuery()
            query.prepare("select provincia from provincias")
            if query.exec():
                Var.ui.cmbProvincia.addItem("")
                while query.next():
                    # print(str(query.value(0)))
                    Var.ui.cmbProvincia.addItem(query.value(0))
        except Exception as error:
            print("Error en la carga del combo prov: ", error)

    def cargaProvCli(self=None):
        try:
            Var.ui.cmbProvCliente.clear()
            query = QtSql.QSqlQuery()
            query.prepare("select provincia from provincias")
            if query.exec():
                Var.ui.cmbProvCliente.addItem("")
                while query.next():
                    Var.ui.cmbProvCliente.addItem(query.value(0))
        except Exception as error:
            print("Error en la carga del combo provCli: ", error)

    def selMuni(self=None):
        try:
            Var.ui.cmbLocalidad.clear()
            id = 0
            prov = Var.ui.cmbProvincia.currentText()
            print("as")
            query = QtSql.QSqlQuery()
            query.prepare("select idprov from provincias where provincia = :prov")
            query.bindValue(":prov", prov)
            if query.exec():
                while query.next():
                    id = query.value(0)

            query1 = QtSql.QSqlQuery()
            query1.prepare("select municipio from municipios where idprov = :id")
            query1.bindValue(":id", int(id))
            if query1.exec():
                Var.ui.cmbLocalidad.addItem("")
                while query1.next():
                    Var.ui.cmbLocalidad.addItem(query1.value(0))

        except Exception as error:
            print("Error en la seleccion de municipios: ", error)

    def selMuniCli(self):
        try:
            Var.ui.cmbMuniCliente.clear()
            id = 0
            prov = Var.ui.cmbProvCliente.currentText()
            query = QtSql.QSqlQuery()
            query.prepare("select idprov from provincias where provincia = :prov")
            query.bindValue(":prov", prov)
            if query.exec():
                while query.next():
                    id = query.value(0)

            query1 = QtSql.QSqlQuery()
            query1.prepare("select municipio from municipios where idprov = :id")
            query1.bindValue(":id", int(id))
            if query1.exec():
                Var.ui.cmbMuniCliente.addItem("")
                while query1.next():
                    Var.ui.cmbMuniCliente.addItem(query1.value(0))
        except Exception as error:
            print("Error en la seleccion de municipios en pestaña clientes: ", error)

    @staticmethod
    def guardarDri(driver):
        try:  # comprobamos que no se añaden campos vacios
            if (driver[0].strip() == "" or driver[1].strip() == "" or driver[2].strip() == "" or driver[
                3].strip() == "" or driver[7].strip() == ""):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setWindowIcon(QtGui.QIcon("./img/warning.png"))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mensaje = "Faltan DATOS. Debe introducir al menos:\n\nDNI, Apellidos, Nombre, Fecha de alta, Movil."
                mbox.setText(mensaje)
                mbox.exec()
            else:
                query = QtSql.QSqlQuery()
                query.prepare(
                    "INSERT INTO drivers (dnidri, altadri, apeldri, nombredri, direcciondri, provdri, munidri, movildri, salariodri, carnetdri) VALUES (:dni, :alta, :apel, :nombre, :direccion, :prov, :muni, :movil, :salario, :carnet)")

                query.bindValue(":dni", str(driver[0]))
                query.bindValue(":alta", str(driver[1]))
                query.bindValue(":apel", str(driver[2]))
                query.bindValue(":nombre", str(driver[3]))
                query.bindValue(":direccion", str(driver[4]))
                query.bindValue(":prov", str(driver[5]))
                query.bindValue(":muni", str(driver[6]))
                query.bindValue(":movil", str(driver[7]))
                query.bindValue(":salario", str(driver[8]))
                query.bindValue(":carnet", str(driver[9]))

                if query.exec():  # Nota: se utiliza para mostrar los cuadros de dialogo de confimacion en Drivers.altaDriver()
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText("Empleado dado de alta.")
                    mbox.exec()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("Asegúrese de que el conductor no existe.")
                    mbox.exec()
            # select datos de conductores de la base de datos
            Conexion.mostrarDrivers(self=None)
        except Exception as error:
            print("Error en alta conductor: ", error)


    @staticmethod
    def guardarCli(cliente):
        try:  # comprobamos que no se añaden campos vacios
            if (cliente[0].strip() == "" or cliente[1].strip() == "" or cliente[2].strip() == "" or cliente[
                3].strip() == "" or cliente[4].strip() == "" or cliente[5].strip() == ""):
                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setWindowIcon(QtGui.QIcon("./img/warning.png"))
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mensaje = "Faltan DATOS. Debe llenar todos los campos."
                mbox.setText(mensaje)
                mbox.exec()
            else:
                query = QtSql.QSqlQuery()
                query.prepare(
                    "INSERT INTO clientes (dnicli, rscli, direccioncli, telefonocli, provcli, municli) VALUES (:dni, :rs, :direccion, :telefono, :prov, :muni)")

                query.bindValue(":dni", str(cliente[0]))
                query.bindValue(":rs", str(cliente[1]))
                query.bindValue(":direccion", str(cliente[2]))
                query.bindValue(":telefono", str(cliente[3]))
                query.bindValue(":prov", str(cliente[4]))
                query.bindValue(":muni", str(cliente[5]))

                if query.exec():  # Nota: se utiliza para mostrar los cuadros de dialogo de confimacion en Drivers.altaDriver()
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText("Empleado dado de alta.")
                    mbox.exec()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle('Aviso')
                    mbox.setWindowIcon(QtGui.QIcon('./img/logo.ico'))
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("Asegúrese de que el conductor no existe.")
                    mbox.exec()
            # select datos de conductores de la base de datos
            Conexion.mostrarClientes(self=None)
        except Exception as error:
            print("Error en alta cliente: ", error)

    # Metodo que pasa la posicion del historico, para luego mostrar los Drivers en la tabla por otros metodos
    @staticmethod
    def mostrarDrivers(self):  # Nota: no borrar el self
        try:
            if Var.ui.rbtTodos.isChecked():
                estado = 0
                Conexion.selectDrivers(
                    estado)
            elif Var.ui.rbtAlta.isChecked():
                estado = 1
                Conexion.selectDrivers(
                    estado)
            elif Var.ui.rbtBaja.isChecked():
                estado = 2
                Conexion.selectDrivers(
                    estado)  # Nota: le pasamos el estado y que el metodo selectDrivers() cargue los drivers en la tabla
        except Exception as error:
            print("Error mostrar drivers: ", error)

    @staticmethod
    def mostrarClientes(self):  # Nota: no borrar el self
        try:
            if Var.ui.rbtTodosCliente.isChecked():
                estado = 0
                Conexion.selectClientes(
                    estado)
            elif Var.ui.rbtAltaCliente.isChecked():
                estado = 1
                Conexion.selectClientes(
                    estado)
            elif Var.ui.rbtBajaCliente.isChecked():
                estado = 2
                Conexion.selectClientes(
                    estado)  # Nota: le pasamos el estado y que el metodo selectDrivers() cargue los drivers en la tabla
        except Exception as error:
            print("Error mostrar clientes: ", error)

    # buscamos un conductor segun su codigo en la BBDD
    def oneDriver(codigo):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM drivers WHERE codigo = :codigo")
            query.bindValue(":codigo", int(codigo))
            if query.exec():
                while query.next():
                    for i in range(12):  # recorremos las columnas de la BBDD
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("Error en fichero conexion datos de 1 driver: ", error)

    # buscamos un conductor segun su codigo en la BBDD
    def oneCliente(codigo):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM clientes WHERE codigocli = :codigo")
            query.bindValue(":codigo", int(codigo))
            if query.exec():
                while query.next():
                    for i in range(8):  # recorremos las columnas de la BBDD
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("Error en fichero conexion datos de 1 cliente: ", error)

    # Metodo buscar el codigo del driver segun su dni, para después recuperar el driver segun su codigo
    def codDri(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT codigo FROM drivers WHERE dnidri =:dnidri")
            query.bindValue(":dnidri", str(dni))
            if query.exec():
                while query.next():
                    codigo = query.value(0)
                if codigo is not None:
                    registro = Conexion.oneDriver(codigo)
                    return registro
        except Exception as error:
            print("Error en busca de codigo de un conductor: ", error)
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Aviso")
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText('El conductor no existe o error de búsqueda')
            mbox.exec()

    def modifDriver(modifDriver):  # Nota: "modifDriver" es un array que contiene todos los datos del driver
        try:
            registro = Conexion.oneDriver(int(modifDriver[0]))
            if modifDriver[1] == registro[
                1]:  # Nota: aquí comprobamos que el driver existe en la base de datos previamente, para no modificar empleados que no existan
                query = QtSql.QSqlQuery()
                query.prepare(
                    "UPDATE drivers SET dnidri = :dni, altadri= :alta, apeldri = :apel, nombredri = :nombre, direcciondri "
                    "= :direccion, provdri = :provincia, munidri = :municipio, movildri = :movil, salariodri = :salario, "
                    "carnetdri = :carnet, bajadri = :baja where codigo = :codigo")

                query.bindValue(":codigo", int(modifDriver[0]))
                query.bindValue(":dni", str(modifDriver[1]))
                query.bindValue(":alta", str(modifDriver[2]))
                query.bindValue(":apel", str(modifDriver[3]))
                query.bindValue(":nombre", str(modifDriver[4]))
                query.bindValue(":direccion", str(modifDriver[5]))
                query.bindValue(":provincia", str(modifDriver[6]))
                query.bindValue(":municipio", str(modifDriver[7]))
                query.bindValue(":movil", str(modifDriver[8]))
                query.bindValue(":salario", str(modifDriver[9]))
                query.bindValue(":carnet", str(modifDriver[10]))
                if str(modifDriver[11]) == '':
                    query.bindValue(":baja", None)
                else:
                    query.bindValue(":baja", str(modifDriver[11]))

                if query.exec():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Aviso")
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText("Datos Conductor Modificados")
                    msg.exec()
                    Conexion.mostrarDrivers(self=None)
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Aviso")
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText(query.lastError().text())
                    msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText("No existe el conductor a modificar.")
                msg.exec()

        except Exception as error:
            print("Error en metodo modifDriver: ", error)


    def modifCliente(modifCliente):
        try:
            registro = Conexion.oneCliente(int(modifCliente[0]))
            if modifCliente[0] == registro[0]:
                query = QtSql.QSqlQuery()
                query.prepare(
                    "UPDATE clientes SET dnicli = :dni, rscli = :rs, direccioncli = :direccion,  telefonocli = :telefono, provcli = :prov, municli = :muni, bajacli = :baja where codigocli = :codigo")

                query.bindValue(":codigo", int(modifCliente[0]))
                query.bindValue(":dni", str(modifCliente[1]))
                query.bindValue(":rs", str(modifCliente[2]))
                query.bindValue(":direccion", str(modifCliente[3]))
                query.bindValue(":telefono", str(modifCliente[4]))
                query.bindValue(":prov", str(modifCliente[5]))
                query.bindValue(":muni", str(modifCliente[6]))
                if str(modifCliente[7]) == '':
                    query.bindValue(":baja", None)
                else:
                    query.bindValue(":baja", str(modifCliente[7]))

                if query.exec():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Aviso")
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText("Datos Cliente Modificados")
                    msg.exec()
                    Conexion.mostrarClientes(self=None)
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Aviso")
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    msg.setText(query.lastError().text())
                    msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText("No existe el cliente a modificar.")
                msg.exec()

        except Exception as error:
            print("Error en metodo modifCliente: ", error)

    def borraDriv(dni):
        global valor
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare("SELECT bajadri FROM drivers WHERE dnidri = :dni")
            query1.bindValue(":dni", str(dni))

            if query1.exec():
                while query1.next():
                    valor = query1.value(0)

            if valor == "":
                # comprobar fecha
                fecha = datetime.today()
                fecha = fecha.strftime("%d/%m/%Y")

                query = QtSql.QSqlQuery()
                query.prepare("UPDATE drivers SET bajadri = :fechabaja WHERE dnidri = :dni")
                query.bindValue(":fechabaja", str(fecha))
                query.bindValue(":dni", str(dni))

                if query.exec():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Aviso")
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText("Conductor dado de baja.")
                    msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText("No existe conductor o conductor dado de baja anteriormente.")
                msg.exec()
        except Exception as error:
            print("Error en baja driver en conexion: ", error)

    def borrarCliente(dni):
        global valor1
        try:
            query1 = QtSql.QSqlQuery()
            query1.prepare("SELECT bajacli FROM clientes WHERE dnicli = :dni")
            query1.bindValue(":dni", str(dni))

            if query1.exec():
                while query1.next():
                    valor1 = query1.value(0)

            if valor1 == "":
                # comprobar fecha
                fecha = datetime.today()
                fecha = fecha.strftime("%d/%m/%Y")

                query = QtSql.QSqlQuery()
                query.prepare("UPDATE clientes SET bajacli = :fechabaja WHERE dnicli = :dni")
                query.bindValue(":fechabaja", str(fecha))
                query.bindValue(":dni", str(dni))

                if query.exec():
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Aviso")
                    msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    msg.setText("Cliente dado de baja.")
                    msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText("No existe cliente dado de baja anteriormente.")
                msg.exec()
        except Exception as error:
            print("Error en baja cliente en conexion: ", error)

    def selectDrivers(
            estado):  # NOTA: recibe por parametro la posicion del histórico y luego a traves de Drivers.cargarTablaDri() carga los datos en la tabla
        try:
            registros = []
            if estado == 0:
                Var.ui.lblFechaBaja.hide()
                Var.ui.txtFechaBaja.hide()
                Var.ui.btnCalendarBaja.hide()
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, apeldri, nombredri, movildri, "
                              "carnetdri, bajadri from drivers")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                Drivers.Drivers.cargarTablaDri(registros)
            elif estado == 1:
                Var.ui.lblFechaBaja.hide()
                Var.ui.txtFechaBaja.hide()
                Var.ui.btnCalendarBaja.hide()
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, apeldri, nombredri, movildri, "
                              "carnetdri, bajadri from drivers where bajadri is null")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                Drivers.Drivers.cargarTablaDri(registros)
            elif estado == 2:
                Var.ui.lblFechaBaja.show()
                Var.ui.txtFechaBaja.show()
                Var.ui.btnCalendarBaja.show()
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, apeldri, nombredri, movildri, "
                              "carnetdri, bajadri from drivers where bajadri is not null")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                Drivers.Drivers.cargarTablaDri(registros)
        except Exception as error:
            print("Error al seleccionar los drivers", error)

    def selectClientes(
            estado):  # NOTA: recibe por parametro la posicion del histórico y luego a traves de Drivers.cargarTablaDri() carga los datos en la tabla
        try:
            registros = []
            if estado == 0:
                Var.ui.lblFechaBCliente.hide()
                Var.ui.txtFechaBCliente.hide()
                Var.ui.btnCalendarBajaCli.hide()
                query = QtSql.QSqlQuery()
                query.prepare("select codigocli, rscli, telefonocli, provcli from clientes")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                Clientes.Clientes.cargarTablaCli(registros)
            elif estado == 1:
                Var.ui.lblFechaBCliente.hide()
                Var.ui.txtFechaBCliente.hide()
                Var.ui.btnCalendarBajaCli.hide()
                query = QtSql.QSqlQuery()
                query.prepare("select codigocli, rscli, telefonocli, provcli from clientes where bajacli is null")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                Clientes.Clientes.cargarTablaCli(registros)
            elif estado == 2:
                Var.ui.lblFechaBCliente.show()
                Var.ui.txtFechaBCliente.show()
                Var.ui.btnCalendarBajaCli.show()
                query = QtSql.QSqlQuery()
                query.prepare("select codigocli, rscli, telefonocli, provcli from clientes where bajacli is not null")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                Clientes.Clientes.cargarTablaCli(registros)
        except Exception as error:
            print("Error al seleccionar los clientes", error)

    @staticmethod
    def selectDriversTodos():  # NOTA: metodo para buscar todos los drivers
        try:
            registros = []
            query = QtSql.QSqlQuery()
            query.prepare("select * from drivers order by apeldri")
            if query.exec():
                while query.next():
                    row = [query.value(i) for i in range(query.record().count())]  # funcion lambda
                    registros.append(row)
            return registros
        except Exception as error:
            print("error devolver todos los drivers: ", error)




