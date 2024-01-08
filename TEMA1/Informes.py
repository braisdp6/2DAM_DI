import os
from datetime import datetime

from reportlab.pdfgen import canvas

import Var


class Informes:

    def reportClientes(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre =  fecha + '_listadoclientes.pdf'
            Var.report = canvas.Canvas('informes/' + nombre)
            titulo = 'LISTADO CLIENTES'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            Var.report.drawString(250,250, 'Mi primer informe')
            Var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith('listadoclientes.pdf'):
                    os.startfile('%s\%s' % (rootPath,file))

        except Exception as error:
            print('Error LISTADO CLIENTES: ', error)

    def topInforme(titulo):
        try:
            logo = ".\img\logo.png"
            Var.report.line(50, 800, 525, 800)
            Var.report.setFont("Helvetica-Bold", size=14)
            Var.report.drawString(55, 785, "Transportes Teis")
            Var.report.drawString(240, 695, titulo)
            Var.report.line(50, 690, 525, 690)
            Var.report.drawImage(logo, 440, 715, width=65, height=65) # nota: no tocar dimensiones
            Var.report.setFont("Helvetica", size=9)
            Var.report.drawString(55, 770, "CIF: A12345678")
            Var.report.drawString(55, 755, "Avda. Galicia - 101")
            Var.report.drawString(55, 740, "Vigo - 36216 - España")
            Var.report.drawString(55, 725, "Teléfono: 986 132 456")
            Var.report.drawString(55, 710, "e-mail: cartesteisr@mail.com")

        except Exception as error:
            print("Error en cabecera informe: ", error)

    def footInforme(titulo):
        try:
            Var.report.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d-%m-%Y %H:%M:%S')
            Var.report.setFont("Helvetica-Oblique", size=7)
            Var.report.drawString(50, 40, str(fecha))
            Var.report.drawString(250, 40, str(titulo))
            Var.report.drawString(490, 40, str("Página %s" % Var.report.getPageNumber()))


        except Exception as error:
            print("Error en pie informe de cualquier tipo: ", error)
