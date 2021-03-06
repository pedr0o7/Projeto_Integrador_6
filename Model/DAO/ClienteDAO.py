from PyQt5.QtSql import QSqlQuery
from DataBase.ConexaoSQL import ConexaoSQL

class ClienteDAO:
    def CadastrarCliente (self,cliente):

        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        query = QSqlQuery()
        query.prepare("INSERT INTO Cliente(Nome, CPF, Endereco, Email, Telefone) "
                      "VALUES (?, ?, ?, ?, ?)")
        query.addBindValue(cliente.Nome)
        query.addBindValue(cliente.CPF)
        query.addBindValue(cliente.Endereco)
        query.addBindValue(cliente.Email)
        query.addBindValue(cliente.Telefone)
        query.exec_()
        db.commit()

    def AtualizarCliente(self,codigoCli, cliente):

        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        query = QSqlQuery()
        query.prepare("UPDATE Cliente SET Nome = '"+cliente.Nome+"', CPF = '"+cliente.CPF
                      +"', Endereco = '"+cliente.Endereco+"', Email = '"+cliente.Email
                      +"', Telefone = '"+cliente.Telefone
                      +"' WHERE CodigoCli = "+codigoCli)
        query.exec_()
        db.commit()

    def ExcluirCliente(codigoCli):
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        query = QSqlQuery()
        query.prepare("DELETE FROM Cliente WHERE CodigoCli=:codigoCli")
        query.bindValue(":codigoCli", codigoCli)
        query.exec_()
        db.commit()

    def PesquisarTodosClientes():
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()
        sql = "SELECT CodigoCli, Nome, printf('%.3d.%.3d.%.3d-%.2d',substr(CPF,1,3),substr(CPF,4,3), substr(CPF,7,3), substr(CPF,10,2)) as CPF, Endereco, Email, printf('(%.2d) %.1d %.4d-%.4d', substr(Telefone,1,2),substr(Telefone,3,1), substr(Telefone,4,4),substr(Telefone,8,4)) as TELEFONE FROM Cliente;"
        query = QSqlQuery(sql)

        return query

    def PesquisarCliente(valor, tipo):
        valor = valor.replace(".","")
        valor = valor.replace("-","")
        conn = ConexaoSQL
        db = conn.getConexao()
        db.open()

        if tipo=='C??digo':
            sql = "SELECT CodigoCli, Nome, printf('%.3d.%.3d.%.3d-%.2d',substr(CPF,1,3),substr(CPF,4,3), substr(CPF,7,3), substr(CPF,10,2)) as CPF, Endereco, Email, printf('(%.2d) %.1d %.4d-%.4d', substr(Telefone,1,2),substr(Telefone,3,1), substr(Telefone,4,4),substr(Telefone,8,4)) as TELEFONE FROM Cliente where CodigoCli = " + valor
            query = QSqlQuery(sql)
        elif tipo=='Nome':
            sql = "SELECT CodigoCli, Nome, printf('%.3d.%.3d.%.3d-%.2d',substr(CPF,1,3),substr(CPF,4,3), substr(CPF,7,3), substr(CPF,10,2)) as CPF, Endereco, Email, printf('(%.2d) %.1d %.4d-%.4d', substr(Telefone,1,2),substr(Telefone,3,1), substr(Telefone,4,4),substr(Telefone,8,4)) as TELEFONE FROM Cliente where Nome LIKE '"+valor+"%'"
            query = QSqlQuery(sql)
        elif tipo=='CPF':
            
            sql = "SELECT CodigoCli, Nome, printf('%.3d.%.3d.%.3d-%.2d',substr(CPF,1,3),substr(CPF,4,3), substr(CPF,7,3), substr(CPF,10,2)) as CPF, Endereco, Email, printf('(%.2d) %.1d %.4d-%.4d', substr(Telefone,1,2),substr(Telefone,3,1), substr(Telefone,4,4),substr(Telefone,8,4)) as TELEFONE FROM Cliente where CPF = '" + valor+"'"
            query = QSqlQuery(sql)

        return query




