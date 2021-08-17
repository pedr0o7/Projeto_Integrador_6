from Model.DTO.ClienteDTO import ClienteDTO
from Model.DAO.ClienteDAO import ClienteDAO

class ClienteCTR:
    def CadastrarCliente(self, nome, cpf, endereco, email, telefone):
        clienteDTO = ClienteDTO
        clienteDTO.Nome = nome
        clienteDTO.CPF = cpf
        clienteDTO.Endereco = endereco
        clienteDTO.Email = email
        clienteDTO.Telefone = telefone

        clienteDAO = ClienteDAO
        clienteDAO.CadastrarCliente(self,clienteDTO)

    def AtualizarCliente(self, codigoCli, nome, CPF, endereco, email, telefone):

        clienteDTO = ClienteDTO
        clienteDTO.Nome = nome
        clienteDTO.CPF = CPF
        clienteDTO.Endereco = endereco
        clienteDTO.Email = email
        clienteDTO.Telefone = telefone

        clienteDAO = ClienteDAO
        clienteDAO.AtualizarCliente(self,codigoCli, clienteDTO)

    def PesquisarTodosClientes():
        clienteDAO = ClienteDAO
        query = clienteDAO.PesquisarTodosClientes()

        return query

    def PesquisarCliente(self, valor, tipo):

        clienteDAO = ClienteDAO
        query = clienteDAO.PesquisarCliente(valor, tipo)

        return query

    def ExcluirCliente(codigoCli):
        clienteDAO = ClienteDAO
        clienteDAO.ExcluirCliente(codigoCli)


def CadastrarCliente(nome, cpf, endereco, email, telefone):
    return None