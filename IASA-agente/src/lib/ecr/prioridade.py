from ecr.comport_comp import ComportComp


class Prioridade(ComportComp):
    """
    Classe que implementa a classe abstrata ComportComp correspondente aos
    comportamentos compostos implementando a selecção de acção sob forma de
    prioridade

    Perante as várias reacções contidas no comportamento composto em função da
    percepção do ambiente atual é implementada uma prioridade entre as reacções
    de forma a selecionar apenas uma delas para obter a acção que o agente deve
    executar. Esta prioridade varia ao longo do tempo e consiste num valor
    atribuido a cada reacção que pode variar em função de valores como a
    distância entre o agente e um objeto, por exemplo. A classe percorre a
    lista de acções e retorna a acção com a prioridade mais elevada para ser
    executada pelo agente.

    @method seleccionar_accao: método que percorre a lista de acções e seleciona
        a mais prioritária
    """

    def seleccionar_accao(self, accoes):
        """
        Método que percorre a lista de acções fornecida e seleciona aquela
        com maior prioridade.

        O parâmetro key define qual o parâmetro a que a função max se aplica,
        que nos permite obter a acção com o valor mais alto

        @param accoes: lista de acções
        @returns: a acção mais prioritária da lista, a executar pelo agente
        """
        if accoes:
            return max(accoes, key=lambda accao: accao.prioridade)
