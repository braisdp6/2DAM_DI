from datetime import datetime

from PyQt6 import QtSql, QtWidgets, QtCore, QtGui

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

    def cargaProv(self=None):s
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

    def selMuni(self=None):
        try:
            Var.ui.cmbLocalidad.clear()
            id = 0
            prov = Var.ui.cmbProvincia.currentText()
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

    def guardarDri(newDriver):
        try:  # comprobamos que no se añaden campos vacios
            if (newDriver[0].strip() == "" or newDriver[1].strip() == "" or newDriver[2].strip() == "" or newDriver[3].strip() == "" or newDriver[7].strip() == ""):
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

                query.bindValue(":dni", str(newDriver[0]))
                query.bindValue(":alta", str(newDriver[1]))
                query.bindValue(":apel", str(newDriver[2]))
                query.bindValue(":nombre", str(newDriver[3]))
                query.bindValue(":direccion", str(newDriver[4]))
                query.bindValue(":prov", str(newDriver[5]))
                query.bindValue(":muni", str(newDriver[6]))
                query.bindValue(":movil", str(newDriver[7]))
                query.bindValue(":salario", str(newDriver[8]))
                query.bindValue(":carnet", str(newDriver[9]))
                if query.exec():
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle("Aviso")
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                    mbox.setText("Empleado dado de alta")
                    mbox.exec()
                else:
                    mbox = QtWidgets.QMessageBox()
                    mbox.setWindowTitle("Aviso")
                    mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                    mbox.setText("Asegúrese que el NIF no exista en la base de datos.")
                    mbox.exec()
            # select datos de conductores de la base de datos
            Conexion.mostrarDrivers()
        except Exception as error:
            print("Error en alta conductor: ", error)

    # Metodo para mostrar los Drivers en la tabla
    @classmethod
    def mostrarDrivers(self):
        try:
            registros = []
            query1 = QtSql.QSqlQuery()
            query1.prepare("SELECT codigo, apeldri, nombredri, movildri, carnetdri, bajadri FROM drivers")
            if query1.exec():
                while query1.next():
                    row = [query1.value(i) for i in range(query1.record().count())]
                    registros.append(row)
            Drivers.Drivers.cargarTablaDri(registros)
            print(registros)
        except Exception as error:
            print("Error mostrar drivers: ", error)

    # buscamos un conductor segun su codigo en la BBDD
    def oneDriver(codigo):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT * FROM drivers WHERE codigo = :codigo")
            query.bindValue(":codigo", int(codigo))
            if query.exec():
                while query.next():
                    for i in range(12):# recorremos las columnas de la BBDD
                        registro.append(str(query.value(i)))
            return registro
        except Exception as error:
            print("Error en fichero conexion datos de 1 driver: ", error)

    def codDri(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT codigo FROM drivers WHERE dnidri =:dnidri")
            query.bindValue(":dnidri", str(dni))
            if query.exec():
                while query.next():
                    codigo = query.value(0)
                    registro = Conexion.oneDriver(codigo)
                    return registro

                mbox = QtWidgets.QMessageBox()
                mbox.setWindowTitle("Aviso")
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                mbox.setText("El conductor no existe.")
                mbox.exec()
        except Exception as error:
            print("Error en busca de codigo de un conductor: ", error)

    def modifDriver(modifDriver):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("UPDATE drivers SET dnidri = :dni, altadri= :alta, apeldri = :apel, nombredri = :nombre, direcciondri = :direccion, provdri = :provincia, munidri = :municipio, movildri = :movil, salariodri = :salario, carnetdri = :carnet where codigo = :codigo")

            query.bindValue(":codigo", int(modifDriver[0]))
            query.bindValue(":dni", str(modifDriver[1]))
            query.bindValue(":alta", str(modifDriver[2]))
            query.bindValue(":apel", str(modifDriver[3]))
            query.bindValue(":nombre", str(modifDriver[4]))
            query.bindValue(":direccion", str(modifDriver[5]))
            query.bindValue(":prov", str(modifDriver[6]))
            query.bindValue(":muni", str(modifDriver[7]))
            query.bindValue(":movil", str(modifDriver[8]))
            query.bindValue(":salario", str(modifDriver[9]))
            query.bindValue(":carnet", str(modifDriver[10]))

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
        except Exception as error:
            print("Error en metodo modifDriver: ", error)

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


    def selectDrivers(estado):
        try:
            registros=[]
            if estado == 0:
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, apeldri, nombredri, movildri, "
                               "carnetdri, bajadri from drivers")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                Drivers.Drivers.cargarTablaDri(registros)
            elif estado == 1:
                query = QtSql.QSqlQuery()
                query.prepare("select codigo, apeldri, nombredri, movildri, "
                              "carnetdri, bajadri from drivers where bajadri is null")
                if query.exec():
                    while query.next():
                        row = [query.value(i) for i in range(query.record().count())]
                        registros.append(row)
                Drivers.Drivers.cargarTablaDri(registros)
            elif estado == 2:
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
