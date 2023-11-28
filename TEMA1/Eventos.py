import os.path
import shutil
import zipfile
from datetime import datetime

import xlrd
import xlwt
from PyQt6 import QtWidgets, QtSql

import Conexion
import Drivers
import Var
import locale
import sys

locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")
locale.setlocale(locale.LC_MONETARY, "es_ES.UTF-8")


class Eventos():
    def salir(self):
        try:
            sys.exit()
            pass
        except Exception as error:
            print(error, "en modulo eventos")

    def abrirCalendar(self):
        try:
            Var.calendar.show()
        except Exception as error:
            print("Error en abrir calendar: ", error)

    def abrirVentanaSalir(self):
        try:
            Var.ventanaSalir.show()
        except Exception as error:
            print("Error en abrir ventana salir: ", error)

    def abrirAcercaDe(self):
        try:
            Var.acercaDe.show()
            pass
        except Exception as error:
            print("Error abrir ventana acerca de: ", error)

    def selHistorico(self):
        if Var.ui.rbtTodos.isChecked():
            print("Pulsaste todos.")
        elif Var.ui.rbtAlta.isChecked():
            print("Pulsaste alta.")
        elif Var.ui.rbtBaja.isChecked():
            print("Pulsaste baja.")

    def resizeTabDrivers(self):
        try:
            header = Var.ui.tabDrivers.horizontalHeader()
            for i in range(5):
                if i == 0 or i == 4 or i == 3:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
                elif i == 1 or i == 2:
                    header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeMode.Stretch)
        except Exception as error:
            print("Error a la hora de redimensionar en tabDrivers ", error)

    @staticmethod
    def formatCajaTexto():
        try:
            Var.ui.txtApel.setText(Var.ui.txtApel.text().title())
            Var.ui.txtNombre.setText(Var.ui.txtNombre.text().title())

            Var.ui.txtSalario.setText(str(locale.currency(float(Var.ui.txtSalario.text()))))
        except Exception as error:
            print("Error a la hora de formatear las cajas de texto ", error)

    def crearBackup(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime("%Y_%m_%d_%H_%M_%S")
            copia = (str(fecha) + "_backup.zip")
            directorio, filename = Var.dlgAbrir.getSaveFileName(None, "Guardar Copia Seguridad", copia, ".zip")
            if Var.dlgAbrir.accept and filename != "":
                fichZip = zipfile.ZipFile(copia, "w")
                fichZip.write(Var.bbdd, os.path.basename(Var.bbdd), zipfile.ZIP_DEFLATED)
                fichZip.close()
                shutil.move(str(copia), str(directorio))
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText("Copia de Seguridad Creada.")
                msg.exec()
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText("Error en copia de seguridad: ", error)
            msg.exec()

    def restaurarBackup(self):
        try:
            filename = Var.dlgAbrir.getOpenFileName(None, 'Restaurar Copia de Seguridad',
                                                    '', '*.zip;;All Files(*)')
            file = filename[0]
            if Var.dlgAbrir.accept and file:
                with zipfile.ZipFile(str(file), 'r') as bbdd:
                    bbdd.extractall(pwd=None)
                bbdd.close()
                Conexion.Conexion.mostrarDrivers()

                msg = QtWidgets.QMessageBox()
                msg.setModal(True)
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
                msg.setText('Copia de Seguridad Restaurada.')
                msg.exec()
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error en Restauracion Copia Seguridad: ', error)
            msg.exec()

    def exportarDatosXLS(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            file = (str(fecha) + 'Datos.xls')
            directorio, filename = Var.dlgAbrir.getSaveFileName(None, 'Exportar datos en XLS', file, '.xls')
            if Var.dlgAbrir.accept and filename:
                wb = xlwt.Workbook()
                sheet1 = wb.add_sheet('conductores')
                sheet1.write(0, 0, 'ID')
                sheet1.write(0, 1, 'DNI')
                sheet1.write(0, 2, 'Fecha Alta')
                sheet1.write(0, 3, 'Apellidos')
                sheet1.write(0, 4, 'Nombre')
                sheet1.write(0, 5, 'Direccion')
                sheet1.write(0, 6, 'Provincia')
                sheet1.write(0, 7, 'Localidad')
                sheet1.write(0, 8, 'Movil')
                sheet1.write(0, 9, 'Salario')
                sheet1.write(0, 10, 'Licencias')
                sheet1.write(0, 11, 'Fecha baja')
                registros = Conexion.Conexion.selectDriversTodos(self)

                for j, registro in enumerate(registros, 1):
                    for i, valor in enumerate(registro[:-1]):
                        sheet1.write(j, i, valor)
                wb.save(directorio)
                mbox = QtWidgets.QMessageBox()
                mbox.setModal(True)
                mbox.setWindowTitle('Aviso')
                mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                mbox.setText("Exportación completada con éxito.")
                mbox.exec()

        except Exception as error:
            mbox = QtWidgets.QMessageBox()
            mbox.setWindowTitle('Aviso')
            mbox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            mbox.setText("Error exportar datos en hoja de calculo", error)
            mbox.exec()

    def importarDatos(self):
        try:
            fileName = Var.dlgAbrir.getOpenFileName(None, "Importar datos", "", ".xls;;All Files(*)")
            if Var.dlgAbrir.accept and fileName != "":
                file = fileName[0]
                documento = xlrd.open_workbook(file)
                datos = documento.sheet_by_index(0)  # Nota: cogemos datos de la primera hoja del .xls
                filas = datos.nrows
                columnas = datos.ncols
                for i in range(filas):
                    if i == 0:  # Nota: lee la primera fila donde estan las cabeceras (no las vamos a usar)
                        pass
                    else:
                        new = []  # Nota: le cargamos en el array todos los datos de las filas del .xls
                        for j in range(columnas):
                            new.append(str(datos.cell(i, j)))
                            # if Drivers.Drivers.validarDNI(str(new[0])) checkeamos si existe el DNI (NOTA: se necesita hacer un metodo con sobrecarga, que no funciona todavia)
                        Conexion.Conexion.guardarDri(new)
                    if i == filas -1:
                        mbox = QtWidgets.QMessageBox()
                        mbox.setModal(True)
                        mbox.setWindowTitle("Aviso")
                        mbox.setIcon(QtWidgets.QMessageBox.Icon.Information)
                        mbox.setText("Importación de Datos Realizada")
                        mbox.exec()
                Conexion.Conexion.selectDrivers(1)
                
        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msg.setText('Error en importar datos: ', error)
            msg.exec()
