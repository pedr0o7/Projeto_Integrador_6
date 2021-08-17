# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\PyCharm\projetos\Projeto_Integrador_6\View\UI\frmPesqVeiculos.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmPesqVeiculos(object):
    def setupUi(self, frmPesqVeiculos):
        frmPesqVeiculos.setObjectName("frmPesqVeiculos")
        frmPesqVeiculos.resize(820, 491)
        frmPesqVeiculos.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.508, y1:0.727, x2:0.505, y2:1, stop:0 rgba(255, 255, 153, 255), stop:1 rgba(255, 255, 255, 255))")
        self.groupBox = QtWidgets.QGroupBox(frmPesqVeiculos)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 801, 81))
        self.groupBox.setStyleSheet("font: 87 10pt \"Arial\";")
        self.groupBox.setObjectName("groupBox")
        self.edtPesquisa_2 = QtWidgets.QLineEdit(self.groupBox)
        self.edtPesquisa_2.setGeometry(QtCore.QRect(140, 40, 521, 20))
        self.edtPesquisa_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtPesquisa_2.setObjectName("edtPesquisa_2")
        self.btnPesquisa = QtWidgets.QPushButton(self.groupBox)
        self.btnPesquisa.setGeometry(QtCore.QRect(670, 30, 121, 41))
        self.btnPesquisa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPesquisa.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"background-color: rgb(20,20,20);\n"
"color:rgb(200,200,200);\n"
"font: 87 12pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color:rgb(0, 0, 0);\n"
"color: rbg(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(0,0,30);\n"
"color:rbg(200,200,200)\n"
"}\n"
"\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\PyCharm\\projetos\\Projeto_Integrador_6\\View\\UI\\../../Imagens/Pesquisar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisa.setIcon(icon)
        self.btnPesquisa.setIconSize(QtCore.QSize(30, 30))
        self.btnPesquisa.setObjectName("btnPesquisa")
        self.cbPesquisa = QtWidgets.QComboBox(self.groupBox)
        self.cbPesquisa.setGeometry(QtCore.QRect(10, 40, 121, 22))
        self.cbPesquisa.setStyleSheet("font: 87 10pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.cbPesquisa.setObjectName("cbPesquisa")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.btnAlterar_2 = QtWidgets.QPushButton(frmPesqVeiculos)
        self.btnAlterar_2.setGeometry(QtCore.QRect(600, 400, 101, 51))
        self.btnAlterar_2.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"background-color: rgb(20,20,20);\n"
"color:rgb(200,200,200);\n"
"font: 87 12pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color:rgb(0, 0, 0);\n"
"color: rbg(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(0,0,30);\n"
"color:rbg(200,200,200)\n"
"}\n"
"\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\PyCharm\\projetos\\Projeto_Integrador_6\\View\\UI\\../../Imagens/Alterar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlterar_2.setIcon(icon1)
        self.btnAlterar_2.setIconSize(QtCore.QSize(35, 35))
        self.btnAlterar_2.setObjectName("btnAlterar_2")
        self.btnExcluir = QtWidgets.QPushButton(frmPesqVeiculos)
        self.btnExcluir.setGeometry(QtCore.QRect(710, 400, 101, 51))
        self.btnExcluir.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"background-color: rgb(20,20,20);\n"
"color:rgb(200,200,200);\n"
"font: 87 12pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color:rgb(0, 0, 0);\n"
"color: rbg(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(0,0,30);\n"
"color:rbg(200,200,200)\n"
"}\n"
"\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\PyCharm\\projetos\\Projeto_Integrador_6\\View\\UI\\../../Imagens/lixeira.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExcluir.setIcon(icon2)
        self.btnExcluir.setIconSize(QtCore.QSize(30, 30))
        self.btnExcluir.setObjectName("btnExcluir")
        self.gridVeiculos = QtWidgets.QTableWidget(frmPesqVeiculos)
        self.gridVeiculos.setGeometry(QtCore.QRect(10, 100, 801, 281))
        self.gridVeiculos.setStyleSheet("alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 87 10pt \"Arial\";")
        self.gridVeiculos.setObjectName("gridVeiculos")
        self.gridVeiculos.setColumnCount(11)
        self.gridVeiculos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.gridVeiculos.setHorizontalHeaderItem(10, item)

        self.retranslateUi(frmPesqVeiculos)
        QtCore.QMetaObject.connectSlotsByName(frmPesqVeiculos)

    def retranslateUi(self, frmPesqVeiculos):
        _translate = QtCore.QCoreApplication.translate
        frmPesqVeiculos.setWindowTitle(_translate("frmPesqVeiculos", "Lista de Cliente"))
        self.groupBox.setTitle(_translate("frmPesqVeiculos", "Selecione o Tipo de Pesquisa"))
        self.btnPesquisa.setText(_translate("frmPesqVeiculos", "Pesquisar"))
        self.cbPesquisa.setItemText(0, _translate("frmPesqVeiculos", "Código"))
        self.cbPesquisa.setItemText(1, _translate("frmPesqVeiculos", "Marca"))
        self.cbPesquisa.setItemText(2, _translate("frmPesqVeiculos", "Modelo"))
        self.cbPesquisa.setItemText(3, _translate("frmPesqVeiculos", "Disponível"))
        self.cbPesquisa.setItemText(4, _translate("frmPesqVeiculos", "Alugado"))
        self.btnAlterar_2.setText(_translate("frmPesqVeiculos", "Alterar"))
        self.btnExcluir.setText(_translate("frmPesqVeiculos", "Excluir"))
        item = self.gridVeiculos.horizontalHeaderItem(0)
        item.setText(_translate("frmPesqVeiculos", "Código"))
        item = self.gridVeiculos.horizontalHeaderItem(1)
        item.setText(_translate("frmPesqVeiculos", "Modelo"))
        item = self.gridVeiculos.horizontalHeaderItem(2)
        item.setText(_translate("frmPesqVeiculos", "Marca"))
        item = self.gridVeiculos.horizontalHeaderItem(3)
        item.setText(_translate("frmPesqVeiculos", "Ano"))
        item = self.gridVeiculos.horizontalHeaderItem(4)
        item.setText(_translate("frmPesqVeiculos", "Placa"))
        item = self.gridVeiculos.horizontalHeaderItem(5)
        item.setText(_translate("frmPesqVeiculos", "Alugado"))
        item = self.gridVeiculos.horizontalHeaderItem(6)
        item.setText(_translate("frmPesqVeiculos", "Batido"))
        item = self.gridVeiculos.horizontalHeaderItem(7)
        item.setText(_translate("frmPesqVeiculos", "kmAtual"))
        item = self.gridVeiculos.horizontalHeaderItem(8)
        item.setText(_translate("frmPesqVeiculos", "Valor da Diária"))
        item = self.gridVeiculos.horizontalHeaderItem(9)
        item.setText(_translate("frmPesqVeiculos", "descricao"))
        item = self.gridVeiculos.horizontalHeaderItem(10)
        item.setText(_translate("frmPesqVeiculos", "Tipo do Veículo"))
