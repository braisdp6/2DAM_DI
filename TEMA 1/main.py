import Eventos
from MainWindow import *
import sys,Var


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        Var.ui = Ui_MainWindow()
        Var.ui.setupUi(self) # encargado de generar la interfaz

        '''
        zona de eventos de botones
        '''
        Var.ui.btnSalir.clicked.connect(Eventos.Eventos.saludar)

if __name__ == "__main__": # evita que haya dos funciones iguales que se lanzen
    app = QtWidgets.QApplication([])
    window = Main()
    window.show()
    sys.exit(app.exec())
