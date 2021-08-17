from PyQt5 import QtCore, QtGui, QtWidgets
from Controller import ClienteCTR
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from validar import validacpfcnpj

class Ui_frmCliente(object):

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

    def setupUi(self, frmCliente, estado, codigoCli):

        frmCliente.setObjectName("frmCliente")
        frmCliente.resize(532, 269)
        #Icone da pag
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Integrador_6\Imagens//Cadastrar_cliente_preto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmCliente.setWindowIcon(icon)
        #Background
        frmCliente.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.508, y1:0.727, x2:0.505, y2:1, stop:0 rgba(255, 255, 153, 255), stop:1 rgba(255, 255, 255, 255))")
        self.groupBox = QtWidgets.QGroupBox(frmCliente)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 511, 161))
        self.groupBox.setStyleSheet("font: 87 12pt \"Arial\";")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(340, 10, 91, 16))
        self.label_2.setObjectName("label_2")
        self.lbEndereco = QtWidgets.QLabel(self.groupBox)
        self.lbEndereco.setGeometry(QtCore.QRect(10, 110, 141, 16))
        self.lbEndereco.setObjectName("lbEndereco")
        self.lbEmail = QtWidgets.QLabel(self.groupBox)
        self.lbEmail.setGeometry(QtCore.QRect(10, 60, 61, 16))
        self.lbEmail.setObjectName("lbEmail")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(340, 60, 131, 16))
        self.label_5.setObjectName("label_5")
        self.edtNome = QtWidgets.QLineEdit(self.groupBox)
        self.edtNome.setGeometry(QtCore.QRect(10, 30, 321, 20))
        self.edtNome.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtNome.setObjectName("edtNome")
        self.edtCPF = QtWidgets.QLineEdit(self.groupBox)
        self.edtCPF.setGeometry(QtCore.QRect(340, 30, 161, 20))
        self.edtCPF.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtCPF.setObjectName("edtCPF")
        self.edtEmail = QtWidgets.QLineEdit(self.groupBox)
        self.edtEmail.setGeometry(QtCore.QRect(10, 80, 321, 20))
        self.edtEmail.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtEmail.setObjectName("edtEmail")
        self.edtTelefone = QtWidgets.QLineEdit(self.groupBox)
        self.edtTelefone.setGeometry(QtCore.QRect(340, 80, 161, 20))
        self.edtTelefone.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtTelefone.setObjectName("edtTelefone")
        self.edtEndereco = QtWidgets.QLineEdit(self.groupBox)
        self.edtEndereco.setGeometry(QtCore.QRect(10, 130, 491, 20))
        self.edtEndereco.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.edtEndereco.setObjectName("edtEndereco")
        self.groupBox_2 = QtWidgets.QGroupBox(frmCliente)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 180, 511, 81))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnSalvar = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSalvar.setGeometry(QtCore.QRect(380, 10, 101, 61))
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
        icon1.addPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Integrador_6\Imagens/Salvar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSalvar.setIcon(icon1)
        self.btnSalvar.setIconSize(QtCore.QSize(35, 35))
        self.btnSalvar.setObjectName("btnSalvar")

        self.btnSalvar.clicked.connect(lambda: self.btnSalvar_Click(estado, codigoCli))

        self.retranslateUi(frmCliente)
        QtCore.QMetaObject.connectSlotsByName(frmCliente)

    def retranslateUi(self, frmCliente):
        _translate = QtCore.QCoreApplication.translate
        frmCliente.setWindowTitle(_translate("frmCliente", "Cadastro de Cliente"))
        self.label.setText(_translate("frmCliente", "Nome"))
        self.label_2.setText(_translate("frmCliente", "CPF"))
        self.lbEndereco.setText(_translate("frmCliente", "Endereço"))
        self.lbEmail.setText(_translate("frmCliente", "EMail"))
        self.label_5.setText(_translate("frmCliente", "Telefone"))
        self.btnSalvar.setText(_translate("frmCliente", "Salvar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmCliente = QtWidgets.QWidget()
    ui = Ui_frmCliente()
    ui.setupUi(frmCliente,'',None)
    frmCliente.show()
    sys.exit(app.exec_())
