from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.AluguelCTR import AluguelCTR
from Controller.ClienteCTR import ClienteCTR
from Controller.VeiculoCTR import VeiculoCTR

class Ui_FrmAluguel(object):
    def btnSalvar_Click(self):
        linha = self.gridCliente.currentItem().row()
        codigoCli = self.gridCliente.item(linha, 0).text()
        linha = self.gridVeiculo.currentItem().row()
        codigoVeic = self.gridVeiculo.item(linha, 0).text()

        DataAluguel = self.EdtDataAluguel.text()
        DataPrazo = self.EdtPrazo.text()

        ValorAluguel = self.EdtValor.text()
        ValorMulta = self.EdtMulta.text()
        KmEntrada = self.EdtkmEntrada.text()


        aluguel = AluguelCTR
        aluguel.CadastrarAluguel(self,DataAluguel, DataPrazo, ValorAluguel,
                      ValorMulta, KmEntrada, codigoCli, codigoVeic)

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Aluguel cadastrado com sucesso!")
        msg.setWindowTitle("Cadastro de  Aluguel")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

        self.EdtDataAluguel.setText('')
        self.EdtPrazo.setText('')

        self.EdtValor.setText('')
        self.EdtMulta.setText('')
        self.EdtkmEntrada.setText('')



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

    def PesquisarCliente(self, valor, tipo):
        if valor == '':
            self.PesquisarTodosClientes()
        else:
            cliente = ClienteCTR
            query = cliente.PesquisarCliente(self,valor, tipo)

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

    def PesquisarVeiculo(self, valor, tipo):
        if (valor == '') :
            self.PesquisarVeiculosDisponiveis()
        else:
            veiculo = VeiculoCTR
            query = veiculo.PesquisarVeiculo(self,valor, tipo)

            while (self.gridVeiculo.rowCount() > 0):
                self.gridVeiculo.removeRow(0)

            row = 0
            while query.next():
                self.gridVeiculo.insertRow(row)
                codigoVeic = QtWidgets.QTableWidgetItem(str(query.value(0)))
                modelo = QtWidgets.QTableWidgetItem(str(query.value(1)))
                marca = QtWidgets.QTableWidgetItem(str(query.value(2)))
                anoModelo = QtWidgets.QTableWidgetItem(str(query.value(3)))
                placa = QtWidgets.QTableWidgetItem(str(query.value(4)))
                alugado = QtWidgets.QTableWidgetItem(str(query.value(5)))
                batido = QtWidgets.QTableWidgetItem(str(query.value(6)))
                kmAtual = QtWidgets.QTableWidgetItem(str(query.value(7)))
                valorDiaria = QtWidgets.QTableWidgetItem(str(query.value(8)))
                descricao = QtWidgets.QTableWidgetItem(str(query.value(9)))
                tipoVeiculo = QtWidgets.QTableWidgetItem(str(query.value(10)))

                self.gridVeiculo.setItem(row, 0, codigoVeic)
                self.gridVeiculo.setItem(row, 1, modelo)
                self.gridVeiculo.setItem(row, 2, marca)
                self.gridVeiculo.setItem(row, 3, anoModelo)
                self.gridVeiculo.setItem(row, 4, placa)
                self.gridVeiculo.setItem(row, 5, alugado)
                self.gridVeiculo.setItem(row, 6, batido)
                self.gridVeiculo.setItem(row, 7, kmAtual)
                self.gridVeiculo.setItem(row, 8, valorDiaria)
                self.gridVeiculo.setItem(row, 9, descricao)
                self.gridVeiculo.setItem(row, 10, tipoVeiculo)

                row = row + 1

    def PesquisarVeiculosDisponiveis(self):
        veiculo = VeiculoCTR
        query = veiculo.PesquisarVeiculosDisponiveis()

        while (self.gridVeiculo.rowCount() > 0):
                self.gridVeiculo.removeRow(0)

        row = 0
        while query.next():
            self.gridVeiculo.insertRow(row)
            codigoVeic = QtWidgets.QTableWidgetItem(str(query.value(0)))
            modelo = QtWidgets.QTableWidgetItem(str(query.value(1)))
            marca = QtWidgets.QTableWidgetItem(str(query.value(2)))
            anoModelo = QtWidgets.QTableWidgetItem(str(query.value(3)))
            placa = QtWidgets.QTableWidgetItem(str(query.value(4)))
            alugado = QtWidgets.QTableWidgetItem(str(query.value(5)))
            batido = QtWidgets.QTableWidgetItem(str(query.value(6)))
            kmAtual = QtWidgets.QTableWidgetItem(str(query.value(7)))
            valorDiaria = QtWidgets.QTableWidgetItem(str(query.value(8)))
            descricao = QtWidgets.QTableWidgetItem(str(query.value(9)))
            tipoVeiculo = QtWidgets.QTableWidgetItem(str(query.value(10)))

            self.gridVeiculo.setItem(row, 0, codigoVeic)
            self.gridVeiculo.setItem(row, 1, modelo)
            self.gridVeiculo.setItem(row, 2, marca)
            self.gridVeiculo.setItem(row, 3, anoModelo)
            self.gridVeiculo.setItem(row, 4, placa)
            self.gridVeiculo.setItem(row, 5, alugado)
            self.gridVeiculo.setItem(row, 6, batido)
            self.gridVeiculo.setItem(row, 7, kmAtual)
            self.gridVeiculo.setItem(row, 8, valorDiaria)
            self.gridVeiculo.setItem(row, 9, descricao)
            self.gridVeiculo.setItem(row, 10, tipoVeiculo)

            row = row + 1

    def setupUi(self, FrmAluguel):
        FrmAluguel.setObjectName("FrmAluguel")
        FrmAluguel.resize(1066, 801)
        FrmAluguel.setMinimumSize(QtCore.QSize(1066, 801))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Imagens/Aluguel_veiculo_preto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmAluguel.setWindowIcon(icon)
        FrmAluguel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.508, y1:0.727, x2:0.505, y2:1, stop:0 rgba(255, 255, 153, 255), stop:1 rgba(255, 255, 255, 255));")
        self.centralwidget = QtWidgets.QWidget(FrmAluguel)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("font: 87 12pt \"Arial\";")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.EdtValor = QtWidgets.QLineEdit(self.groupBox)
        self.EdtValor.setMinimumSize(QtCore.QSize(0, 30))
        self.EdtValor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EdtValor.setObjectName("EdtValor")
        self.gridLayout_2.addWidget(self.EdtValor, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 3, 1, 1)
        self.EdtPrazo = QtWidgets.QLineEdit(self.groupBox)
        self.EdtPrazo.setMinimumSize(QtCore.QSize(0, 30))
        self.EdtPrazo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EdtPrazo.setObjectName("EdtPrazo")
        self.gridLayout_2.addWidget(self.EdtPrazo, 1, 1, 1, 1)
        self.EdtMulta = QtWidgets.QLineEdit(self.groupBox)
        self.EdtMulta.setMinimumSize(QtCore.QSize(0, 30))
        self.EdtMulta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EdtMulta.setObjectName("EdtMulta")
        self.gridLayout_2.addWidget(self.EdtMulta, 1, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 2, 1, 1)
        self.EdtDataAluguel = QtWidgets.QLineEdit(self.groupBox)
        self.EdtDataAluguel.setMinimumSize(QtCore.QSize(0, 30))
        self.EdtDataAluguel.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EdtDataAluguel.setObjectName("EdtDataAluguel")
        self.gridLayout_2.addWidget(self.EdtDataAluguel, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 4, 1, 1)
        self.EdtkmEntrada = QtWidgets.QLineEdit(self.groupBox)
        self.EdtkmEntrada.setMinimumSize(QtCore.QSize(0, 30))
        self.EdtkmEntrada.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EdtkmEntrada.setObjectName("EdtkmEntrada")
        self.gridLayout_2.addWidget(self.EdtkmEntrada, 1, 4, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setStyleSheet("font: 87 12pt \"Arial\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.btnPesqVeic = QtWidgets.QPushButton(self.groupBox_2)
        self.btnPesqVeic.setEnabled(True)
        self.btnPesqVeic.setMinimumSize(QtCore.QSize(120, 50))
        self.btnPesqVeic.setMaximumSize(QtCore.QSize(120, 50))
        self.btnPesqVeic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPesqVeic.setStyleSheet("QPushButton{\n"
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
        self.btnPesqVeic.setIcon(icon1)
        self.btnPesqVeic.setIconSize(QtCore.QSize(30, 30))
        self.btnPesqVeic.setObjectName("btnPesqVeic")
        self.gridLayout_3.addWidget(self.btnPesqVeic, 0, 2, 2, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 2)
        self.EdtPesqCliente = QtWidgets.QLineEdit(self.groupBox_2)
        self.EdtPesqCliente.setMinimumSize(QtCore.QSize(0, 30))
        self.EdtPesqCliente.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EdtPesqCliente.setObjectName("EdtPesqCliente")
        self.gridLayout_3.addWidget(self.EdtPesqCliente, 1, 1, 1, 1)
        self.cbPesqCliente = QtWidgets.QComboBox(self.groupBox_2)
        self.cbPesqCliente.setMinimumSize(QtCore.QSize(100, 30))
        self.cbPesqCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbPesqCliente.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.cbPesqCliente.setObjectName("cbPesqCliente")
        self.cbPesqCliente.addItem("")
        self.cbPesqCliente.addItem("")
        self.cbPesqCliente.addItem("")
        self.gridLayout_3.addWidget(self.cbPesqCliente, 1, 0, 1, 1)
        self.gridCliente = QtWidgets.QTableWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridCliente.sizePolicy().hasHeightForWidth())
        self.gridCliente.setSizePolicy(sizePolicy)
        self.gridCliente.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"border-color: rgb(4, 4, 4);")
        self.gridCliente.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.gridCliente.setShowGrid(True)
        self.gridCliente.setGridStyle(QtCore.Qt.SolidLine)
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
        self.gridLayout_3.addWidget(self.gridCliente, 2, 0, 1, 3)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setStyleSheet("font: 87 12pt \"Arial\";")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 2)
        self.btnPesqVeic_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.btnPesqVeic_2.setMinimumSize(QtCore.QSize(120, 50))
        self.btnPesqVeic_2.setMaximumSize(QtCore.QSize(120, 50))
        self.btnPesqVeic_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPesqVeic_2.setStyleSheet("QPushButton{\n"
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
        self.btnPesqVeic_2.setIcon(icon1)
        self.btnPesqVeic_2.setIconSize(QtCore.QSize(30, 30))
        self.btnPesqVeic_2.setObjectName("btnPesqVeic_2")
        self.gridLayout_4.addWidget(self.btnPesqVeic_2, 0, 2, 2, 1)
        self.cbPesqVeic = QtWidgets.QComboBox(self.groupBox_3)
        self.cbPesqVeic.setMinimumSize(QtCore.QSize(100, 30))
        self.cbPesqVeic.setMaximumSize(QtCore.QSize(100, 30))
        self.cbPesqVeic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cbPesqVeic.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.cbPesqVeic.setObjectName("cbPesqVeic")
        self.cbPesqVeic.addItem("")
        self.cbPesqVeic.addItem("")
        self.cbPesqVeic.addItem("")
        self.cbPesqVeic.addItem("")
        self.cbPesqVeic.addItem("")
        self.gridLayout_4.addWidget(self.cbPesqVeic, 1, 0, 1, 1)
        self.gridVeiculo = QtWidgets.QTableWidget(self.groupBox_3)
        self.gridVeiculo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.gridVeiculo.setObjectName("gridVeiculo")
        self.gridVeiculo.setColumnCount(11)
        self.gridVeiculo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridVeiculo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridVeiculo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridVeiculo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridVeiculo.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridVeiculo.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridVeiculo.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridVeiculo.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridVeiculo.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridVeiculo.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridVeiculo.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.gridVeiculo.setHorizontalHeaderItem(10, item)
        self.gridLayout_4.addWidget(self.gridVeiculo, 3, 0, 1, 3)
        self.EdtPesqVeiculo = QtWidgets.QLineEdit(self.groupBox_3)
        self.EdtPesqVeiculo.setMinimumSize(QtCore.QSize(0, 30))
        self.EdtPesqVeiculo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.EdtPesqVeiculo.setObjectName("EdtPesqVeiculo")
        self.gridLayout_4.addWidget(self.EdtPesqVeiculo, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.btnSalvar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalvar.setEnabled(False)
        self.btnSalvar.setMinimumSize(QtCore.QSize(120, 50))
        self.btnSalvar.setMaximumSize(QtCore.QSize(120, 50))
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSalvar.setAutoFillBackground(False)
        self.btnSalvar.setStyleSheet("QPushButton{\n"
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
        icon2.addPixmap(QtGui.QPixmap("./Imagens/Salvar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon2)
        self.btnSalvar.setIconSize(QtCore.QSize(35, 35))
        self.btnSalvar.setObjectName("btnSalvar")
        self.gridLayout.addWidget(self.btnSalvar, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        FrmAluguel.setCentralWidget(self.centralwidget)

        self.retranslateUi(FrmAluguel)
        QtCore.QMetaObject.connectSlotsByName(FrmAluguel)


        self.btnPesqVeic.clicked.connect(lambda: self.PesquisarCliente(self.EdtPesqCliente.text(), self.cbPesqCliente.currentText()))
        self.btnPesqVeic_2.clicked.connect(lambda: self.PesquisarVeiculo(self.EdtPesqVeiculo.text(), self.cbPesqVeic.currentText()))
        self.btnSalvar.clicked.connect(self.btnSalvar_Click)

        self.PesquisarTodosClientes()
        self.PesquisarVeiculosDisponiveis()

    def retranslateUi(self, FrmAluguel):
        _translate = QtCore.QCoreApplication.translate
        FrmAluguel.setWindowTitle(_translate("FrmAluguel", "Aluguel de Veículos"))
        self.label.setText(_translate("FrmAluguel", "Data do Aluguel"))
        self.label_5.setText(_translate("FrmAluguel", "Valor Multa"))
        self.label_4.setText(_translate("FrmAluguel", "Valor Aluguel"))
        self.label_2.setText(_translate("FrmAluguel", "Prazo de Entrega"))
        self.label_6.setText(_translate("FrmAluguel", "Km Atual"))
        self.groupBox_2.setTitle(_translate("FrmAluguel", "Selecione o Cliente"))
        self.btnPesqVeic.setText(_translate("FrmAluguel", "Pesquisar"))
        self.label_8.setText(_translate("FrmAluguel", "Tipo de Pesquisa"))
        self.cbPesqCliente.setItemText(0, _translate("FrmAluguel", "Código"))
        self.cbPesqCliente.setItemText(1, _translate("FrmAluguel", "Nome"))
        self.cbPesqCliente.setItemText(2, _translate("FrmAluguel", "CPF"))
        item = self.gridCliente.horizontalHeaderItem(0)
        item.setText(_translate("FrmAluguel", "Código"))
        item = self.gridCliente.horizontalHeaderItem(1)
        item.setText(_translate("FrmAluguel", "Nome"))
        item = self.gridCliente.horizontalHeaderItem(2)
        item.setText(_translate("FrmAluguel", "CPF"))
        item = self.gridCliente.horizontalHeaderItem(3)
        item.setText(_translate("FrmAluguel", "Endereço"))
        item = self.gridCliente.horizontalHeaderItem(4)
        item.setText(_translate("FrmAluguel", "Email"))
        item = self.gridCliente.horizontalHeaderItem(5)
        item.setText(_translate("FrmAluguel", "Telefone"))
        self.groupBox_3.setTitle(_translate("FrmAluguel", "Selecione o Veículo"))
        self.label_9.setText(_translate("FrmAluguel", "Tipo de Pesquisa"))
        self.btnPesqVeic_2.setText(_translate("FrmAluguel", "Pesquisar"))
        self.cbPesqVeic.setItemText(0, _translate("FrmAluguel", "Código"))
        self.cbPesqVeic.setItemText(1, _translate("FrmAluguel", "Marca"))
        self.cbPesqVeic.setItemText(2, _translate("FrmAluguel", "Modelo"))
        self.cbPesqVeic.setItemText(3, _translate("FrmAluguel", "Disponível"))
        self.cbPesqVeic.setItemText(4, _translate("FrmAluguel", "Alugado"))
        item = self.gridVeiculo.horizontalHeaderItem(0)
        item.setText(_translate("FrmAluguel", "Código"))
        item = self.gridVeiculo.horizontalHeaderItem(1)
        item.setText(_translate("FrmAluguel", "Modelo"))
        item = self.gridVeiculo.horizontalHeaderItem(2)
        item.setText(_translate("FrmAluguel", "Marca"))
        item = self.gridVeiculo.horizontalHeaderItem(3)
        item.setText(_translate("FrmAluguel", "Ano"))
        item = self.gridVeiculo.horizontalHeaderItem(4)
        item.setText(_translate("FrmAluguel", "Placa"))
        item = self.gridVeiculo.horizontalHeaderItem(5)
        item.setText(_translate("FrmAluguel", "Alugado"))
        item = self.gridVeiculo.horizontalHeaderItem(6)
        item.setText(_translate("FrmAluguel", "Batido"))
        item = self.gridVeiculo.horizontalHeaderItem(7)
        item.setText(_translate("FrmAluguel", "Km Atual"))
        item = self.gridVeiculo.horizontalHeaderItem(8)
        item.setText(_translate("FrmAluguel", "Valor Diária"))
        item = self.gridVeiculo.horizontalHeaderItem(9)
        item.setText(_translate("FrmAluguel", "Descrição"))
        item = self.gridVeiculo.horizontalHeaderItem(10)
        item.setText(_translate("FrmAluguel", "Tipo"))
        self.btnSalvar.setText(_translate("FrmAluguel", "Salvar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmAluguel = QtWidgets.QMainWindow()
    ui = Ui_FrmAluguel()
    ui.setupUi(FrmAluguel)
    FrmAluguel.show()
    sys.exit(app.exec_())
