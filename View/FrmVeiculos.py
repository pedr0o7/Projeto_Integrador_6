from PyQt5 import QtCore, QtGui, QtWidgets
from Controller.VeiculoCTR import VeiculoCTR

class Ui_frmVeiculos(object):


    # PREENCHER OS CAMPOS PARA ALTERAÇÃO
    def PreencherAlterar(self, modelo, marca, anoModelo, placa, alugado, batido, kmAtual, valorDiaria, descricao,
                         tipoVeiculo):
        self.edtModelo.setText(modelo)
        self.edtMarca.setText(marca)
        self.edtAno.setText(anoModelo)
        self.edtPlaca.setText(placa)
        self.edtKm.setText(kmAtual)
        self.edtDiaria.setText(valorDiaria)
        self.txtDescricao.setPlainText(descricao)
        self.edtTipo.setText(tipoVeiculo)

        if alugado == 'Sim':
            self.rbAlugado.setChecked(True)
            self.rbDisponivel.setChecked(False)
        elif alugado == 'Não':
            self.rbDisponivel.setChecked(True)
            self.rbAlugado.setChecked(False)

        if batido == 'Sim':
            self.rbBatido.setChecked(True)
            self.rbPerfeito.setChecked(False)
        elif batido == 'Não':
            self.rbPerfeito.setChecked(True)
            self.rbBatido.setChecked(False)

    # CLICK BTN_SALVAR
    def btnSalvar_Click(self, estado, codigoVeic):
        global alugado, batido
        modelo = self.edtModelo.text()
        marca = self.edtMarca.text()
        anoModelo = self.edtAno.text()
        placa = self.edtPlaca.text()

        if self.rbAlugado.isChecked():
            alugado = self.rbAlugado.text()
        elif self.rbDisponivel.isChecked():
            alugado = self.rbDisponivel.text()

        if self.rbBatido.isChecked():
            batido = self.rbBatido.text()
        elif self.rbPerfeito.isChecked():
            batido = self.rbPerfeito.text()

        kmAtual = self.edtKm.text()
        valorDiaria = self.edtDiaria.text()
        descricao = self.txtDescricao.toPlainText()
        tipoVeiculo = self.edtTipo.text()

        # VERIFICA O ESTADO INSERIR/ALTERAR PARA CHAMAR A FUNÇAO APROPRIADA
        if estado == 'inserir':
            veiculo = VeiculoCTR
            veiculo.CadastrarVeiculo(modelo, marca, anoModelo, placa, alugado, batido,
                         kmAtual, valorDiaria, descricao, tipoVeiculo)

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Veículo inserido com sucesso!")
            # msg.setInformativeText("This is additional information")
            msg.setWindowTitle("Inserir Veículo")
            # msg.setDetailedText("The details are as follows:")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        if estado == 'alterar':
            veiculo = VeiculoCTR
            veiculo.AtualizarVeiculo(self,codigoVeic, modelo, marca, anoModelo, placa, alugado,batido, kmAtual, valorDiaria, descricao, tipoVeiculo)

            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Veículo alterado com sucesso!")
            # msg.setInformativeText("This is additional information")
            msg.setWindowTitle("Alterar Veículo")
            # msg.setDetailedText("The details are as follows:")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

        self.edtModelo.setText('')
        self.edtMarca.setText('')
        self.edtAno.setText('')
        self.edtPlaca.setText('')
        self.edtKm.setText('')
        self.edtDiaria.setText('')
        self.txtDescricao.setText('')
        self.edtTipo.setText('')

    def setupUi(self, frmVeiculos, estado, codigoVeic):
        frmVeiculos.setObjectName("frmVeiculos")
        frmVeiculos.resize(652, 350)
        frmVeiculos.setMinimumSize(QtCore.QSize(0, 0))
        frmVeiculos.setMaximumSize(QtCore.QSize(16777215, 350))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Imagens/Cadastrar_veiculo_preto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmVeiculos.setWindowIcon(icon)
        frmVeiculos.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.508, y1:0.727, x2:0.505, y2:1, stop:0 rgba(255, 255, 153, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(frmVeiculos)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 310))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 310))
        self.groupBox.setStyleSheet("font: 87 10pt \"Arial\";")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.edtTipo = QtWidgets.QLineEdit(self.groupBox)
        self.edtTipo.setMinimumSize(QtCore.QSize(0, 30))
        self.edtTipo.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edtTipo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtTipo.setObjectName("edtTipo")
        self.gridLayout.addWidget(self.edtTipo, 3, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setMinimumSize(QtCore.QSize(0, 30))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 5, 1, 1)
        self.edtAno = QtWidgets.QLineEdit(self.groupBox)
        self.edtAno.setMinimumSize(QtCore.QSize(0, 30))
        self.edtAno.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edtAno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtAno.setObjectName("edtAno")
        self.gridLayout.addWidget(self.edtAno, 3, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rbAlugado = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbAlugado.setObjectName("rbAlugado")
        self.verticalLayout.addWidget(self.rbAlugado)
        self.rbDisponivel = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbDisponivel.setObjectName("rbDisponivel")
        self.verticalLayout.addWidget(self.rbDisponivel)
        self.gridLayout.addWidget(self.groupBox_3, 4, 0, 1, 1)
        self.edtModelo = QtWidgets.QLineEdit(self.groupBox)
        self.edtModelo.setMinimumSize(QtCore.QSize(0, 30))
        self.edtModelo.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edtModelo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtModelo.setObjectName("edtModelo")
        self.gridLayout.addWidget(self.edtModelo, 1, 0, 1, 3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbBatido = QtWidgets.QRadioButton(self.groupBox_4)
        self.rbBatido.setObjectName("rbBatido")
        self.verticalLayout_2.addWidget(self.rbBatido)
        self.rbPerfeito = QtWidgets.QRadioButton(self.groupBox_4)
        self.rbPerfeito.setObjectName("rbPerfeito")
        self.verticalLayout_2.addWidget(self.rbPerfeito)
        self.gridLayout.addWidget(self.groupBox_4, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setStyleSheet("gridline-color: qlineargradient(spread:pad, x1:0.467, y1:0.348, x2:0.465, y2:0.00586364, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edtDiaria = QtWidgets.QLineEdit(self.groupBox)
        self.edtDiaria.setMinimumSize(QtCore.QSize(0, 30))
        self.edtDiaria.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edtDiaria.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtDiaria.setObjectName("edtDiaria")
        self.gridLayout.addWidget(self.edtDiaria, 3, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.edtMarca = QtWidgets.QLineEdit(self.groupBox)
        self.edtMarca.setMinimumSize(QtCore.QSize(120, 30))
        self.edtMarca.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edtMarca.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtMarca.setObjectName("edtMarca")
        self.gridLayout.addWidget(self.edtMarca, 1, 3, 1, 1)
        self.lbEmail = QtWidgets.QLabel(self.groupBox)
        self.lbEmail.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lbEmail.setObjectName("lbEmail")
        self.gridLayout.addWidget(self.lbEmail, 0, 4, 1, 1)
        self.edtPlaca = QtWidgets.QLineEdit(self.groupBox)
        self.edtPlaca.setMinimumSize(QtCore.QSize(0, 30))
        self.edtPlaca.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edtPlaca.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtPlaca.setObjectName("edtPlaca")
        self.gridLayout.addWidget(self.edtPlaca, 1, 4, 1, 1)
        self.lbEndereco = QtWidgets.QLabel(self.groupBox)
        self.lbEndereco.setMaximumSize(QtCore.QSize(16777215, 40))
        self.lbEndereco.setObjectName("lbEndereco")
        self.gridLayout.addWidget(self.lbEndereco, 0, 5, 1, 1)
        self.edtKm = QtWidgets.QLineEdit(self.groupBox)
        self.edtKm.setMinimumSize(QtCore.QSize(0, 30))
        self.edtKm.setMaximumSize(QtCore.QSize(16777215, 30))
        self.edtKm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtKm.setObjectName("edtKm")
        self.gridLayout.addWidget(self.edtKm, 1, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 3, 1, 1)
        self.txtDescricao = QtWidgets.QTextEdit(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtDescricao.sizePolicy().hasHeightForWidth())
        self.txtDescricao.setSizePolicy(sizePolicy)
        self.txtDescricao.setMinimumSize(QtCore.QSize(120, 30))
        self.txtDescricao.setMaximumSize(QtCore.QSize(16777215, 30))
        self.txtDescricao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDescricao.setObjectName("txtDescricao")
        self.gridLayout.addWidget(self.txtDescricao, 3, 3, 1, 1)
        self.btnSalvar = QtWidgets.QPushButton(self.groupBox)
        self.btnSalvar.setMinimumSize(QtCore.QSize(120, 50))
        self.btnSalvar.setMaximumSize(QtCore.QSize(120, 50))
        self.btnSalvar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Imagens/Salvar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setIconSize(QtCore.QSize(35, 35))
        self.btnSalvar.setObjectName("btnSalvar")
        self.gridLayout.addWidget(self.btnSalvar, 4, 5, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        frmVeiculos.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(frmVeiculos)
        self.statusbar.setObjectName("statusbar")
        frmVeiculos.setStatusBar(self.statusbar)

        self.retranslateUi(frmVeiculos)
        QtCore.QMetaObject.connectSlotsByName(frmVeiculos)

        self.btnSalvar.clicked.connect(lambda: self.btnSalvar_Click(estado, codigoVeic))

    def retranslateUi(self, frmVeiculos):
        _translate = QtCore.QCoreApplication.translate
        frmVeiculos.setWindowTitle(_translate("frmVeiculos", "Cadastro de Veículos"))
        self.label_3.setText(_translate("frmVeiculos", "Ano"))
        self.label_6.setText(_translate("frmVeiculos", "Tipo de Veículo"))
        self.groupBox_3.setTitle(_translate("frmVeiculos", "Alugado"))
        self.rbAlugado.setText(_translate("frmVeiculos", "Sim"))
        self.rbDisponivel.setText(_translate("frmVeiculos", "Não"))
        self.groupBox_4.setTitle(_translate("frmVeiculos", "Batido"))
        self.rbBatido.setText(_translate("frmVeiculos", "Sim"))
        self.rbPerfeito.setText(_translate("frmVeiculos", "Não"))
        self.label_4.setText(_translate("frmVeiculos", "Valor da Diária"))
        self.label.setText(_translate("frmVeiculos", "Modelo"))
        self.label_2.setText(_translate("frmVeiculos", "Marca"))
        self.lbEmail.setText(_translate("frmVeiculos", "Placa"))
        self.lbEndereco.setText(_translate("frmVeiculos", "KM Atual"))
        self.label_5.setText(_translate("frmVeiculos", "Descrição"))
        self.btnSalvar.setText(_translate("frmVeiculos", "Salvar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmVeiculos = QtWidgets.QMainWindow()
    ui = Ui_frmVeiculos()
    ui.setupUi(frmVeiculos)
    frmVeiculos.show()
    sys.exit(app.exec_())
