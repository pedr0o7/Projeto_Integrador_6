from PyQt5 import QtCore, QtGui, QtWidgets
from Controller import ClienteCTR
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from validar import validacpfcnpj


class Ui_FrmCliente(object):

    #PREENCHER OS CAMPOS PARA ALTERAÇÃO
    def PreencherAlterar(self, nome, cpf, endereco, email, telefone):
        self.edtNome.setText(nome)
        self.edtCPF.setText(cpf)
        self.edtEndereco.setText(endereco)
        self.edtEmail.setText(email)
        self.edtTelefone.setText(telefone)

    def btnSalvar_Click(self, estado, codigoCli):

        nome = self.edtNome.text()
        cpf = self.edtCPF.text()
        endereco = self.edtEndereco.text()
        email = self.edtEmail.text()
        print(email)
        telefone = self.edtTelefone.text()

        Email = email.count("@")
        cpf_cnpj = validacpfcnpj.ValidaCpfCnpj(cpf)

        if cpf_cnpj.valida():
            if Email == 1:
                if len(telefone) >=11 and len(telefone)<16 :
                    if estado == 'inserir':
                        cliente = ClienteCTR
                        cliente.ClienteCTR.CadastrarCliente(self, nome, cpf, endereco, email, telefone)

                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Information)
                        msg.setText("Cliente inserido com sucesso!")
                        msg.setWindowTitle("Inserir Cliente")
                        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                        msg.exec_()

                    if estado == 'alterar':
                        cliente = ClienteCTR
                        cliente.ClienteCTR.AtualizarCliente(self, codigoCli, nome, cpf, endereco, email, telefone)
                        msg = QtWidgets.QMessageBox()
                        msg.setIcon(QtWidgets.QMessageBox.Information)
                        msg.setText("Cliente alterado com sucesso!")
                        msg.setWindowTitle("Alterar Cliente")
                        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                        msg.exec_()
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setIcon(QtWidgets.QMessageBox.Information)
                    msg.setText("Telefone inválido.")
                    msg.setWindowTitle("Inserir Cliente")
                    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    msg.exec_()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Email inválido.")
                msg.setWindowTitle("Inserir Cliente")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("CPF inválido.")
            msg.setWindowTitle("Inserir Cliente")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()

        self.edtNome.setText('')
        self.edtCPF.setText('')
        self.edtEndereco.setText('')
        self.edtEmail.setText('')
        self.edtTelefone.setText('')

    def setupUi(self, FrmCliente, estado, codigoCli):
        FrmCliente.setObjectName("FrmCliente")
        FrmCliente.resize(1000, 300)
        FrmCliente.setMinimumSize(QtCore.QSize(0, 0))
        FrmCliente.setMaximumSize(QtCore.QSize(1000, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Imagens/Cadastrar_cliente_preto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmCliente.setWindowIcon(icon)
        FrmCliente.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.508, y1:0.727, x2:0.505, y2:1, stop:0 rgba(255, 255, 153, 255), stop:1 rgba(255, 255, 255, 255))")
        self.centralwidget = QtWidgets.QWidget(FrmCliente)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("font: 87 12pt \"Arial\";")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.edtNome = QtWidgets.QLineEdit(self.groupBox)
        self.edtNome.setMinimumSize(QtCore.QSize(0, 30))
        self.edtNome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtNome.setObjectName("edtNome")
        self.gridLayout.addWidget(self.edtNome, 1, 0, 1, 1)
        self.edtCPF = QtWidgets.QLineEdit(self.groupBox)
        self.edtCPF.setMinimumSize(QtCore.QSize(0, 30))
        self.edtCPF.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtCPF.setObjectName("edtCPF")
        self.gridLayout.addWidget(self.edtCPF, 1, 1, 1, 1)
        self.lbEmail = QtWidgets.QLabel(self.groupBox)
        self.lbEmail.setObjectName("lbEmail")
        self.gridLayout.addWidget(self.lbEmail, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.edtEmail = QtWidgets.QLineEdit(self.groupBox)
        self.edtEmail.setMinimumSize(QtCore.QSize(0, 30))
        self.edtEmail.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtEmail.setObjectName("edtEmail")
        self.gridLayout.addWidget(self.edtEmail, 3, 0, 1, 1)
        self.edtTelefone = QtWidgets.QLineEdit(self.groupBox)
        self.edtTelefone.setMinimumSize(QtCore.QSize(0, 30))
        self.edtTelefone.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtTelefone.setObjectName("edtTelefone")
        self.gridLayout.addWidget(self.edtTelefone, 3, 1, 1, 1)
        self.lbEndereco = QtWidgets.QLabel(self.groupBox)
        self.lbEndereco.setObjectName("lbEndereco")
        self.gridLayout.addWidget(self.lbEndereco, 4, 0, 1, 1)
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
        self.gridLayout.addWidget(self.btnSalvar, 6, 1, 1, 1, QtCore.Qt.AlignRight)
        self.edtEndereco = QtWidgets.QLineEdit(self.groupBox)
        self.edtEndereco.setMinimumSize(QtCore.QSize(0, 30))
        self.edtEndereco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtEndereco.setObjectName("edtEndereco")
        self.gridLayout.addWidget(self.edtEndereco, 5, 0, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        FrmCliente.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(FrmCliente)
        self.statusbar.setObjectName("statusbar")
        FrmCliente.setStatusBar(self.statusbar)

        self.btnSalvar.clicked.connect(lambda: self.btnSalvar_Click(estado, codigoCli))


        self.retranslateUi(FrmCliente)
        QtCore.QMetaObject.connectSlotsByName(FrmCliente)

    def retranslateUi(self, FrmCliente):
        _translate = QtCore.QCoreApplication.translate
        FrmCliente.setWindowTitle(_translate("FrmCliente", "Cadastro de Cliente"))
        self.label.setText(_translate("FrmCliente", "Nome"))
        self.label_2.setText(_translate("FrmCliente", "CPF"))
        self.lbEmail.setText(_translate("FrmCliente", "EMail"))
        self.label_5.setText(_translate("FrmCliente", "Telefone"))
        self.lbEndereco.setText(_translate("FrmCliente", "Endereço"))
        self.btnSalvar.setText(_translate("FrmCliente", "Salvar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmCliente = QtWidgets.QMainWindow()
    ui = Ui_FrmCliente()
    ui.setupUi(FrmCliente)
    FrmCliente.show()
    sys.exit(app.exec_())
