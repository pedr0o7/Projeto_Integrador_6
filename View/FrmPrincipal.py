from PyQt5 import QtCore, QtGui, QtWidgets

from View.FrmAluguel import Ui_FrmAluguel
from View.FrmCliente import Ui_frmCliente
from View.FrmPesqAluguel import Ui_FrmPesqAluguel
from View.FrmVeiculos import Ui_frmVeiculos
from View.frmPesqCliente import Ui_frmPesqCliente
from View.frmPesqVeiculos import Ui_frmPesqVeiculos


class Ui_FrmPrincipal(object):
    def setupUi(self, FrmPrincipal):
        FrmPrincipal.setObjectName("FrmPrincipal")
        FrmPrincipal.setWindowModality(QtCore.Qt.NonModal)
        FrmPrincipal.resize(1051, 515)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Python-20210805T211248Z-001\Projeto_Python\Imagens/unknown.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmPrincipal.setWindowIcon(icon)
        FrmPrincipal.setAutoFillBackground(False)
        FrmPrincipal.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.508, y1:0.727, x2:0.505, y2:1, stop:0 rgba(255, 255, 153, 255), stop:1 rgba(255, 255, 255, 255))")
        FrmPrincipal.setIconSize(QtCore.QSize(40, 40))
        self.centralwidget = QtWidgets.QWidget(FrmPrincipal)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 1031, 101))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.btnAlugar = QtWidgets.QPushButton(self.groupBox_2)
        self.btnAlugar.setGeometry(QtCore.QRect(10, 10, 151, 81))
        self.btnAlugar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnAlugar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnAlugar.setAutoFillBackground(False)
        self.btnAlugar.setStyleSheet("QPushButton{\n"
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
        icon1.addPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Python-20210805T211248Z-001\Projeto_Python\Imagens/Aluguel_veiculo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlugar.setIcon(icon1)
        self.btnAlugar.setIconSize(QtCore.QSize(40, 40))
        self.btnAlugar.setObjectName("btnAlugar")

        self.btnCliente = QtWidgets.QPushButton(self.groupBox_2)
        self.btnCliente.setGeometry(QtCore.QRect(170, 10, 161, 81))
        self.btnCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCliente.setStyleSheet("QPushButton{\n"
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
        icon2.addPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Python-20210805T211248Z-001\Projeto_Python\Imagens/Cadastrar_cliente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCliente.setIcon(icon2)
        self.btnCliente.setIconSize(QtCore.QSize(30, 30))
        self.btnCliente.setObjectName("btnCliente")
        self.btnVeiculo = QtWidgets.QPushButton(self.groupBox_2)
        self.btnVeiculo.setGeometry(QtCore.QRect(340, 10, 171, 81))
        self.btnVeiculo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVeiculo.setStyleSheet("QPushButton{\n"
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
        icon3.addPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Python-20210805T211248Z-001\Projeto_Python\Imagens/Cadastrar_veiculo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVeiculo.setIcon(icon3)
        self.btnVeiculo.setIconSize(QtCore.QSize(40, 40))
        self.btnVeiculo.setObjectName("btnVeiculo")
        self.btnListCliente = QtWidgets.QPushButton(self.groupBox_2)
        self.btnListCliente.setGeometry(QtCore.QRect(520, 10, 171, 81))
        self.btnListCliente.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnListCliente.setStyleSheet("QPushButton{\n"
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Python-20210805T211248Z-001\Projeto_Python\Imagens/Lista_cliente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListCliente.setIcon(icon4)
        self.btnListCliente.setIconSize(QtCore.QSize(30, 30))
        self.btnListCliente.setObjectName("btnListCliente")
        self.btnListVeiculo = QtWidgets.QPushButton(self.groupBox_2)
        self.btnListVeiculo.setGeometry(QtCore.QRect(700, 10, 161, 81))
        self.btnListVeiculo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnListVeiculo.setStyleSheet("QPushButton{\n"
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Python-20210805T211248Z-001\Projeto_Python\Imagens/Lista_Veiculos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListVeiculo.setIcon(icon5)
        self.btnListVeiculo.setIconSize(QtCore.QSize(30, 30))
        self.btnListVeiculo.setObjectName("btnListVeiculo")
        self.btnListAluguel = QtWidgets.QPushButton(self.groupBox_2)
        self.btnListAluguel.setGeometry(QtCore.QRect(870, 10, 151, 81))
        self.btnListAluguel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnListAluguel.setStyleSheet("QPushButton{\n"
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Python-20210805T211248Z-001\Projeto_Python\Imagens/Lista_aluguel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListAluguel.setIcon(icon6)
        self.btnListAluguel.setIconSize(QtCore.QSize(30, 30))
        self.btnListAluguel.setObjectName("btnListAluguel")
        self.lbImg = QtWidgets.QLabel(self.centralwidget)
        self.lbImg.setGeometry(QtCore.QRect(110, 120, 801, 351))
        self.lbImg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.lbImg.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.lbImg.setText("")
        self.lbImg.setPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Python-20210805T211248Z-001\Projeto_Python\Imagens/Logo_Meca.jpeg"))#Logo_Meca #Logo_uno_escada
        self.lbImg.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.lbImg.setObjectName("lbImg")
        FrmPrincipal.setCentralWidget(self.centralwidget)
        self.actionCliente = QtWidgets.QAction(FrmPrincipal)
        self.actionCliente.setObjectName("actionCliente")
        self.actionVe_culo = QtWidgets.QAction(FrmPrincipal)
        self.actionVe_culo.setObjectName("actionVe_culo")
        self.actionAlugar = QtWidgets.QAction(FrmPrincipal)
        self.actionAlugar.setObjectName("actionAlugar")
        self.actionCliente_2 = QtWidgets.QAction(FrmPrincipal)
        self.actionCliente_2.setObjectName("actionCliente_2")
        self.actionVe_culos = QtWidgets.QAction(FrmPrincipal)
        self.actionVe_culos.setObjectName("actionVe_culos")
        self.actionAlugueis = QtWidgets.QAction(FrmPrincipal)
        self.actionAlugueis.setObjectName("actionAlugueis")
        self.actionSair = QtWidgets.QAction(FrmPrincipal)
        self.actionSair.setObjectName("actionSair")

        self.retranslateUi(FrmPrincipal)
        QtCore.QMetaObject.connectSlotsByName(FrmPrincipal)

        self.btnAlugar.clicked.connect(self.FrmAluguel_Click)
        self.btnCliente.clicked.connect(self.FrmCliente_Click)
        self.btnVeiculo.clicked.connect(self.FrmVeiculo_Click)
        self.btnListCliente.clicked.connect(self.btnListarCliente_Click)
        self.btnListVeiculo.clicked.connect(self.btnListarVeiculo_Click)
        self.btnListAluguel.clicked.connect(self.btnListarAluguel_Click)
    def retranslateUi(self, FrmPrincipal):
        _translate = QtCore.QCoreApplication.translate
        FrmPrincipal.setWindowTitle(_translate("FrmPrincipal", "Locadora de Veículos"))
        self.btnAlugar.setText(_translate("FrmPrincipal", "Alugar Veículo"))
        self.btnCliente.setText(_translate("FrmPrincipal", "Cadastrar Cliente"))
        self.btnVeiculo.setText(_translate("FrmPrincipal", "Cadastrar Veículo"))
        self.btnListCliente.setText(_translate("FrmPrincipal", "Listar Clientes"))
        self.btnListVeiculo.setText(_translate("FrmPrincipal", "Listar Veículos"))
        self.btnListAluguel.setText(_translate("FrmPrincipal", "Listar Alugueis"))
        self.actionCliente.setText(_translate("FrmPrincipal", "Cliente"))
        self.actionVe_culo.setText(_translate("FrmPrincipal", "Veículo"))
        self.actionAlugar.setText(_translate("FrmPrincipal", "Alugar Veículo"))
        self.actionCliente_2.setText(_translate("FrmPrincipal", "Clientes"))
        self.actionVe_culos.setText(_translate("FrmPrincipal", "Veículos"))
        self.actionAlugueis.setText(_translate("FrmPrincipal", "Alugueis"))
        self.actionSair.setText(_translate("FrmPrincipal", "Sair"))

    # BTN ALUGUEL.CLICK
    def FrmAluguel_Click(self):
        self.frmAluguel = QtWidgets.QMainWindow()
        self.ui = Ui_FrmAluguel()
        self.ui.setupUi(self.frmAluguel)
        self.frmAluguel.show()

    # BTNCLIENTE.CLICK
    def FrmCliente_Click(self):
        self.frmCliente = QtWidgets.QMainWindow()
        self.ui = Ui_frmCliente()
        self.ui.setupUi(self.frmCliente, 'inserir', None)
        self.frmCliente.show()

    # BTNVEICULO.CLICK
    def FrmVeiculo_Click(self):
        self.frmVeiculo = QtWidgets.QMainWindow()
        self.ui = Ui_frmVeiculos()
        self.ui.setupUi(self.frmVeiculo, 'inserir', None)
        self.frmVeiculo.show()

    # BTN LISTAR TODOS CLIENTES CLICK
    def btnListarCliente_Click(self):
        self.frmPesqCliente = QtWidgets.QMainWindow()
        self.ui = Ui_frmPesqCliente()
        self.ui.setupUi(self.frmPesqCliente)
        self.frmPesqCliente.show()

    # BTN LISTAR TODOS VEICULOS CLICK
    def btnListarVeiculo_Click(self):
        self.frmPesqVeiculo = QtWidgets.QMainWindow()
        self.ui = Ui_frmPesqVeiculos()
        self.ui.setupUi(self.frmPesqVeiculo)
        self.frmPesqVeiculo.show()

    # BTN LISTAR TODOS ALUGUEIS CLICK
    def btnListarAluguel_Click(self):
        self.frmPesqAluguel = QtWidgets.QMainWindow()
        self.ui = Ui_FrmPesqAluguel()
        self.ui.setupUi(self.frmPesqAluguel)
        self.frmPesqAluguel.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FrmPrincipal = QtWidgets.QMainWindow()
    ui = Ui_FrmPrincipal()
    ui.setupUi(FrmPrincipal)
    FrmPrincipal.show()
    sys.exit(app.exec_())
