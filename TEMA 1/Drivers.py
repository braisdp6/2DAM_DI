import re
from idlelib import query

from PyQt6 import QtWidgets, QtCore, QtGui

import Conexion
import Var


class Drivers():

    def limpiarPanel(self):
        try:
            listaWidgets = [Var.ui.txtDni, Var.ui.txtFechaAlta, Var.ui.txtApel, Var.ui.txtNombre, Var.ui.txtDireccion,
                            Var.ui.txtMovil, Var.ui.txtSalario, Var.ui.lblValidarDni, Var.ui.lblCodbd]
            for i in listaWidgets:
                i.setText(None)

            chkLicencia = [Var.ui.chkA, Var.ui.chkB, Var.ui.chkC, Var.ui.chkD]
            for i in chkLicencia:
                i.setChecked(False)
            Var.ui.cmbProvincia.setCurrentText("")
            Var.ui.cmbLocalidad.setCurrentText("")
        except Exception as error:
            print("error limpiar panel driver: ", error)

    def cargaFecha(qDate):
        try:
            # data = ("{0}/{1}/{2}".format(qDate.day(), qDate.month(), qDate.year()))
            data = ("{:02d}/{:02d}/{:4d}".format(qDate.day(), qDate.month(), qDate.year()))
            Var.ui.txtFechaAlta.setText(str(data))
            Var.calendar.hide()
        except Exception as error:
            print("error en cargar fecha: ", error)

    def validarDNI(self=None):
        try:
            dni = Var.ui.txtDni.text()
            dni = dni.upper()
            Var.ui.txtDni.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {"X": "0", "Y": "1", "Z": "2"}
            numeros = "1234567890"

            if len(dni) == 9:  # comprueba que son nueve
                dig_control = dni[8]  # tomo la letra del dni
                dni = dni[:8]  # tomo los numeros del dni

                if dni[0] in dig_ext:  # reemplazas la letra por el numero correspondiente
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                    # comprueba que no haya letras en el medio

                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    Var.ui.lblValidarDni.setStyleSheet("color:green;")
                    Var.ui.lblValidarDni.setText("V")
                else:
                    Var.ui.lblValidarDni.setStyleSheet("color:red;")
                    Var.ui.lblValidarDni.setText("X")
                    Var.ui.txtDni.setText("")
                    Var.ui.txtDni.setFocus()

            else:
                Var.ui.lblValidarDni.setStyleSheet("color:red;")
                Var.ui.lblValidarDni.setText("X")
                Var.ui.txtDni.setText("")
                Var.ui.txtDni.setFocus()
        except Exception as error:
            print("error en validar dni: ", error)

    def altaDriver(self):
        try:
            driver = [Var.ui.txtDni.text(), Var.ui.txtFechaAlta.text(), Var.ui.txtApel.text(), Var.ui.txtNombre.text(),
                      Var.ui.txtDireccion.text(), Var.ui.cmbProvincia.currentText(), Var.ui.cmbLocalidad.currentText(),
                      Var.ui.txtMovil.text(), Var.ui.txtSalario.text()]
            licencias = []
            chkLicencia = [Var.ui.chkA, Var.ui.chkB, Var.ui.chkC, Var.ui.chkD]
            for i in chkLicencia:
                if i.isChecked():
                    licencias.append(i.text())
            driver.append("-".join(licencias))
            print(driver)
            Conexion.Conexion.guardarDri(driver)
        except Exception as error:
            print("Error alta cliente ", error)

    def validarMovil(self=None):
        try:
            regex = r'^\d{9}$'
            numTelefono = Var.ui.txtMovil.text()

            if not re.match(regex, numTelefono):
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
                msg.setText('Valor de movil incorrecto (123456789)')
                msg.exec()
                Var.ui.txtMovil.setText("")
                Var.ui.txtMovil.setFocus()
            else:
                Var.ui.txtMovil.setText(numTelefono)
        except Exception as error:
            print("Error alta cliente ", error)

    # Metodo para mostrar los datos en la tabla
    def cargarTablaDri(registros): #TODO: error: 'NoneType' object is not iterable
        try:
            index = 0
            for registro in registros:
                Var.ui.tabDrivers.setRowCount(index + 1)
                Var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                Var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                Var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                Var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))
                Var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(registro[4])))
                Var.ui.tabDrivers.setItem(index, 5, QtWidgets.QTableWidgetItem(str(registro[5])))

                Var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                Var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                Var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                Var.ui.tabDrivers.item(index, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1
        except Exception as error:
            print("Error carga tabla drivers: ", error)

    # Metodo para cargar driver cuando se haga click en el "tabDriver"
    def cargaDriver(self):
        try:
            Drivers.limpiarPanel(self)
            row = Var.ui.tabDrivers.selectedItems() # Recoge la fila donde se haga click
            fila = [dato.text() for dato in row]
            registro = Conexion.Conexion.oneDriver(fila[0])
            datos = [Var.ui.lblCodbd, Var.ui.txtDni, Var.ui.txtFechaAlta, Var.ui.txtApel, Var.ui.txtNombre,
                     Var.ui.txtDireccion, Var.ui.cmbProvincia, Var.ui.cmbLocalidad, Var.ui.txtMovil, Var.ui.txtSalario]

            for i, dato in enumerate(datos):  # i es la posicion y dato es el contenido de datos
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))

            if "A" in registro[10]:
                Var.ui.chkA.setChecked(True)
            if "B" in registro[10]:
                Var.ui.chkB.setChecked(True)
            if "C" in registro[10]:
                Var.ui.chkC.setChecked(True)
            if "D" in registro[10]:
                Var.ui.chkD.setChecked(True)
            print(fila)
        except Exception as error:
            print("Error cargar datos de un cliente marcando en la tabla: ", error)

    def buscarDni(self):# TODO: buscar utilidad
        try:
            dni = Var.ui.txtDni.text()
            registro = Conexion.Conexion.codDri(dni)
            Drivers.cargarDatos(registro)
        except Exception as error:
            print("Error al buscar por DNI: ", error)

    def cargarDatos(registro):
        try:
            datos = [Var.ui.lblCodbd, Var.ui.txtDni, Var.ui.txtFechaAlta, Var.ui.txtApel, Var.ui.txtNombre,
                     Var.ui.txtDireccion, Var.ui.cmbProvincia, Var.ui.cmbLocalidad, Var.ui.txtMovil, Var.ui.txtSalario]

            for i, dato in enumerate(datos):  # i es la posicion y dato es el contenido de datos
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))
            if "A" in registro[10]:
                Var.ui.chkA.setChecked(True)
            if "B" in registro[10]:
                Var.ui.chkB.setChecked(True)
            if "C" in registro[10]:
                Var.ui.chkC.setChecked(True)
            if "D" in registro[10]:
                Var.ui.chkD.setChecked(True)
        except Exception as error:
            print("Error al cargar datos: ", error)

    # metodo para que te haga focus en la tabla que busques
    def buscarDriverTabla(self):
        try:
            dni = Var.ui.txtDni.text()
            registro = Conexion.Conexion.codDri(dni)
            Drivers.cargarDatos(registro)
            registros = Conexion.Conexion.mostrarDrivers()
            Drivers.cargarTablaDri(registros)
            codigo = Var.ui.lblCodbd.text()
            for fila in range(Var.ui.tabDrivers.rowCount()):
                if Var.ui.tabDrivers.item(fila, 0).text() == str(codigo):
                    # Var.ui.tabDrivers.selectRow(fila)
                    Var.ui.tabDrivers.scrollToItem(Var.ui.tabDrivers.item(fila, 0))
                    Var.ui.tabDrivers.setItem(fila, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                    Var.ui.tabDrivers.setItem(fila, 1, QtWidgets.QTableWidgetItem(str(registro[3])))
                    Var.ui.tabDrivers.setItem(fila, 2, QtWidgets.QTableWidgetItem(str(registro[4])))
                    Var.ui.tabDrivers.setItem(fila, 3, QtWidgets.QTableWidgetItem(str(registro[8])))
                    Var.ui.tabDrivers.setItem(fila, 4, QtWidgets.QTableWidgetItem(str(registro[10])))
                    Var.ui.tabDrivers.setItem(fila, 5, QtWidgets.QTableWidgetItem(str(registro[11])))
                    Var.ui.tabDrivers.item(fila, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    Var.ui.tabDrivers.item(fila, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    Var.ui.tabDrivers.item(fila, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    Var.ui.tabDrivers.item(fila, 5).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                    Var.ui.tabDrivers.item(fila, 0).setBackground(QtGui.QColor(255, 241, 150))
                    Var.ui.tabDrivers.item(fila, 1).setBackground(QtGui.QColor(255, 241, 150))
                    Var.ui.tabDrivers.item(fila, 2).setBackground(QtGui.QColor(255, 241, 150))
                    Var.ui.tabDrivers.item(fila, 3).setBackground(QtGui.QColor(255, 241, 150))
                    Var.ui.tabDrivers.item(fila, 4).setBackground(QtGui.QColor(255, 241, 150))
                    Var.ui.tabDrivers.item(fila, 5).setBackground(QtGui.QColor(255, 241, 150))
                    break
        except Exception as error:
            print(error, "en busca de datos de un conductor")

    def modifDri(self):
        try:
            driver = [Var.ui.lblCodbd, Var.ui.txtDni, Var.ui.txtFechaAlta, Var.ui.txtApel, Var.ui.txtNombre,
                      Var.ui.txtDireccion, Var.ui.cmbProvincia, Var.ui.cmbLocalidad,
                      Var.ui.txtMovil, Var.ui.txtSalario]
            modifDriver = []
            for i in driver:
                modifDriver.append(i.text().title())
            prov = Var.ui.cmbProvincia.currentText()
            modifDriver.insert(6, prov)
            muni = Var.ui.cmbProvincia.currentText()
            modifDriver.insert(7, muni)
            licencias = []
            chkLicencia = [Var.ui.chkA, Var.ui.chkB, Var.ui.chkC, Var.ui.chkD]

            for i in chkLicencia:
                if i.isChecked():
                    licencias.append(i.text())

            modifDriver.append("-".join(licencias))
            Conexion.Conexion.modifDriver(modifDriver)
        except Exception as error:
            print('Error en modificar driver: ', error)


    def borraDriv(self):
        try:
            dni = Var.ui.txtDni.text()
            Conexion.Conexion.borraDriv(dni)
            Drivers.cargarTablaDri(self)

        except Exception as error:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText("El conductor no existe o no se puede borrar")
                msg.exec()
