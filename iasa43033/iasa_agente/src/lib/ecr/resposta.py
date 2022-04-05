class Resposta:
    """
    Classe que representa a resposta ativada pelo estímulo

    Perante o estímulo percepcionado o agente responde ao mesmo com uma
    acção predefinida
    """

    def __init__(self, accao):
        """
        Método construtor da classe resposta

        @param accao: acção que o agente deve executar
        """
        self._accao = accao

    def activar(self, percepcao, intensidade=0):
        """
        Método que activa a execução da acção por parte do agente

        É definida a prioridade da acção em função da intensidade do
        estímulo percepcionado, traduzindo-se numa hierarquia prioritária
        onde uma resposta pode ser executada em função da intensidade do
        estímulo

        @param percepcao: estado atual do ambiente que rodeia o agente
        @type intensidade: int
        @param intensidade: intensidade do estímulo percepcionado
            (default é 0)
        @returns: a acção a executar pelo agente com a prioridade atualizada
        """
        self._accao.prioridade = intensidade

        return self._accao
