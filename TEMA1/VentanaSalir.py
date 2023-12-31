# Form implementation generated from reading ui file '.\templates\VentanaSalir.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ventanaDeseaSalir(object):
    def setupUi(self, ventanaDeseaSalir):
        ventanaDeseaSalir.setObjectName("ventanaDeseaSalir")
        ventanaDeseaSalir.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        ventanaDeseaSalir.resize(310, 116)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ventanaDeseaSalir.sizePolicy().hasHeightForWidth())
        ventanaDeseaSalir.setSizePolicy(sizePolicy)
        ventanaDeseaSalir.setMinimumSize(QtCore.QSize(310, 116))
        ventanaDeseaSalir.setMaximumSize(QtCore.QSize(310, 116))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\templates\\../img/salir.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        ventanaDeseaSalir.setWindowIcon(icon)
        ventanaDeseaSalir.setStyleSheet("background-color: white;")
        ventanaDeseaSalir.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(ventanaDeseaSalir)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=ventanaDeseaSalir)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblDeseaSalir = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.lblDeseaSalir.setFont(font)
        self.lblDeseaSalir.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.lblDeseaSalir.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblDeseaSalir.setObjectName("lblDeseaSalir")
        self.horizontalLayout_2.addWidget(self.lblDeseaSalir)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(parent=ventanaDeseaSalir)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnAceptar = QtWidgets.QPushButton(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAceptar.sizePolicy().hasHeightForWidth())
        self.btnAceptar.setSizePolicy(sizePolicy)
        self.btnAceptar.setMinimumSize(QtCore.QSize(93, 23))
        self.btnAceptar.setMaximumSize(QtCore.QSize(93, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.horizontalLayout.addWidget(self.btnAceptar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnCancelar = QtWidgets.QPushButton(parent=self.widget_2)
        self.btnCancelar.setMaximumSize(QtCore.QSize(100, 23))
        self.btnCancelar.setObjectName("btnCancelar")
        self.horizontalLayout.addWidget(self.btnCancelar)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(ventanaDeseaSalir)
        QtCore.QMetaObject.connectSlotsByName(ventanaDeseaSalir)

    def retranslateUi(self, ventanaDeseaSalir):
        _translate = QtCore.QCoreApplication.translate
        ventanaDeseaSalir.setWindowTitle(_translate("ventanaDeseaSalir", "Ventana Salir"))
        self.lblDeseaSalir.setText(_translate("ventanaDeseaSalir", "¿Desea Salir?"))
        self.btnAceptar.setText(_translate("ventanaDeseaSalir", "Aceptar"))
        self.btnCancelar.setText(_translate("ventanaDeseaSalir", "Cancelar"))
