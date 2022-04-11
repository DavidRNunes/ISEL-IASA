from ecr.estimulo import Estimulo
from sae import Elemento


class EstimuloAlvo(Estimulo):
    """
    Classe associada à classe Estimulo implementando o estímulo correspondente
    à detecção de um alvo por parte do agente

    Esta classe permite criar o estímulo percepcionado pelo agente aquando da
    detecção de um alvo numa determinada direção em estudo. Caso seja detectado
    um alvo na direcção pretendida, a distância entre o agente e esse mesmo alvo
    é inversamente proporcional à intensidade do estímulo, pelo que um alvo que
    se encontre mais próximo do agente (a uma distância inferior) traduz-se num
    valor de intensidade mais alto

    @param direccao: direcção em estudo que se pretende verificar a existência
        de um alvo
    @param gama: float no intervalo 0 a 1 exclusivo que permite obter o valor da
        intensidade do estímulo, default = 0.9

    @method detectar: método que permite verificar se um alvo é detectado
    """

    def __init__(self, direccao, gama=0.9):
        """
        Método construtor da classe

        Implementa-se o estímulo para a direcção fornecida em função da gama
        fornecida, que permite obter a intensidade do estímulo inversamente
        proporcional à distância compreendida entre o estímulo detectado e o
        agente

        @param direccao: direcção em estudo por parte do agente
        @param gama: float no intervalo 0 a 1 exclusivo que permite inverter
            o valor da distância entre o agente e um alvo de forma a obter a
            intensidade do estímulo detectado, default = 0.9
        """
        self._direccao = direccao
        self._gama = gama

    def detectar(self, percepcao):
        """
        Método que permite ao agente verificar se detecta algum alvo

        Em função da percepção do ambiente atual é verificada para a direcção
        em estudo se o agente detecta algum elemento do tipo alvo, ou seja, é
        testado se o agente detecta um alvo na direcção em estudo. Caso seja
        detectado um alvo é retornado o valor da intensidade do estímulo,
        traduzido num valor inversamente proporcional à distância, ou seja,
        um alvo a uma distância superior do agente retorna um valor de
        intensidade mais baixo do que um alvo próximo do agente

        @param percepcção: percepção atual do ambiente que rodeia o agente
        @returns: 0 se não for detetado nenhum alvo ou um float que varia
            inversamente em função da distância a que se encontra o alvo
        """
        elemento, distancia, _ = percepcao[self._direccao]

        if elemento == Elemento.ALVO:
            return self._gama**distancia
        else:
            return 0
