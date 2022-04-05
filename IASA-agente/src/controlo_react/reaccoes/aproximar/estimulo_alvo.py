from ecr.estimulo import Estimulo
from sae import Elemento


class EstimuloAlvo(Estimulo):
    """
    Classe que implementa a classe Estimulo, representante do estímulo
    percepcionado pelo agente, neste caso o estímulo é um alvo para o qual
    o agente se deve deslocar


    """

    def __init__(self, direccao, gama=0.9):
        """
        Método construtor da classe

        @param gama: no intervalo 0 a 1 exclusivo
        """
        self._direccao = direccao
        self._gama = gama

    def detectar(self, percepcao):
        """
        Método que permite ao agente detectar se detecta algum alvo

        @param percepcção: percepção atual do ambiente que rodeia o agente
        @returns: 0 se não for detetado nenhum alvo ou um float que varia
            em função da distância a que se encontra o alvo
        """
        elemento, distancia, _ = percepcao[self._direccao]

        if elemento == Elemento.ALVO:
            return self._gama**distancia
        else:
            return 0
