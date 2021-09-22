# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FrmPesqAluguel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Controller import AluguelCTR


class Ui_FrmPesqAluguel(object):
    def DevolverVeiculo(self):
        linha = self.tableWidget_2.currentItem().row()
        codigoAlug = self.tableWidget_2.item(linha, 0).text()
        dataDevol = self.edtDevolucao.text()
        valorMulta = self.edtMulta.text()
        kmSaida = self.edtSaida.text()
        print("salve")
        aluguel= AluguelCTR
        aluguel.AluguelCTR.DevolverVeiculo(self, codigoAlug, dataDevol, valorMulta, kmSaida)
        print("roia")
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Veículo devolvido!")
        msg.setWindowTitle("Devolver Veículo")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

        self.edtDevolucao.setText('')
        self.edtMulta.setText('')
        self.edtSaida.setText('')

    def PesquisarAluguel(self, valor, tipo):
        if (valor == ''):
            self.PesquisarTodosAluguel()
        else:
            aluguel = AluguelCTR
            query = aluguel.AluguelCTR.PesquisarAluguel(self, valor, tipo)

            while (self.tableWidget_2.rowCount() > 0):
                self.tableWidget_2.removeRow(0)

            row = 0
            while query.next():
                self.tableWidget_2.insertRow(row)
                codigoAlug = QtWidgets.QTableWidgetItem(str(query.value(0)))
                Nome = QtWidgets.QTableWidgetItem(str(query.value(10)))
                CodigoCli = QtWidgets.QTableWidgetItem(str(query.value(8)))
                CodigoVeic = QtWidgets.QTableWidgetItem(str(query.value(9)))
                dataAlug = QtWidgets.QTableWidgetItem(str(query.value(1)))
                dataPrazo = QtWidgets.QTableWidgetItem(str(query.value(2)))
                dataDevolucao = QtWidgets.QTableWidgetItem(str(query.value(3)))
                valorAluguel = QtWidgets.QTableWidgetItem(str(query.value(4)))
                valorMulta = QtWidgets.QTableWidgetItem(str(query.value(5)))
                kmEntrada = QtWidgets.QTableWidgetItem(str(query.value(6)))
                kmSaida = QtWidgets.QTableWidgetItem(str(query.value(7)))

                self.tableWidget_2.setItem(row, 0, codigoAlug)
                self.tableWidget_2.setItem(row, 1, Nome)
                self.tableWidget_2.setItem(row, 2, CodigoCli)
                self.tableWidget_2.setItem(row, 3, CodigoVeic)
                self.tableWidget_2.setItem(row, 4, dataAlug)
                self.tableWidget_2.setItem(row, 5, dataPrazo)
                self.tableWidget_2.setItem(row, 6, dataDevolucao)
                self.tableWidget_2.setItem(row, 7, valorAluguel)
                self.tableWidget_2.setItem(row, 8, valorMulta)
                self.tableWidget_2.setItem(row, 9, kmEntrada)
                self.tableWidget_2.setItem(row, 10, kmSaida)
                row = row + 1

        self.edtPesquisa.setText('')

    def PesquisarTodosAluguel(self):
        aluguel = AluguelCTR
        query = aluguel.AluguelCTR.PesquisarTodosAluguel()

        while (self.tableWidget_2.rowCount() > 0):
            self.tableWidget_2.removeRow(0)

        row = 0
        while query.next():
            self.tableWidget_2.insertRow(row)
            codigoAlug = QtWidgets.QTableWidgetItem(str(query.value(0)))
            Nome = QtWidgets.QTableWidgetItem(str(query.value(10)))
            CodigoCli = QtWidgets.QTableWidgetItem(str(query.value(8)))
            CodigoVeic = QtWidgets.QTableWidgetItem(str(query.value(9)))
            dataAlug = QtWidgets.QTableWidgetItem(str(query.value(1)))
            dataPrazo = QtWidgets.QTableWidgetItem(str(query.value(2)))
            dataDevolucao = QtWidgets.QTableWidgetItem(str(query.value(3)))
            valorAluguel = QtWidgets.QTableWidgetItem(str(query.value(4)))
            valorMulta = QtWidgets.QTableWidgetItem(str(query.value(5)))
            kmEntrada = QtWidgets.QTableWidgetItem(str(query.value(6)))
            kmSaida = QtWidgets.QTableWidgetItem(str(query.value(7)))

            self.tableWidget_2.setItem(row, 0, codigoAlug)
            self.tableWidget_2.setItem(row, 1, Nome)
            self.tableWidget_2.setItem(row, 2, CodigoCli)
            self.tableWidget_2.setItem(row, 3, CodigoVeic)
            self.tableWidget_2.setItem(row, 4, dataAlug)
            self.tableWidget_2.setItem(row, 5, dataPrazo)
            self.tableWidget_2.setItem(row, 6, dataDevolucao)
            self.tableWidget_2.setItem(row, 7, valorAluguel)
            self.tableWidget_2.setItem(row, 8, valorMulta)
            self.tableWidget_2.setItem(row, 9, kmEntrada)
            self.tableWidget_2.setItem(row, 10, kmSaida)

        row = row + 1

    def setupUi(self, FrmPesqAluguel):
        FrmPesqAluguel.setObjectName("FrmPesqAluguel")
        FrmPesqAluguel.resize(1124, 716)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FrmPesqAluguel.sizePolicy().hasHeightForWidth())
        FrmPesqAluguel.setSizePolicy(sizePolicy)
        FrmPesqAluguel.setMinimumSize(QtCore.QSize(1124, 716))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Imagens/Lista_aluguel_preto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmPesqAluguel.setWindowIcon(icon)
        FrmPesqAluguel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.508, y1:0.727, x2:0.505, y2:1, stop:0 rgba(255, 255, 153, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(FrmPesqAluguel)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbPesquisa = QtWidgets.QComboBox(self.centralwidget)
        self.cbPesquisa.setMinimumSize(QtCore.QSize(0, 30))
        self.cbPesquisa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbPesquisa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cbPesquisa.setObjectName("cbPesquisa")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.horizontalLayout.addWidget(self.cbPesquisa)
        self.edtPesquisa = QtWidgets.QLineEdit(self.centralwidget)
        self.edtPesquisa.setMinimumSize(QtCore.QSize(0, 30))
        self.edtPesquisa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtPesquisa.setObjectName("edtPesquisa")
        self.horizontalLayout.addWidget(self.edtPesquisa)
        self.btnPesquisa = QtWidgets.QPushButton(self.centralwidget)
        self.btnPesquisa.setMinimumSize(QtCore.QSize(120, 50))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Imagens/Pesquisar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnPesquisa.setIcon(icon1)
        self.btnPesquisa.setIconSize(QtCore.QSize(30, 30))
        self.btnPesquisa.setObjectName("btnPesquisa")
        self.horizontalLayout.addWidget(self.btnPesquisa)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setStyleSheet("font: 87 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(11)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setHorizontalHeaderItem(10, item)
        self.verticalLayout.addWidget(self.tableWidget_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edtDevolucao = QtWidgets.QLineEdit(self.centralwidget)
        self.edtDevolucao.setMinimumSize(QtCore.QSize(0, 30))
        self.edtDevolucao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtDevolucao.setObjectName("edtDevolucao")
        self.horizontalLayout_3.addWidget(self.edtDevolucao)
        self.edtMulta = QtWidgets.QLineEdit(self.centralwidget)
        self.edtMulta.setMinimumSize(QtCore.QSize(0, 30))
        self.edtMulta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtMulta.setObjectName("edtMulta")
        self.horizontalLayout_3.addWidget(self.edtMulta)
        self.edtSaida = QtWidgets.QLineEdit(self.centralwidget)
        self.edtSaida.setMinimumSize(QtCore.QSize(0, 30))
        self.edtSaida.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtSaida.setObjectName("edtSaida")
        self.horizontalLayout_3.addWidget(self.edtSaida)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.btnDevolver = QtWidgets.QPushButton(self.centralwidget)
        self.btnDevolver.setMinimumSize(QtCore.QSize(120, 50))
        self.btnDevolver.setMaximumSize(QtCore.QSize(120, 50))
        self.btnDevolver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDevolver.setStyleSheet("QPushButton{\n"
"border-radius: 5px;\n"
"background-color: rgb(20,20,20);\n"
"color:rgb(200,200,200);\n"
"font: 87 12pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton:hover{ \n"
"background-color:rgb(0,0, 0);\n"
"color: rbg(200,200,200)\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(0,0,30);\n"
"color:rbg(200,200,200)\n"
"}\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Imagens/Devolver.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDevolver.setIcon(icon2)
        self.btnDevolver.setIconSize(QtCore.QSize(30, 30))
        self.btnDevolver.setObjectName("btnDevolver")
        self.verticalLayout_2.addWidget(self.btnDevolver, 0, QtCore.Qt.AlignRight)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        FrmPesqAluguel.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FrmPesqAluguel)
        self.statusbar.setObjectName("statusbar")
        FrmPesqAluguel.setStatusBar(self.statusbar)

        self.retranslateUi(FrmPesqAluguel)
        QtCore.QMetaObject.connectSlotsByName(FrmPesqAluguel)

        self.PesquisarTodosAluguel()
        # BTN PESQUISAR CLICK #
        self.btnPesquisa.clicked.connect(
            lambda: self.PesquisarAluguel(self.edtPesquisa.text(), self.cbPesquisa.currentText()))
        # btn DEVOLVER click
        self.btnDevolver.clicked.connect(lambda: self.DevolverVeiculo())

    def retranslateUi(self, FrmPesqAluguel):
        _translate = QtCore.QCoreApplication.translate
        FrmPesqAluguel.setWindowTitle(_translate("FrmPesqAluguel", "Lista de Alugueis"))
        FrmPesqAluguel.setToolTip(_translate("FrmPesqAluguel", "<html><head/><body><p>FrmPesqAluguel</p></body></html>"))
        self.label_5.setText(_translate("FrmPesqAluguel", "Selecione o Tipo de Pesquisa"))
        self.cbPesquisa.setItemText(0, _translate("FrmPesqAluguel", "Código Aluguel"))
        self.cbPesquisa.setItemText(1, _translate("FrmPesqAluguel", "Código Cliente"))
        self.cbPesquisa.setItemText(2, _translate("FrmPesqAluguel", "Código Veículo"))
        self.cbPesquisa.setItemText(3, _translate("FrmPesqAluguel", "Nome Cliente"))
        self.btnPesquisa.setText(_translate("FrmPesqAluguel", "Pesquisar"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("FrmPesqAluguel", "Código Aluguel"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("FrmPesqAluguel", "Nome Cliente"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("FrmPesqAluguel", "Código Cliente"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("FrmPesqAluguel", "Código Veiculo"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("FrmPesqAluguel", "Data Aluguel"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("FrmPesqAluguel", "Data Prazo"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("FrmPesqAluguel", "Data Devolução"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("FrmPesqAluguel", "Valor Aluguel"))
        item = self.tableWidget_2.horizontalHeaderItem(8)
        item.setText(_translate("FrmPesqAluguel", "Valor Multa"))
        item = self.tableWidget_2.horizontalHeaderItem(9)
        item.setText(_translate("FrmPesqAluguel", "Km Entrada"))
        item = self.tableWidget_2.horizontalHeaderItem(10)
        item.setText(_translate("FrmPesqAluguel", "Km Devolução"))
        self.label_4.setText(_translate("FrmPesqAluguel", "Devolução de Veiculo"))
        self.label.setText(_translate("FrmPesqAluguel", "Data Devolução"))
        self.label_2.setText(_translate("FrmPesqAluguel", "Multa"))
        self.label_3.setText(_translate("FrmPesqAluguel", "Km de Devolução"))
        self.btnDevolver.setText(_translate("FrmPesqAluguel", "Devolver"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmPesqAluguel = QtWidgets.QMainWindow()
    ui = Ui_FrmPesqAluguel()
    ui.setupUi(FrmPesqAluguel)
    FrmPesqAluguel.show()
    sys.exit(app.exec_())
