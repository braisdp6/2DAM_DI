import Var
class Eventos():
    def saludar(self):
        try:
            Var.ui.lblTitulo.setText("Hola has pulsado el botón")
        except Exception as error:
            print(error, "en modulo eventos")