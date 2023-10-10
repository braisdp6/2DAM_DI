import Var
class Drivers():

    def limpiarPanel(self):
        try:
            listaWidgets = [Var.ui.txtDni, Var.ui.txtFechaAlta, Var.ui.txtApel, Var.ui.txtNombre, Var.ui.txtDireccion, Var.ui.txtMovil, Var.ui.txtSalario, Var.ui.lblValidarDni]
            for i in listaWidgets:
                i.setText(None)
        except Exception as error:
            print("error limpiar panel driver: ", error)


    def cargaFecha(qDate):
        try:
            #data = ("{0}/{1}/{2}".format(qDate.day(), qDate.month(), qDate.year()))
            data = ("{:02d}/{:02d}/{:4d}".format(qDate.day(), qDate.month(), qDate.year()))
            Var.ui.txtFechaAlta.setText(str(data))
            Var.calendar.hide()
        except Exception as error:
            print("error en cargar fecha: ", error)
    def validarDNI(self=None):
        try:
            dni = Var.ui.txtDni.text()
            dni = dni.upper()
            Var.ui.txtDni.setText(dni)
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
            dig_ext = "XYZ"
            reemp_dig_ext = {"X": "0", "Y": "1", "Z": "2"}
            numeros = "1234567890"

            if len(dni) == 9:  # comprueba que son nueve
                dig_control = dni[8]  # tomo la letra del dni
                dni = dni[:8]  # tomo los numeros del dni

                if dni[0] in dig_ext:  # reemplazas la letra por el numero correspondiente
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                    # comprueba que no haya letras en el medio

                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    Var.ui.lblValidarDni.setStyleSheet("color:green;")
                    Var.ui.lblValidarDni.setText("V")
                else:
                    Var.ui.lblValidarDni.setStyleSheet("color:red;")
                    Var.ui.lblValidarDni.setText("X")
                    Var.ui.txtDni.setText("")
                    Var.ui.txtDni.setFocus()

            else:
                Var.ui.lblValidarDni.setStyleSheet("color:red;")
                Var.ui.lblValidarDni.setText("X")
                Var.ui.txtDni.setText("")
                Var.ui.txtDni.setFocus()
        except Exception as error:
            print("error en validar dni: ", error)
