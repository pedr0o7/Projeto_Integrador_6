from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.ClienteCTR import ClienteCTR
from View.FrmCliente import Ui_FrmCliente


class Ui_frmPesqCliente(object):
    def AlterarCliente_Click(self):
        linha = self.gridCliente.currentItem().row()
        codigoCli = self.gridCliente.item(linha, 0).text()
        nome = self.gridCliente.item(linha, 1).text()
        cpf = self.gridCliente.item(linha, 2).text()
        endereco = self.gridCliente.item(linha, 3).text()
        email = self.gridCliente.item(linha, 4).text()
        telefone = self.gridCliente.item(linha, 5).text()
        self.frmCliente = QtWidgets.QMainWindow()
        self.ui = Ui_FrmCliente()
        self.ui.setupUi(self.frmCliente, 'alterar', codigoCli)
        self.ui.PreencherAlterar(nome, cpf, endereco, email, telefone)
        self.frmCliente.show()

    def ExcluirCliente_Click(self):
        linha = self.gridCliente.currentItem().row()
        codigoCli = self.gridCliente.item(linha, 0).text()
        self.gridCliente.removeRow(linha)
        cliente = ClienteCTR
        cliente.ExcluirCliente(codigoCli)
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Cliente Excluído!")
        # msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Excluir Cliente")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def PesquisarCliente(self, valor, tipo):
        if valor == '':
            self.PesquisarTodosClientes()
        else:
            cliente = ClienteCTR
            query = cliente.PesquisarCliente(self, valor, tipo)

            while (self.gridCliente.rowCount() > 0):
                self.gridCliente.removeRow(0)

            row = 0
            while query.next():
                self.gridCliente.insertRow(row)
                codCli = QtWidgets.QTableWidgetItem(str(query.value(0)))
                nome = QtWidgets.QTableWidgetItem(str(query.value(1)))
                cpf = QtWidgets.QTableWidgetItem(str(query.value(2)))
                endereco = QtWidgets.QTableWidgetItem(str(query.value(3)))
                email = QtWidgets.QTableWidgetItem(str(query.value(4)))
                telefone = QtWidgets.QTableWidgetItem(str(query.value(5)))

                self.gridCliente.setItem(row, 0, codCli)
                self.gridCliente.setItem(row, 1, nome)
                self.gridCliente.setItem(row, 2, cpf)
                self.gridCliente.setItem(row, 3, endereco)
                self.gridCliente.setItem(row, 4, email)
                self.gridCliente.setItem(row, 5, telefone)

                row = row + 1

        self.edtPesquisa.setText('')

    def PesquisarTodosClientes(self):
        cliente = ClienteCTR
        query = cliente.PesquisarTodosClientes()

        while (self.gridCliente.rowCount() > 0):
            self.gridCliente.removeRow(0)

        row = 0
        while query.next():
            self.gridCliente.insertRow(row)
            codCli = QtWidgets.QTableWidgetItem(str(query.value(0)))
            nome = QtWidgets.QTableWidgetItem(str(query.value(1)))
            cpf = QtWidgets.QTableWidgetItem(str(query.value(2)))
            endereco = QtWidgets.QTableWidgetItem(str(query.value(3)))
            email = QtWidgets.QTableWidgetItem(str(query.value(4)))
            telefone = QtWidgets.QTableWidgetItem(str(query.value(5)))

            self.gridCliente.setItem(row, 0, codCli)
            self.gridCliente.setItem(row, 1, nome)
            self.gridCliente.setItem(row, 2, cpf)
            self.gridCliente.setItem(row, 3, endereco)
            self.gridCliente.setItem(row, 4, email)
            self.gridCliente.setItem(row, 5, telefone)

            row = row + 1

    def setupUi(self, frmPesqCliente):
        frmPesqCliente.setObjectName("frmPesqCliente")
        frmPesqCliente.resize(640, 480)
        frmPesqCliente.setMinimumSize(QtCore.QSize(640, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Imagens/Lista_cliente_preto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmPesqCliente.setWindowIcon(icon)
        frmPesqCliente.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.508, y1:0.727, x2:0.505, y2:1, stop:0 rgba(255, 255, 153, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(frmPesqCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("font: 87 12pt \"Arial\"; background-color: qlineargradient(spread:pad, x1:0.508, y1:0.727, x2:0.505, y2:1, stop:0 rgba(255, 255, 153, 255), stop:1 rgba(255, 255, 255, 255))")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.cbPesquisa = QtWidgets.QComboBox(self.groupBox)
        self.cbPesquisa.setMinimumSize(QtCore.QSize(100, 30))
        self.cbPesquisa.setStyleSheet("font: 87 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.cbPesquisa.setObjectName("cbPesquisa")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.cbPesquisa.addItem("")
        self.gridLayout.addWidget(self.cbPesquisa, 0, 0, 1, 1)
        self.edtPesquisa = QtWidgets.QLineEdit(self.groupBox)
        self.edtPesquisa.setMinimumSize(QtCore.QSize(0, 30))
        self.edtPesquisa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtPesquisa.setObjectName("edtPesquisa")
        self.gridLayout.addWidget(self.edtPesquisa, 0, 1, 1, 1)
        self.btnPesquisa = QtWidgets.QPushButton(self.groupBox)
        self.btnPesquisa.setMinimumSize(QtCore.QSize(120, 50))
        self.btnPesquisa.setMaximumSize(QtCore.QSize(120, 50))
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
        self.gridLayout.addWidget(self.btnPesquisa, 0, 2, 1, 1)
        self.gridCliente = QtWidgets.QTableWidget(self.groupBox)
        self.gridCliente.setStyleSheet("font: 87 12pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.gridCliente.setObjectName("gridCliente")
        self.gridCliente.setColumnCount(6)
        self.gridCliente.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridCliente.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridCliente.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridCliente.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridCliente.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridCliente.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridCliente.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.gridCliente, 1, 0, 1, 3)
        self.btnAlterar = QtWidgets.QPushButton(self.groupBox)
        self.btnAlterar.setMinimumSize(QtCore.QSize(120, 50))
        self.btnAlterar.setMaximumSize(QtCore.QSize(120, 50))
        self.btnAlterar.setStyleSheet("QPushButton{\n"
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
        icon2.addPixmap(QtGui.QPixmap("./Imagens/Alterar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlterar.setIcon(icon2)
        self.btnAlterar.setIconSize(QtCore.QSize(35, 35))
        self.btnAlterar.setObjectName("btnAlterar")
        self.gridLayout.addWidget(self.btnAlterar, 2, 1, 1, 1, QtCore.Qt.AlignRight)
        self.btnExcluir = QtWidgets.QPushButton(self.groupBox)
        self.btnExcluir.setMinimumSize(QtCore.QSize(120, 50))
        self.btnExcluir.setMaximumSize(QtCore.QSize(120, 50))
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./Imagens/lixeira.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnExcluir.setIcon(icon3)
        self.btnExcluir.setIconSize(QtCore.QSize(30, 30))
        self.btnExcluir.setObjectName("btnExcluir")
        self.gridLayout.addWidget(self.btnExcluir, 2, 2, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        frmPesqCliente.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(frmPesqCliente)
        self.statusbar.setObjectName("statusbar")
        frmPesqCliente.setStatusBar(self.statusbar)

        self.retranslateUi(frmPesqCliente)
        QtCore.QMetaObject.connectSlotsByName(frmPesqCliente)

        # printINICIAL
        self.PesquisarTodosClientes()

        self.btnPesquisa.clicked.connect(
            lambda: self.PesquisarCliente(self.edtPesquisa.text(), self.cbPesquisa.currentText()))
        self.btnExcluir.clicked.connect(lambda: self.ExcluirCliente_Click())
        self.btnAlterar.clicked.connect(lambda: self.AlterarCliente_Click())

    def retranslateUi(self, frmPesqCliente):
        _translate = QtCore.QCoreApplication.translate
        frmPesqCliente.setWindowTitle(_translate("frmPesqCliente", "Lista de Cliente"))
        self.groupBox.setTitle(_translate("frmPesqCliente", "Selecione o Tipo de Pesquisa"))
        self.cbPesquisa.setItemText(0, _translate("frmPesqCliente", "Código"))
        self.cbPesquisa.setItemText(1, _translate("frmPesqCliente", "Nome"))
        self.cbPesquisa.setItemText(2, _translate("frmPesqCliente", "CPF"))
        self.btnPesquisa.setText(_translate("frmPesqCliente", "Pesquisar"))
        item = self.gridCliente.horizontalHeaderItem(0)
        item.setText(_translate("frmPesqCliente", "Código"))
        item = self.gridCliente.horizontalHeaderItem(1)
        item.setText(_translate("frmPesqCliente", "Nome"))
        item = self.gridCliente.horizontalHeaderItem(2)
        item.setText(_translate("frmPesqCliente", "CPF"))
        item = self.gridCliente.horizontalHeaderItem(3)
        item.setText(_translate("frmPesqCliente", "Endereço"))
        item = self.gridCliente.horizontalHeaderItem(4)
        item.setText(_translate("frmPesqCliente", "Email"))
        item = self.gridCliente.horizontalHeaderItem(5)
        item.setText(_translate("frmPesqCliente", "Telefone"))
        self.btnAlterar.setText(_translate("frmPesqCliente", "Alterar"))
        self.btnExcluir.setText(_translate("frmPesqCliente", "Excluir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmPesqCliente = QtWidgets.QMainWindow()
    ui = Ui_frmPesqCliente()
    ui.setupUi(frmPesqCliente)
    frmPesqCliente.show()
    sys.exit(app.exec_())
