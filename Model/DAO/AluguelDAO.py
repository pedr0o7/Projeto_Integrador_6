from PyQt5.QtSql import QSqlQuery
from DataBase.ConexaoSQL import ConexaoSQL

class AluguelDAO:
    def CadastrarAluguel(self,aluguel):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        query = QSqlQuery()


        query.prepare("UPDATE Veiculo SET Alugado = 'Sim' WHERE CodigoVeic = "+aluguel.CodigoVeic)
        query.exec_()
        db.commit()

        query.prepare("INSERT INTO Aluguel(DataAluguel, DataPrazo, DataDevolucao, ValorAluguel, "
                      "ValorMulta, KmEntrada, KmSaida, CodigoCli_, CodigoVeic_) "
                      "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")
        query.addBindValue(aluguel.DataAluguel)
        query.addBindValue(aluguel.DataPrazo)
        query.addBindValue(None)
        query.addBindValue(aluguel.ValorAluguel)
        query.addBindValue(aluguel.ValorMulta)
        query.addBindValue(aluguel.KmEntrada)
        query.addBindValue(None)
        query.addBindValue(aluguel.CodigoCli)
        query.addBindValue(aluguel.CodigoVeic)
        query.exec_()
        db.commit()

    def PesquisarTodosAluguel():

        conn = ConexaoSQL

        db = conn.getConexao()

        db.open()

        sql = "SELECT CodigoAlug, DataAluguel,DataPrazo, DataDevolucao, printf('R$ %.2f', ValorAluguel) as 'ValorAluguel', printf('R$ %.2f', ValorMulta) AS 'ValorMulta', printf('%.3f', KmEntrada) AS 'KmEntrada', printf('%.3f', KmSaida) AS 'KmSaida',CodigoCli_, (CodigoVeic_ || ' - ' || Modelo) as 'CodigoVeic_',Nome as 'Nome' from Aluguel as a, Veiculo as v, Cliente as c WHERE a.CodigoVeic_ = v.CodigoVeic and a.CodigoCli_ = c.CodigoCli ORDER by CodigoAlug DESC;"
        query = QSqlQuery(sql)

        return query

    def PesquisarAluguel(valor, tipo):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        if tipo=='Código Aluguel':
            sql = "SELECT CodigoAlug, DataAluguel,DataPrazo, DataDevolucao, printf('R$ %.2f', ValorAluguel) as 'ValorAluguel', printf('R$ %.2f', ValorMulta) AS 'ValorMulta', printf('%.3f', KmEntrada) AS 'KmEntrada', printf('%.3f', KmSaida) AS 'KmSaida',CodigoCli_, (CodigoVeic_ || ' - ' || Modelo) as 'CodigoVeic_',Nome as 'Nome' from Aluguel as a, Veiculo as v, Cliente as c WHERE a.CodigoVeic_ = v.CodigoVeic and a.CodigoCli_ = c.CodigoCli and CodigoAlug = " + valor
            query = QSqlQuery(sql)
        elif tipo=='Código Cliente':
            sql = "SELECT CodigoAlug, DataAluguel,DataPrazo, DataDevolucao, printf('R$ %.2f', ValorAluguel) as 'ValorAluguel', printf('R$ %.2f', ValorMulta) AS 'ValorMulta', printf('%.3f', KmEntrada) AS 'KmEntrada', printf('%.3f', KmSaida) AS 'KmSaida',CodigoCli_, (CodigoVeic_ || ' - ' || Modelo) as 'CodigoVeic_',Nome as 'Nome' from Aluguel as a, Veiculo as v, Cliente as c WHERE a.CodigoVeic_ = v.CodigoVeic and a.CodigoCli_ = c.CodigoCli and CodigoCli_ = "+valor
            query = QSqlQuery(sql)
        elif tipo=='Código Veículo':
            sql = "SELECT CodigoAlug, DataAluguel,DataPrazo, DataDevolucao, printf('R$ %.2f', ValorAluguel) as 'ValorAluguel', printf('R$ %.2f', ValorMulta) AS 'ValorMulta', printf('%.3f', KmEntrada) AS 'KmEntrada', printf('%.3f', KmSaida) AS 'KmSaida',CodigoCli_, (CodigoVeic_ || ' - ' || Modelo) as 'CodigoVeic_',Nome as 'Nome' from Aluguel as a, Veiculo as v, Cliente as c WHERE a.CodigoVeic_ = v.CodigoVeic and a.CodigoCli_ = c.CodigoCli and CodigoVeic_ = " + valor
            query = QSqlQuery(sql)
        elif tipo=='Nome Cliente':
            sql = "SELECT CodigoAlug, DataAluguel,DataPrazo, DataDevolucao, printf('R$ %.2f', ValorAluguel) as 'ValorAluguel', printf('R$ %.2f', ValorMulta) AS 'ValorMulta', printf('%.3f', KmEntrada) AS 'KmEntrada', printf('%.3f', KmSaida) AS 'KmSaida',CodigoCli_, (CodigoVeic_ || ' - ' || Modelo) as 'CodigoVeic_',Nome as 'Nome' from Aluguel as a, Veiculo as v, Cliente as c WHERE a.CodigoVeic_ = v.CodigoVeic and a.CodigoCli_ = c.CodigoCli and Nome LIKE '"+valor+"%'"
            query = QSqlQuery(sql)

        return query

    def DevolverVeiculo(codigoAlug, aluguel):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()



        select = "SELECT Veiculo.CodigoVeic FROM Aluguel"\
                      " INNER JOIN Veiculo ON Aluguel.CodigoVeic_ = Veiculo.CodigoVeic"\
                      " WHERE Aluguel.CodigoAlug = "+codigoAlug

        query = QSqlQuery(select)

        while query.next():
            codigoVeic = str(query.value(0))

        sql = "UPDATE Veiculo SET Alugado = 'Não' WHERE CodigoVeic_ = "+codigoVeic
        query.prepare(sql)
        query.exec_()
        db.commit()


        sql = "UPDATE Aluguel SET DataDevolucao = '"+aluguel.DataDevolucao+"', ValorMulta = '"+aluguel.ValorMulta\
                      +"', KmSaida = '"+aluguel.KmSaida\
                      +"' WHERE CodigoAlug = "+codigoAlug

        query.prepare(sql)

        query.exec_()
        db.commit()
