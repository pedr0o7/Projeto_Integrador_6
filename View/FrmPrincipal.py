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
        FrmPrincipal.setWindowModality(QtCore.Qt.WindowModal)
        FrmPrincipal.resize(1137, 683)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./Imagens/FrmIcon_Car.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FrmPrincipal.setWindowIcon(icon)
        FrmPrincipal.setIconSize(QtCore.QSize(40, 40))

        FrmPrincipal.setAutoFillBackground(False)
        FrmPrincipal.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0.508, y1:0.727, x2:0.505, y2:1, stop:0 rgba(255, 255, 153, 255), stop:1 rgba(255, 255, 255, 255))")

        FrmPrincipal.setAnimated(False)
        FrmPrincipal.setDocumentMode(False)
        FrmPrincipal.setDockNestingEnabled(False)
        FrmPrincipal.setUnifiedTitleAndToolBarOnMac(True)

        self.centralwidget = QtWidgets.QWidget(FrmPrincipal)
        self.centralwidget.setMinimumSize(QtCore.QSize(1137, 683))
        self.centralwidget.setObjectName("centralwidget")


        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.btnCliente = QtWidgets.QPushButton(self.centralwidget)
        self.btnCliente.setMinimumSize(QtCore.QSize(0, 80))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./Imagens/Cadastrar_cliente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCliente.setIcon(icon1)
        self.btnCliente.setIconSize(QtCore.QSize(35, 35))
        self.btnCliente.setObjectName("btnCliente")
        self.horizontalLayout_3.addWidget(self.btnCliente)
        self.btnListCliente = QtWidgets.QPushButton(self.centralwidget)
        self.btnListCliente.setMinimumSize(QtCore.QSize(0, 80))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./Imagens/Lista_cliente.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListCliente.setIcon(icon2)
        self.btnListCliente.setIconSize(QtCore.QSize(40, 40))
        self.btnListCliente.setObjectName("btnListCliente")
        self.horizontalLayout_3.addWidget(self.btnListCliente)
        self.btnVeiculo = QtWidgets.QPushButton(self.centralwidget)
        self.btnVeiculo.setMinimumSize(QtCore.QSize(0, 80))
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
        icon3.addPixmap(QtGui.QPixmap("./Imagens/Cadastrar_veiculo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnVeiculo.setIcon(icon3)
        self.btnVeiculo.setIconSize(QtCore.QSize(40, 40))
        self.btnVeiculo.setObjectName("btnVeiculo")
        self.horizontalLayout_3.addWidget(self.btnVeiculo)
        self.btnAlugar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAlugar.setMinimumSize(QtCore.QSize(0, 80))
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
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./Imagens/Aluguel_veiculo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAlugar.setIcon(icon4)
        self.btnAlugar.setIconSize(QtCore.QSize(70, 60))
        self.btnAlugar.setObjectName("btnAlugar")
        self.horizontalLayout_3.addWidget(self.btnAlugar)
        self.btnListAluguel = QtWidgets.QPushButton(self.centralwidget)
        self.btnListAluguel.setMinimumSize(QtCore.QSize(0, 80))
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
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./Imagens/Lista_aluguel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListAluguel.setIcon(icon5)
        self.btnListAluguel.setIconSize(QtCore.QSize(40, 40))
        self.btnListAluguel.setObjectName("btnListAluguel")
        self.horizontalLayout_3.addWidget(self.btnListAluguel)
        self.btnListVeiculo = QtWidgets.QPushButton(self.centralwidget)
        self.btnListVeiculo.setMinimumSize(QtCore.QSize(0, 80))
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./Imagens/Lista_Veiculos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnListVeiculo.setIcon(icon6)
        self.btnListVeiculo.setIconSize(QtCore.QSize(40, 40))
        self.btnListVeiculo.setObjectName("btnListVeiculo")
        self.horizontalLayout_3.addWidget(self.btnListVeiculo)
        self.horizontalLayout.addLayout(self.horizontalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("./Imagens/Logo_uno_escada.jpeg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
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
        self.btnCliente.setText(_translate("FrmPrincipal", "Cadastrar Cliente"))
        self.btnListCliente.setText(_translate("FrmPrincipal", "Listar Clientes"))
        self.btnVeiculo.setText(_translate("FrmPrincipal", "Cadastrar Veículo"))
        self.btnAlugar.setText(_translate("FrmPrincipal", "Alugar Veículo"))
        self.btnListAluguel.setText(_translate("FrmPrincipal", "Listar Alugueis"))
        self.btnListVeiculo.setText(_translate("FrmPrincipal", "Listar Veículos"))
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
