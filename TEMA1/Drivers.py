import re

from PyQt6 import QtWidgets, QtCore, QtGui

import Conexion
import Var


class Drivers():
    @staticmethod
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

            if Var.ui.rbtTodos.isChecked():
                estado = 0
                Conexion.Conexion.selectDrivers(estado)
            elif Var.ui.rbtAlta.isChecked():
                estado = 1
                Conexion.Conexion.selectDrivers(estado)
            elif Var.ui.rbtBaja.isChecked():
                estado = 2
                Conexion.Conexion.selectDrivers(estado)


            # else:
            #     registros = Conexion.Conexion.mostrarDrivers(self)
            #     Drivers.cargarTablaDri(registros)

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
            # Nota: metodo para mostrar cuadro de dialogo en caso de que funcione el metodo
            valor = Conexion.Conexion.guardarDri(driver)
            if valor == True:
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

            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle("Aviso")
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
            mbox.setText("Empleado dado de alta")
            mbox.exec()
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

    # Metodo para cargar los datos en la tabla
    def cargarTablaDri(registros):
        try:
            Var.ui.tabDrivers.clearContents()
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
    def cargaDriver(self=None):
        try:
            # Drivers.limpiarPanel(self)
            fila = Var.ui.tabDrivers.selectedItems()
            row = [dato.text() for dato in fila]
            registro = Conexion.Conexion.oneDriver(row[0])
            # LLAMAMOS AL METODO CARGARDATOS PARA NO COPIAR CODIGO
            Drivers.cargarDatos(registro)

        except Exception as error:
            print("Error al cargar los datos de un cliente: ", error)

    def cargarDatos(registro):
        try:
            # nota: cargar los datos cuando clickeamos encima de algun driver
            datos = [Var.ui.lblCodbd, Var.ui.txtDni, Var.ui.txtFechaAlta, Var.ui.txtApel, Var.ui.txtNombre,
                     Var.ui.txtDireccion, Var.ui.cmbProvincia, Var.ui.cmbLocalidad, Var.ui.txtMovil, Var.ui.txtSalario]

            for i, dato in enumerate(datos):  # nota: i es la posicion y dato es el contenido de datos
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

    # nota: metodo para que te haga focus en la tabla que busques
    def buscarDriverLupa(self):
        try:
            dni = Var.ui.txtDni.text()
            registro = Conexion.Conexion.codDri(dni)
            Drivers.cargarDatos(registro)
            if Var.ui.rbtTodos.isChecked():
                estado = 0
                Conexion.Conexion.selectDrivers(estado)
            elif Var.ui.rbtAlta.isChecked():
                estado = 1
                Conexion.Conexion.selectDrivers(estado)
            elif Var.ui.rbtBaja.isChecked():
                estado = 2
                Conexion.Conexion.selectDrivers(estado)

            codigo = Var.ui.lblCodbd.text()
            for fila in range(Var.ui.tabDrivers.rowCount()):
                if Var.ui.tabDrivers.item(fila, 0).text() == str(codigo):
                    for columna in range(Var.ui.tabDrivers.columnCount()):
                        item = Var.ui.tabDrivers.item(fila, columna)
                        if item is not None:
                            item.setBackground(QtGui.QColor(255, 241, 150))
        except Exception as error:
            print(error, "en busca de datos de un conductor")

    def modifDri(self):
        try:
            driver = [Var.ui.lblCodbd, Var.ui.txtDni, Var.ui.txtFechaAlta, Var.ui.txtApel, Var.ui.txtNombre,
                      Var.ui.txtDireccion, Var.ui.txtMovil, Var.ui.txtSalario]
            modifDriver = []  # NOTA: array que va a contener todos los campos del driver
            for i in driver:
                modifDriver.append(i.text().title())

            # for i in driver:
            #     if isinstance(i, QtWidgets.QComboBox):
            #         modifDriver.append(i.currentText())  # Usar currentText() para QComboBox
            #     else:
            #         modifDriver.append(i.text().title())

            prov = Var.ui.cmbProvincia.currentText()
            modifDriver.insert(6, prov)
            muni = Var.ui.cmbLocalidad.currentText()
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
            Conexion.Conexion.mostrarDrivers(self)
            #Conexion.Conexion.selectDrivers(1)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText("El conductor no existe o no se puede borrar: ", error)
            msg.exec()

    # metodo para que cambie los datos segun los radio buttons de la tabla
    def selEstado(self):
        if Var.ui.rbtTodos.isChecked():
            estado = 0
            Conexion.Conexion.selectDrivers(estado)
        elif Var.ui.rbtAlta.isChecked():
            estado = 1
            Conexion.Conexion.selectDrivers(estado)
        elif Var.ui.rbtBaja.isChecked():
            estado = 2
            Conexion.Conexion.selectDrivers(estado)
