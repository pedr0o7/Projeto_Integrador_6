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
        frmVeiculos.resize(543, 318)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Imagens/Cadastrar_veiculo_preto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmVeiculos.setWindowIcon(icon)
        frmVeiculos.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.508, y1:0.727, x2:0.505, y2:1, stop:0 rgba(255, 255, 153, 255), stop:1 rgba(255, 255, 255, 255))")
        self.groupBox_2 = QtWidgets.QGroupBox(frmVeiculos)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 230, 521, 81))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnSalvar = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSalvar.setGeometry(QtCore.QRect(400, 10, 101, 61))
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
        icon1.addPixmap(QtGui.QPixmap("./Imagens/Salvar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off) ####VER OUTRO MODO!!
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setIconSize(QtCore.QSize(35, 35))
        self.btnSalvar.setObjectName("btnSalvar")
        self.groupBox = QtWidgets.QGroupBox(frmVeiculos)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 521, 211))
        self.groupBox.setStyleSheet("font: 87 10pt \"Arial\";")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label.setStyleSheet("gridline-color: qlineargradient(spread:pad, x1:0.467, y1:0.348, x2:0.465, y2:0.00586364, stop:0 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 51, 16))
        self.label_2.setObjectName("label_2")
        self.lbEndereco = QtWidgets.QLabel(self.groupBox)
        self.lbEndereco.setGeometry(QtCore.QRect(220, 60, 71, 16))
        self.lbEndereco.setObjectName("lbEndereco")
        self.lbEmail = QtWidgets.QLabel(self.groupBox)
        self.lbEmail.setGeometry(QtCore.QRect(420, 10, 46, 13))
        self.lbEmail.setObjectName("lbEmail")
        self.edtModelo = QtWidgets.QLineEdit(self.groupBox)
        self.edtModelo.setGeometry(QtCore.QRect(10, 30, 201, 20))
        self.edtModelo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtModelo.setObjectName("edtModelo")
        self.edtMarca = QtWidgets.QLineEdit(self.groupBox)
        self.edtMarca.setGeometry(QtCore.QRect(220, 30, 191, 20))
        self.edtMarca.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtMarca.setObjectName("edtMarca")
        self.edtAno = QtWidgets.QLineEdit(self.groupBox)
        self.edtAno.setGeometry(QtCore.QRect(420, 80, 91, 20))
        self.edtAno.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtAno.setObjectName("edtAno")
        self.edtKm = QtWidgets.QLineEdit(self.groupBox)
        self.edtKm.setGeometry(QtCore.QRect(220, 80, 91, 20))
        self.edtKm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtKm.setObjectName("edtKm")
        self.edtDiaria = QtWidgets.QLineEdit(self.groupBox)
        self.edtDiaria.setGeometry(QtCore.QRect(320, 80, 91, 20))
        self.edtDiaria.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtDiaria.setObjectName("edtDiaria")
        self.edtTipo = QtWidgets.QLineEdit(self.groupBox)
        self.edtTipo.setGeometry(QtCore.QRect(10, 80, 201, 20))
        self.edtTipo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtTipo.setObjectName("edtTipo")
        self.edtPlaca = QtWidgets.QLineEdit(self.groupBox)
        self.edtPlaca.setGeometry(QtCore.QRect(420, 30, 91, 20))
        self.edtPlaca.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtPlaca.setObjectName("edtPlaca")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(420, 60, 46, 13))
        self.label_3.setObjectName("label_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 120, 81, 80))
        self.groupBox_3.setObjectName("groupBox_3")
        self.rbAlugado = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbAlugado.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.rbAlugado.setObjectName("rbAlugado")
        self.rbDisponivel = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbDisponivel.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.rbDisponivel.setObjectName("rbDisponivel")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(100, 120, 81, 80))
        self.groupBox_4.setObjectName("groupBox_4")
        self.rbBatido = QtWidgets.QRadioButton(self.groupBox_4)
        self.rbBatido.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.rbBatido.setObjectName("rbBatido")
        self.rbPerfeito = QtWidgets.QRadioButton(self.groupBox_4)
        self.rbPerfeito.setGeometry(QtCore.QRect(10, 50, 82, 17))
        self.rbPerfeito.setObjectName("rbPerfeito")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(320, 60, 91, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(200, 120, 91, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.label_6.setObjectName("label_6")
        self.txtDescricao = QtWidgets.QTextEdit(self.groupBox)
        self.txtDescricao.setGeometry(QtCore.QRect(200, 140, 311, 61))
        self.txtDescricao.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtDescricao.setObjectName("txtDescricao")

        self.btnSalvar.clicked.connect(lambda: self.btnSalvar_Click(estado, codigoVeic))

        self.retranslateUi(frmVeiculos)
        QtCore.QMetaObject.connectSlotsByName(frmVeiculos)

    def retranslateUi(self, frmVeiculos):
        _translate = QtCore.QCoreApplication.translate
        frmVeiculos.setWindowTitle(_translate("frmVeiculos", "Cadastro de Veículos"))
        self.btnSalvar.setText(_translate("frmVeiculos", "Salvar"))
        self.label.setText(_translate("frmVeiculos", "Modelo"))
        self.label_2.setText(_translate("frmVeiculos", "Marca"))
        self.lbEndereco.setText(_translate("frmVeiculos", "KM Atual"))
        self.lbEmail.setText(_translate("frmVeiculos", "Placa"))
        self.label_3.setText(_translate("frmVeiculos", "Ano"))
        self.groupBox_3.setTitle(_translate("frmVeiculos", "Alugado"))
        self.rbAlugado.setText(_translate("frmVeiculos", "Sim"))
        self.rbDisponivel.setText(_translate("frmVeiculos", "Não"))
        self.groupBox_4.setTitle(_translate("frmVeiculos", "Batido"))
        self.rbBatido.setText(_translate("frmVeiculos", "Sim"))
        self.rbPerfeito.setText(_translate("frmVeiculos", "Não"))
        self.label_4.setText(_translate("frmVeiculos", "Valor da Diária"))
        self.label_5.setText(_translate("frmVeiculos", "Descrição"))
        self.label_6.setText(_translate("frmVeiculos", "Tipo de Veículo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmVeiculos = QtWidgets.QWidget()
    ui = Ui_frmVeiculos()
    ui.setupUi(frmVeiculos,'',None)
    frmVeiculos.show()
    sys.exit(app.exec_())
