from .comportamento import Comportamento


class Reaccao(Comportamento):
    """
    Classe representativa de uma associação estímulo-resposta baseada na
    arquitectura reactiva que realiza a classe Comportamento.

    Perante a percepção do ambiente exterior atual por parte do agente é
    ativado um estímulo que, para uma intensidade superior a 0, ativa uma
    resposta por parte do agente que se traduz numa acção do mesmo. É
    implementado o método activar da classe Comportamento, que representa
    o módulo comportamental composto por reacções e/ou outros 
    comportamentos que por sua vez seguem a mesma regra estrutural de no
    seu interior poder ter reacções e/ou comportamentos
    """

    def __init__(self, estimulo, resposta):
        """
        Método construtor da classe Reaccao

        @param estimulo: estímulo associado à percepção detetada pelo agente
        @param resposta: resposta ao estímulo detetado em função da sua
            intensidade
        """

        self._estimulo = estimulo
        self._resposta = resposta

    def activar(self, percepcao):
        """
        Método que activa a detecção de um estímulo

        Perante a percepção do exterior adquirida pelo sensor do agente é obtida a
        intensidade do estímulo detectado, que, caso seja superior a 0 (ou seja, 
        caso seja confirmada a existência de um estímulo) é ativada a resposta
        correspondente ao estímulo detectado

        @param percepcao: estado atual do ambiente que rodeia o agente
            percepcionado pelo sensor do mesmo, traduzindo-se num estímulo
        @returns: a resposta ao estímulo detectado, ou seja, a acção a tomar
            pelo agente
        """

        intensidade = self._estimulo.detectar(percepcao)

        if intensidade > 0:
            accao = self._resposta.activar(percepcao, intensidade)

            return accao
