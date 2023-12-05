import re

from PyQt6 import QtWidgets, QtCore, QtGui

import Conexion
import Var

class Clientes():

    def altaClientes(self):
        try:
            cliente = [Var.ui.txtDniCliente.text(), Var.ui.txtRSCliente.text(), Var.ui.txtDireCliente.text(), Var.ui.txtTelefonoCliente.text(), Var.ui.cmbProvCliente.currentText(),Var.ui.cmbMuniCliente.currentText()]
            Conexion.Conexion.guardarCli(cliente)
        except Exception as error:
            print("Error alta cliente ", error)


    # Metodo que carga los datos en la tabla, lo usa solo el metodo Conexion.selectClientes()
    def cargarTablaCli(registros):
        try:
            Var.ui.tabClientes.clearContents()
            index = 0
            for registro in registros:
                Var.ui.tabClientes.setRowCount(index + 1)
                Var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(str(registro[0])))
                Var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(str(registro[1])))
                Var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(str(registro[2])))
                Var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(str(registro[3])))

                Var.ui.tabClientes.item(index, 0).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                Var.ui.tabClientes.item(index, 2).setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
                index += 1
        except Exception as error:
            print("Error carga tabla clientes: ", error)

    # Metodo para cargar cliente cuando se haga click en el "tabClientes"
    def cargaClientes(self=None):
        try:
            fila = Var.ui.tabClientes.selectedItems()
            row = [dato.text() for dato in fila]
            registro = Conexion.Conexion.oneCliente(row[0])

            Clientes.cargarDatos(registro)

        except Exception as error:
            print("Error al cargar los datos de un cliente: ", error)

    # nota: cargar los datos cuando clickeamos encima de algun driver
    def cargarDatos(registro):
        try:
            datos = [Var.ui.lblCodbdCliente.setText(str(registro[0])), Var.ui.txtDniCliente.setText(str(registro[1])), Var.ui.txtRSCliente.setText(str(registro[2])), Var.ui.txtDireCliente.setText(str(registro[3])), Var.ui.txtTelefonoCliente.setText(str(registro[4])), Var.ui.cmbProvCliente.setCurrentText(str(registro[5])),Var.ui.cmbMuniCliente.setCurrentText(str(registro[6])), Var.ui.txtFechaBCliente.setText(str(registro[7]))]
        except Exception as error:
            print("Error al cargar datos: ", error)

    def borrarCliente(self):
        try:
            dni = Var.ui.txtDniCliente.text()
            Conexion.Conexion.borrarCliente(dni)
            Conexion.Conexion.mostrarClientes(self)

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msg.setText("El conductor no existe o no se puede borrar: ", error)
            msg.exec()

    # metodo para que cambie los datos segun los radio buttons de la tabla
    def selEstado(self):
        if Var.ui.rbtTodosCliente.isChecked():
            estado = 0
            Conexion.Conexion.selectClientes(estado)
        elif Var.ui.rbtAltaCliente.isChecked():
            estado = 1
            Conexion.Conexion.selectClientes(estado)
        elif Var.ui.rbtBajaCliente.isChecked():
            estado = 2
            Conexion.Conexion.selectClientes(estado)

    def modifCli(self):
        try:
            cliente = [Var.ui.lblCodbdCliente.text().title(), Var.ui.txtDniCliente.text().title(), Var.ui.txtRSCliente.text().title(), Var.ui.txtDireCliente.text().title(), Var.ui.txtTelefonoCliente.text().title(), Var.ui.cmbProvCliente.currentText(),Var.ui.cmbMuniCliente.currentText(), Var.ui.txtFechaBCliente.text().title()]

            Conexion.Conexion.modifCliente(cliente)
        except Exception as error:
            print('Error en modificar cliente: ', error)

    @staticmethod
    def validarDNI(dni):
        try:
            dni = str(dni).upper()
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = "1234567890"

            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    Var.ui.lblValidarDniCli.setStyleSheet('color:green;')  # si es válido se pone una V en color verde
                    Var.ui.lblValidarDniCli.setText('V')
                    return True
                else:
                    Var.ui.lblValidarDniCli.setStyleSheet('color:red;')  # y si no un aspa en color rojo
                    Var.ui.lblValidarDniCli.setText('X')
                    Var.ui.txtDniCliente.setText(None)
                    Var.ui.txtDniCliente.setFocus()
            else:
                Var.ui.lblValidarDniCli.setStyleSheet('color:red;')
                Var.ui.lblValidarDniCli.setText('X')
                Var.ui.txtDniCliente.setText(None)
                Var.ui.txtDniCliente.setFocus()
        except Exception as error:
            print("error en validar dnicli ", error)





