import re

import Conexion
import Var
from PyQt6 import QtWidgets, QtCore


class Drivers():

    def limpiarPanel(self):
        try:
            listaWidgets = [Var.ui.txtDni, Var.ui.txtFechaAlta, Var.ui.txtApel, Var.ui.txtNombre, Var.ui.txtDireccion,
                            Var.ui.txtMovil, Var.ui.txtSalario, Var.ui.lblValidarDni]
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
            driver = [Var.ui.txtDni.text(), Var.ui.txtFechaAlta.text(), Var.ui.txtApel.text(), Var.ui.txtNombre.text(), Var.ui.txtDireccion.text(), Var.ui.cmbProvincia.currentText(), Var.ui.cmbLocalidad.currentText(), Var.ui.txtMovil.text(), Var.ui.txtSalario.text()]
            '''
            newDriver = []
            for i in driver:
                newDriver.append(i.text().title())
            prov = Var.ui.cmbProvincia.currentText()
            newDriver.insert(5, prov)
            muni = Var.ui.cmbLocalidad.currentText()
            newDriver.insert(6, muni)
            '''
            licencias = []
            chkLicencia = [Var.ui.chkA, Var.ui.chkB, Var.ui.chkC, Var.ui.chkD]
            for i in chkLicencia:
                if i.isChecked():
                    licencias.append(i.text())
            driver.append("-".join(licencias))
            print(driver)
            Conexion.Conexion.guardarDri(driver)
            '''
            index = 0
            Var.ui.tabDrivers.setRowCount(index + 1)
            Var.ui.tabDrivers.setItem(index, 0, QtWidgets.QTableWidgetItem(str(newDriver[0])))
            Var.ui.tabDrivers.setItem(index, 1, QtWidgets.QTableWidgetItem(str(newDriver[1])))
            Var.ui.tabDrivers.setItem(index, 2, QtWidgets.QTableWidgetItem(str(newDriver[2])))
            Var.ui.tabDrivers.setItem(index, 3, QtWidgets.QTableWidgetItem(str(newDriver[3])))
            Var.ui.tabDrivers.setItem(index, 4, QtWidgets.QTableWidgetItem(str(newDriver[4])))
            Var.ui.tabDrivers.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            Var.ui.tabDrivers.item(index, 3).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            Var.ui.tabDrivers.item(index, 4).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            '''
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
