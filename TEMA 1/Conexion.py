from PyQt6 import QtSql, QtWidgets, QtCore, QtGui

import Drivers
import Var


class Conexion():
    def conexion(self=None):
        db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("bbdd.sqlite")
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
                    mbox.setText(query.lastError().text())
                    mbox.exec()
            # select datos de conductores de la base de datos
            Conexion.mostrarDrivers()
        except Exception as error:
            print("Error en alta conductor: ", error)

    def mostrarDrivers(self = None):
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
