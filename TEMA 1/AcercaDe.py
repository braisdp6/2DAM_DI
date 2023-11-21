# Form implementation generated from reading ui file '.\templates\AcercaDe.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ventanaAcercaDe(object):
    def setupUi(self, ventanaAcercaDe):
        ventanaAcercaDe.setObjectName("ventanaAcercaDe")
        ventanaAcercaDe.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        ventanaAcercaDe.resize(518, 403)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ventanaAcercaDe.sizePolicy().hasHeightForWidth())
        ventanaAcercaDe.setSizePolicy(sizePolicy)
        ventanaAcercaDe.setMinimumSize(QtCore.QSize(518, 403))
        ventanaAcercaDe.setMaximumSize(QtCore.QSize(518, 403))
        ventanaAcercaDe.setStyleSheet("background-color: white;")
        ventanaAcercaDe.setModal(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout(ventanaAcercaDe)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=ventanaAcercaDe)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frameImagen = QtWidgets.QFrame(parent=self.frame)
        self.frameImagen.setObjectName("frameImagen")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameImagen)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(parent=self.frameImagen)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblAcercade = QtWidgets.QLabel(parent=self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(120)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAcercade.sizePolicy().hasHeightForWidth())
        self.lblAcercade.setSizePolicy(sizePolicy)
        self.lblAcercade.setMinimumSize(QtCore.QSize(120, 120))
        self.lblAcercade.setMaximumSize(QtCore.QSize(120, 120))
        self.lblAcercade.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.lblAcercade.setText("")
        self.lblAcercade.setPixmap(QtGui.QPixmap(".\\templates\\../img/acercade.png"))
        self.lblAcercade.setObjectName("lblAcercade")
        self.horizontalLayout_4.addWidget(self.lblAcercade)
        self.horizontalLayout_2.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(parent=self.frameImagen)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.widget_3.setFont(font)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lblCt = QtWidgets.QLabel(parent=self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblCt.setFont(font)
        self.lblCt.setObjectName("lblCt")
        self.verticalLayout_2.addWidget(self.lblCt)
        self.lblCarTeis = QtWidgets.QLabel(parent=self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblCarTeis.setFont(font)
        self.lblCarTeis.setObjectName("lblCarTeis")
        self.verticalLayout_2.addWidget(self.lblCarTeis)
        self.lblVersion = QtWidgets.QLabel(parent=self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblVersion.setFont(font)
        self.lblVersion.setObjectName("lblVersion")
        self.verticalLayout_2.addWidget(self.lblVersion)
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.frameImagen)
        self.frameDescripcion = QtWidgets.QFrame(parent=self.frame)
        self.frameDescripcion.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameDescripcion.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameDescripcion.setObjectName("frameDescripcion")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameDescripcion)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_2 = QtWidgets.QWidget(parent=self.frameDescripcion)
        self.widget_2.setMinimumSize(QtCore.QSize(450, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setItalic(False)
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lblFecha = QtWidgets.QLabel(parent=self.widget_2)
        self.lblFecha.setText("")
        self.lblFecha.setObjectName("lblFecha")
        self.verticalLayout_3.addWidget(self.lblFecha)
        self.lblProyecto = QtWidgets.QLabel(parent=self.widget_2)
        self.lblProyecto.setObjectName("lblProyecto")
        self.verticalLayout_3.addWidget(self.lblProyecto)
        self.lblCurso = QtWidgets.QLabel(parent=self.widget_2)
        self.lblCurso.setObjectName("lblCurso")
        self.verticalLayout_3.addWidget(self.lblCurso)
        self.lblInstituto = QtWidgets.QLabel(parent=self.widget_2)
        self.lblInstituto.setObjectName("lblInstituto")
        self.verticalLayout_3.addWidget(self.lblInstituto)
        self.horizontalLayout_3.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.frameDescripcion)
        self.widget_4 = QtWidgets.QWidget(parent=self.frame)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.btnAceptar = QtWidgets.QPushButton(parent=self.widget_4)
        self.btnAceptar.setObjectName("btnAceptar")
        self.horizontalLayout_5.addWidget(self.btnAceptar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(ventanaAcercaDe)
        QtCore.QMetaObject.connectSlotsByName(ventanaAcercaDe)

    def retranslateUi(self, ventanaAcercaDe):
        _translate = QtCore.QCoreApplication.translate
        ventanaAcercaDe.setWindowTitle(_translate("ventanaAcercaDe", "Acerca de..."))
        self.lblCt.setText(_translate("ventanaAcercaDe", "CT"))
        self.lblCarTeis.setText(_translate("ventanaAcercaDe", "CAR TEIS"))
        self.lblVersion.setText(_translate("ventanaAcercaDe", "Version: "))
        self.lblProyecto.setText(_translate("ventanaAcercaDe", "Proyecto INTERFACES GRAFICAS"))
        self.lblCurso.setText(_translate("ventanaAcercaDe", "Desarrollo Aplicaciones Multiplataforma"))
        self.lblInstituto.setText(_translate("ventanaAcercaDe", "2023 - Ies de Teis"))
        self.btnAceptar.setText(_translate("ventanaAcercaDe", "Aceptar"))
