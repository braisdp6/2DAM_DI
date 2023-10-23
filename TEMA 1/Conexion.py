from PyQt6 import QtWidgets, QtSql, QtCore
import Var


class Conexion():
    def conexion(self = None):
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
                    #print(str(query.value(0)))
                    Var.ui.cmbProvincia.addItem(query.value(0))
        except Exception as error:
            print("Error en la carga del combo prov: ", error)

    def cargaLocalidad(self=None):
        try:
            Var.ui.cmbLocalidad.clear()
            query = QtSql.QSqlQuery()
            query.prepare("select municipio from municipios")
            if query.exec():
                Var.ui.cmbLocalidad.addItem("")
                while query.next():
                    #print(str(query.value(0)))
                    Var.ui.cmbLocalidad.addItem(query.value(0))
        except Exception as error:
            print("Error en la carga del combo prov: ", error)