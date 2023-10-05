from datetime import datetime
from VentanaCalendario import Ui_ventanaCalendario
from MainWindow import *
import sys,Var,Eventos



class Calendar(QtWidgets.QDialog):
    def __init__(self):
        super(Calendar, self).__init__()
        Var.calendar = Ui_ventanaCalendario()
        Var.calendar.setupUi(self)
        dia = datetime.now().day
        mes = datetime.now().month
        ano = datetime.now().year

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        Var.ui = Ui_MainWindow()
        Var.ui.setupUi(self) # encargado de generar la interfaz
        Var.calendar = Calendar()

        '''
        zona de eventos de botones
        '''
        Var.ui.btnCalendar.clicked.connect(Eventos.Eventos.abrirCalendar)
        '''
        zona de eventos del menubar
        '''
        Var.ui.actionSalir.triggered.connect(Eventos.Eventos.salir)
if __name__ == "__main__": # evita que haya dos funciones iguales que se lanzen
    app = QtWidgets.QApplication([])
    window = Main()
    window.showMaximized()
    sys.exit(app.exec())
