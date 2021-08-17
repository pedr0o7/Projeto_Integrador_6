from PyQt5 import QtCore, QtGui, QtWidgets

from Controller import VeiculoCTR
from View.FrmVeiculos import Ui_frmVeiculos


class Ui_frmPesqVeiculos(object):

    def AlterarVeiculo_Click(self):
        linha = self.gridVeiculos.currentItem().row()
        codigoVeic = self.gridVeiculos.item(linha, 0).text()
        modelo = self.gridVeiculos.item(linha, 1).text()
        marca = self.gridVeiculos.item(linha, 2).text()
        anoModelo = self.gridVeiculos.item(linha, 3).text()
        placa = self.gridVeiculos.item(linha, 4).text()
        alugado = self.gridVeiculos.item(linha, 5).text()
        batido = self.gridVeiculos.item(linha, 6).text()
        kmAtual = self.gridVeiculos.item(linha, 7).text()
        valorDiaria = self.gridVeiculos.item(linha, 8).text()
        descricao = self.gridVeiculos.item(linha, 9).text()
        tipoVeiculo = self.gridVeiculos.item(linha, 10).text()

        self.frmVeiculos = QtWidgets.QMainWindow()
        self.ui = Ui_frmVeiculos()
        self.ui.setupUi(self.frmVeiculos, 'alterar', codigoVeic)
        self.ui.PreencherAlterar(modelo, marca, anoModelo, placa, alugado, batido, kmAtual, valorDiaria, descricao,
                                 tipoVeiculo)
        self.frmVeiculos.show()

    def ExcluirVeiculo_Click(self):

        linha = self.gridVeiculos.currentItem().row()
        codigoVeic = self.gridVeiculos.item(linha, 0).text()

        self.gridVeiculos.removeRow(linha)
        veiculo = VeiculoCTR
        veiculo.VeiculoCTR.ExcluirVeiculo(self,codigoVeic)

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Veículo Excluído!")
        # msg.setInformativeText("This is additional information")
        msg.setWindowTitle("Excluir Veículo")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()

    def PesquisarVeiculo(self, valor, tipo):
        if (valor == '') and (tipo != 'Disponível') and (tipo != 'Alugado'):
            self.PesquisarTodosVeiculos()
        else:
            veiculo = VeiculoCTR
            query = veiculo.VeiculoCTR.PesquisarVeiculo(self, valor, tipo)

            while (self.gridVeiculos.rowCount() > 0):
                self.gridVeiculos.removeRow(0)

            row = 0
            while query.next():
                self.gridVeiculos.insertRow(row)
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

                self.gridVeiculos.setItem(row, 0, codigoVeic)
                self.gridVeiculos.setItem(row, 1, modelo)
                self.gridVeiculos.setItem(row, 2, marca)
                self.gridVeiculos.setItem(row, 3, anoModelo)
                self.gridVeiculos.setItem(row, 4, placa)
                self.gridVeiculos.setItem(row, 5, alugado)
                self.gridVeiculos.setItem(row, 6, batido)
                self.gridVeiculos.setItem(row, 7, kmAtual)
                self.gridVeiculos.setItem(row, 8, valorDiaria)
                self.gridVeiculos.setItem(row, 9, descricao)
                self.gridVeiculos.setItem(row, 10, tipoVeiculo)

                row = row + 1

        self.edtPesquisa_2.setText('')

    def PesquisarTodosVeiculos(self):
        veiculo = VeiculoCTR
        query = veiculo.VeiculoCTR.PesquisarTodosVeiculos()

        while (self.gridVeiculos.rowCount() > 0):
            self.gridVeiculos.removeRow(0)

        row = 0
        while query.next():
            self.gridVeiculos.insertRow(row)
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

            self.gridVeiculos.setItem(row, 0, codigoVeic)
            self.gridVeiculos.setItem(row, 1, modelo)
            self.gridVeiculos.setItem(row, 2, marca)
            self.gridVeiculos.setItem(row, 3, anoModelo)
            self.gridVeiculos.setItem(row, 4, placa)
            self.gridVeiculos.setItem(row, 5, alugado)
            self.gridVeiculos.setItem(row, 6, batido)
            self.gridVeiculos.setItem(row, 7, kmAtual)
            self.gridVeiculos.setItem(row, 8, valorDiaria)
            self.gridVeiculos.setItem(row, 9, descricao)
            self.gridVeiculos.setItem(row, 10, tipoVeiculo)

            row = row + 1

    def setupUi(self, frmPesqVeiculos):
        frmPesqVeiculos.setObjectName("frmPesqVeiculos")
        frmPesqVeiculos.resize(820, 491)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Integrador_6\Imagens/Lista_Veiculos_preto.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmPesqVeiculos.setWindowIcon(icon)
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
        icon.addPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Integrador_6\Imagens/Pesquisar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Integrador_6\Imagens/Alterar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon2.addPixmap(QtGui.QPixmap("D:\PyCharm\projetos\Projeto_Integrador_6\Imagens/lixeira.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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

        # BTN PESQUISAR CLICK #
        self.btnPesquisa.clicked.connect(lambda: self.PesquisarVeiculo(self.edtPesquisa_2.text(), self.cbPesquisa.currentText()))
        # BTN EXCLUIR CLICK
        self.btnExcluir.clicked.connect(lambda: self.ExcluirVeiculo_Click())
        # BTN ALTERAR CLICK###
        self.btnAlterar_2.clicked.connect(lambda: self.AlterarVeiculo_Click())

    def retranslateUi(self, frmPesqVeiculos):
        _translate = QtCore.QCoreApplication.translate
        frmPesqVeiculos.setWindowTitle(_translate("frmPesqVeiculos", "Lista de Veiculos"))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frmPesqVeiculos = QtWidgets.QDialog()
    ui = Ui_frmPesqVeiculos()
    ui.setupUi(frmPesqVeiculos)
    frmPesqVeiculos.show()
    sys.exit(app.exec_())
