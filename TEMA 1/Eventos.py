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
            print("Error en abrir calendar", error)

 def acerdade():
     try:
         pass
     except Exception as error:
         print("Error abrir ventana acerca de", error)