from Model.DTO.AluguelDTO import AluguelDTO
from Model.DAO.AluguelDAO import AluguelDAO

class AluguelCTR:
    def CadastrarAluguel(self,DataAluguel, DataPrazo, ValorAluguel,
                      ValorMulta, KmEntrada, CodigoCli, CodigoVeic):
        aluguelDTO = AluguelDTO
        aluguelDTO.DataAluguel = DataAluguel
        aluguelDTO.DataPrazo = DataPrazo

        aluguelDTO.ValorAluguel = ValorAluguel
        aluguelDTO.ValorMulta = ValorMulta
        aluguelDTO.KmEntrada = KmEntrada

        aluguelDTO.CodigoCli = CodigoCli
        aluguelDTO.CodigoVeic = CodigoVeic

        aluguelDAO = AluguelDAO
        aluguelDAO.CadastrarAluguel(self,aluguelDTO)

    def PesquisarTodosAluguel():

        aluguelDAO = AluguelDAO
        query = aluguelDAO.PesquisarTodosAluguel()

        return query

    def PesquisarAluguel(self,valor, tipo):
        aluguelDAO = AluguelDAO
        query = aluguelDAO.PesquisarAluguel(valor, tipo)

        return query

    def DevolverVeiculo(self,codigoAlug, dataDevol, valorMulta, kmSaida):
        aluguelDTO = AluguelDTO

        aluguelDTO.DataDevolucao = dataDevol
        aluguelDTO.ValorMulta = valorMulta
        aluguelDTO.KmSaida = kmSaida


        aluguelDAO = AluguelDAO
        aluguelDAO.DevolverVeiculo(codigoAlug, aluguelDTO)
