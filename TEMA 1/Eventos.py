import os.path
import shutil
import zipfile
from datetime import datetime

from PyQt6 import QtWidgets

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
            msg.setText("Error en copia de seguridad.")
            msg.exec()
