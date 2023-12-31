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

    def cargaFechaAlta(qDate):
        try:
            data = ("{:02d}/{:02d}/{:4d}".format(qDate.day(), qDate.month(), qDate.year()))
            Var.ui.txtFechaAlta.setText(str(data))
            Var.calendarAlta.hide()
        except Exception as error:
            print("error en cargar fecha alta: ", error)

    def cargaFechaBaja(qDate):
        try:
            data = ("{:02d}/{:02d}/{:4d}".format(qDate.day(), qDate.month(), qDate.year()))
            Var.ui.txtFechaBaja.setText(str(data))
            Var.calendarBaja.hide()
        except Exception as error:
            print("error en cargar fecha baja: ", error)

    @staticmethod
    def validarDNI(dni):
        try:
            dni = str(dni).upper()
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"
            print(dni)
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    Var.ui.lblValidarDni.setStyleSheet('color:green;')  # si es válido se pone una V en color verde
                    Var.ui.lblValidarDni.setText('V')
                    return True
                else:
                    Var.ui.lblValidarDni.setStyleSheet('color:red;')  # y si no un aspa en color rojo
                    Var.ui.lblValidarDni.setText('X')
                    Var.ui.txtDni.setText(None)
                    Var.ui.txtDni.setFocus()
            else:
                Var.ui.lblValidarDni.setStyleSheet('color:red;')
                Var.ui.lblValidarDni.setText('X')
                Var.ui.txtDni.setText(None)
                Var.ui.txtDni.setFocus()
        except Exception as error:
            print("error en validar dni ", error)

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

    # Metodo que carga los datos en la tabla, lo usa solo el metodo Conexion.selectDrivers()
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

    # nota: cargar los datos cuando clickeamos encima de algun driver
    def cargarDatos(registro):
        try:
            datos = [Var.ui.lblCodbd, Var.ui.txtDni, Var.ui.txtFechaAlta, Var.ui.txtApel, Var.ui.txtNombre,
                     Var.ui.txtDireccion, Var.ui.cmbProvincia, Var.ui.cmbLocalidad, Var.ui.txtMovil, Var.ui.txtSalario]

            for i, dato in enumerate(datos):  # nota: i es la posicion y dato es el contenido de datos
                if i == 6 or i == 7:
                    dato.setCurrentText(str(registro[i]))
                else:
                    dato.setText(str(registro[i]))
            if 'A' in registro[10]:
                Var.ui.chkA.setChecked(True)
            else:
                Var.ui.chkA.setChecked(False)

            if 'B' in registro[10]:
                Var.ui.chkB.setChecked(True)
            else:
                Var.ui.chkB.setChecked(False)

            if 'C' in registro[10]:
                Var.ui.chkC.setChecked(True)
            else:
                Var.ui.chkC.setChecked(False)

            if 'D' in registro[10]:
                Var.ui.chkD.setChecked(True)
            else:
                Var.ui.chkD.setChecked(False)

            Var.ui.txtFechaBaja.setText(str(registro[11]))

        except Exception as error:
            print("Error al cargar datos: ", error)

    # nota: metodo para que te haga focus en la tabla que busques
    def buscarDriverLupa(self):
        try:
            dni = Var.ui.txtDni.text()
            registro = Conexion.Conexion.codDri(dni)
            Drivers.cargarDatos(registro)

            # Nota: de esta forma cambiamos el historico y lo cargamos
            if registro[11] == "":
                Var.ui.rbtAlta.setChecked(True)
                Conexion.Conexion.selectDrivers(1)
            else:
                Var.ui.rbtBaja.setChecked(True)
                Conexion.Conexion.selectDrivers(2)

            codigo = Var.ui.lblCodbd.text()
            for fila in range(Var.ui.tabDrivers.rowCount()):
                if Var.ui.tabDrivers.item(fila, 0).text() == str(codigo):
                    for columna in range(Var.ui.tabDrivers.columnCount()):
                        item = Var.ui.tabDrivers.item(fila, columna)
                        if item is not None:
                            item.setBackground(QtGui.QColor(255, 241, 150))
                            Var.ui.tabDrivers.scrollToItem(item)
        except Exception as error:
            print(error, "en busca de datos de un conductor")

    def modifDri(self):
        try:
            driver = [Var.ui.lblCodbd.text().title(), Var.ui.txtDni.text().title(), Var.ui.txtFechaAlta.text().title(), Var.ui.txtApel.text().title(), Var.ui.txtNombre.text().title(),
                      Var.ui.txtDireccion.text().title(), Var.ui.cmbProvincia.currentText(), Var.ui.cmbLocalidad.currentText(),
                      Var.ui.txtMovil.text().title(), Var.ui.txtSalario.text().title()]
            licencias = []
            chkLicencia = [Var.ui.chkA, Var.ui.chkB, Var.ui.chkC, Var.ui.chkD]
            for i in chkLicencia:
                if i.isChecked():
                    licencias.append(i.text())
            driver.append("-".join(licencias))
            driver.append(Var.ui.txtFechaBaja.text().title())

            Conexion.Conexion.modifDriver(driver)
        except Exception as error:
            print('Error en modificar driver: ', error)

    def borraDriv(self):
        try:
            dni = Var.ui.txtDni.text()
            Conexion.Conexion.borraDriv(dni)
            Conexion.Conexion.mostrarDrivers(self)

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
