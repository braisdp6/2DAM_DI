import os
from datetime import datetime

from PyQt6 import QtSql
from reportlab.pdfgen import canvas

import Var


class Informes:

    def reportClientes(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadoclientes.pdf'
            Var.report = canvas.Canvas('informes/' + nombre)
            titulo = 'LISTADO CLIENTES'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)

            items = ['Código', 'DNI', 'RAZÓN SOCIAL', 'MUNICIPIO', 'TELÉFONO', 'FECHA BAJA']
            Var.report.setFont('Helvetica-Bold', size=10)
            Var.report.drawString(55, 675, str(items[0]))
            Var.report.drawString(120, 675, str(items[1]))
            Var.report.drawString(160, 675, str(items[2]))
            Var.report.drawString(285, 675, str(items[3]))
            Var.report.drawString(370, 675, str(items[4]))
            Var.report.drawString(460, 675, str(items[5]))  # Nueva coordenada para "FECHA BAJA"
            Var.report.line(50, 670, 525, 670)  # Ajusta la longitud de la línea

            # obtencion datos de la base de datos
            query = QtSql.QSqlQuery()
            query.prepare('SELECT codigocli, dnicli, rscli, municli, telefonocli, bajacli FROM clientes ORDER BY rscli')
            Var.report.setFont('Helvetica', size=9)

            if query.exec():
                i = 55
                j = 655
                while query.next():
                    if j <= 80:
                        Var.report.drawString(450, 75, 'Página siguiente...')
                        Var.report.showPage()  # crea una pagina nueva
                        Informes.topInforme(titulo)
                        Informes.footInforme(titulo)
                        Var.report.setFont('Helvetica-Bold', size=10)
                        Var.report.drawString(55, 675, str(items[0]))
                        Var.report.drawString(120, 675, str(items[1]))
                        Var.report.drawString(160, 675, str(items[2]))
                        Var.report.drawString(285, 675, str(items[3]))
                        Var.report.drawString(370, 675, str(items[4]))
                        Var.report.drawString(460, 675, str(items[5]))  # Nueva coordenada para "FECHA BAJA"
                        Var.report.line(50, 670, 525, 670)  # Ajusta la longitud de la línea
                        i = 55
                        j = 655
                    Var.report.setFont('Helvetica', size=9)
                    # Obtén el DNI completo
                    dni_completo = str(query.value(1))

                    # Oculta todos los dígitos del DNI excepto los últimos dos antes de la letra
                    dni_oculto = '*' * (len(dni_completo) - 2) + dni_completo[-2:]

                    Var.report.drawString(i + 15, j, str(query.value(0)))
                    Var.report.drawString(i + 60, j, dni_oculto)
                    Var.report.drawString(i + 110, j, str(query.value(2)))
                    Var.report.drawString(i + 230, j, str(query.value(3)))
                    Var.report.drawString(i + 320, j, str(query.value(4)))
                    Var.report.drawString(i + 410, j, str(query.value(5)))  # Nueva coordenada para "FECHA BAJA"
                    j = j - 25

            Var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith(nombre):
                    os.startfile(os.path.join(rootPath, file))
                    # os.startfile('%s\\%s' % (rootPath, file))
        except Exception as error:
            print('Error LISTADO CLIENTES: ', error)

    def reportDrivers(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y_%m_%d_%H_%M_%S')
            nombre = fecha + '_listadodrivers.pdf'
            Var.report = canvas.Canvas('informes/' + nombre)
            titulo = 'LISTADO DRIVERS'
            Informes.topInforme(titulo)
            Informes.footInforme(titulo)
            Var.report.drawString(250, 250, 'Mi primer informe')
            Var.report.save()
            rootPath = '.\\informes'
            for file in os.listdir(rootPath):
                if file.endswith(nombre):
                    os.startfile('%s\\%s' % (rootPath, file))

        except Exception as error:
            print('Error LISTADO DRIVERS: ', error)

    def topInforme(titulo):
        try:
            logo = ".\\img\\logo.png"
            Var.report.line(50, 800, 525, 800)
            Var.report.setFont("Helvetica-Bold", size=14)
            Var.report.drawString(55, 785, "Transportes Teis")
            Var.report.drawString(240, 695, titulo)
            Var.report.line(50, 690, 525, 690)
            Var.report.drawImage(logo, 440, 715, width=65, height=65)  # nota: no tocar dimensiones
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
