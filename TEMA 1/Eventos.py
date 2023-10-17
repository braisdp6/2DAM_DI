import Var,sys
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

    def cargaProv(self = None):
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
