from PyQt5.QtSql import QSqlQuery
from DataBase.ConexaoSQL import ConexaoSQL

class VeiculoDAO:
    def CadastrarVeiculo(veiculo):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        query = QSqlQuery()
        query.prepare("INSERT INTO Veiculo(Modelo, Marca, AnoModelo, Placa, "
                      "Alugado, Batido, KmAtual, ValorDiaria, Descricao, TipoVeiculo) "
                      "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
        query.addBindValue(veiculo.Modelo)
        query.addBindValue(veiculo.Marca)
        query.addBindValue(veiculo.AnoModelo)
        query.addBindValue(veiculo.Placa)
        query.addBindValue(veiculo.Alugado)
        query.addBindValue(veiculo.Batido)
        query.addBindValue(veiculo.KmAtual)
        query.addBindValue(veiculo.ValorDiaria)
        query.addBindValue(veiculo.Descricao)
        query.addBindValue(veiculo.TipoVeiculo)

        query.exec_()
        db.commit()

    def AtualizarVeiculo(codigoVeic, veiculo):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        query = QSqlQuery()
        query.prepare("UPDATE Veiculo SET Modelo = '"+veiculo.Modelo+"', Marca = '"+veiculo.Marca
                      +"', AnoModelo = "+veiculo.AnoModelo+", Placa = '"+veiculo.Placa
                      +"', Alugado = '"+veiculo.Alugado+"', Batido = '"+veiculo.Batido
                      +"', KmAtual = '"+veiculo.KmAtual+"', ValorDiaria = '"+veiculo.ValorDiaria
                      +"', Descricao = '"+veiculo.Descricao+"', TipoVeiculo = '"+veiculo.TipoVeiculo
                      +"' WHERE CodigoVeic = "+codigoVeic)
        query.exec_()
        db.commit()

    def ExcluirVeiculo(codigoVeic):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        query = QSqlQuery()
        query.prepare("DELETE FROM Veiculo WHERE CodigoVeic=:codigoVeic")
        query.bindValue(":codigoVeic", codigoVeic)
        query.exec_()
        db.commit()

    def PesquisarVeiculosDisponiveis():
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        sql = "select CodigoVeic, Modelo,  Marca, AnoModelo, Placa, Alugado, Batido, printf('%.3f', KmAtual) AS 'KmAtual', 	printf('R$ %.2f', ValorDiaria) as 'ValorDiaria', Descricao, TipoVeiculo FROM Veiculo WHERE Alugado = 'Não'"
        query = QSqlQuery(sql)

        return query

    def PesquisarTodosVeiculos():
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        sql = "select CodigoVeic, Modelo,  Marca, AnoModelo, Placa, Alugado, Batido, printf('%.3f', KmAtual) AS 'KmAtual', 	printf('R$ %.2f', ValorDiaria) as 'ValorDiaria', Descricao, TipoVeiculo FROM Veiculo"
        query = QSqlQuery(sql)

        return query

    def PesquisarVeiculo(valor, tipo):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        if tipo=='Código':
            sql = "select CodigoVeic, Modelo,  Marca, AnoModelo, Placa, Alugado, Batido, printf('%.3f', KmAtual) AS 'KmAtual', 	printf('R$ %.2f', ValorDiaria) as 'ValorDiaria', Descricao, TipoVeiculo FROM Veiculo where CodigoVeic = " + valor
            query = QSqlQuery(sql)
        elif tipo=='Marca':
            sql = "select CodigoVeic, Modelo,  Marca, AnoModelo, Placa, Alugado, Batido, printf('%.3f', KmAtual) AS 'KmAtual', 	printf('R$ %.2f', ValorDiaria) as 'ValorDiaria', Descricao, TipoVeiculo FROM Veiculo Veiculo where Marca LIKE '"+valor+"%'"
            query = QSqlQuery(sql)
        elif tipo=='Modelo':
            sql = "select CodigoVeic, Modelo,  Marca, AnoModelo, Placa, Alugado, Batido, printf('%.3f', KmAtual) AS 'KmAtual', 	printf('R$ %.2f', ValorDiaria) as 'ValorDiaria', Descricao, TipoVeiculo FROM Veiculo where Modelo LIKE '"+valor+"%'"
            query = QSqlQuery(sql)
        elif tipo=='Disponível':
            sql = "select CodigoVeic, Modelo,  Marca, AnoModelo, Placa, Alugado, Batido, printf('%.3f', KmAtual) AS 'KmAtual', 	printf('R$ %.2f', ValorDiaria) as 'ValorDiaria', Descricao, TipoVeiculo FROM Veiculo where Alugado = 'Não'"
            query = QSqlQuery(sql)
        elif tipo=='Alugado':
            sql = "select CodigoVeic, Modelo,  Marca, AnoModelo, Placa, Alugado, Batido, printf('%.3f', KmAtual) AS 'KmAtual', 	printf('R$ %.2f', ValorDiaria) as 'ValorDiaria', Descricao, TipoVeiculo FROM Veiculo Veiculo where Alugado = 'Sim'"
            query = QSqlQuery(sql)

        return query




