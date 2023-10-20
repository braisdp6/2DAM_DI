from PyQt6 import QtWidgets, QtCore
from datetime import datetime

import Var, sys, locale
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

    def acerdade(self):
        try:
            pass
        except Exception as error:
            print("Error abrir ventana acerca de: ", error)

    def cargaProv(self=None):
        try:
            prov = ["A Coruña", "Lugo", "Vigo", "Ferrol", "Santiago de Compostela", "Ourense", "Pontevedra"]
            Var.ui.cmbProvincia.clear()
            Var.ui.cmbProvincia.addItem("")
            for i, m in enumerate(prov):
                Var.ui.cmbProvincia.addItem(str(m))
        except Exception as error:
            print("Error en la carga del combo prov: ", error)

    def selEstado(self):
        if Var.ui.rbtTodos.isChecked():
            print("Pulsaste todos.")
        elif Var.ui.rbtAlta.isChecked():
            print("Pulsaste alta.")
        elif Var.ui.rbtBaja.isChecked():
            print("Pulsaste baja.")

    def resizeTabDrivers(self): #TODO: NO FUNCIONA
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
            print("Error letra capital en cajas de texto ", error)