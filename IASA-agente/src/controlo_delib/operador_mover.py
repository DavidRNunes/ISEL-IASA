import math

from mod import Estado, EstadoAgente, Operador
from sae import Accao


class OperadorMover(Operador):
    """
    Classe que implemementa a interface Operador permitindo criar os
    operadores entre os diferentes estados no modelo do mundo

    A implementação desta classe cria os operadores associados aos estados
    do modelo do mundo, associando a acção de movimento do agente numa
    direcção fornecida ao estado presente numa determinada posição no mundo
    permitindo ao agente deslocar-se entre estados quando aplica o operador
    aqui criado. Essencialmente a classe OperadorMover implementa a acção
    de movimento do agente e quando aplicada retorna o novo estado do agente
    após a aplicação do operador de movimento que permite que o agente se
    desloque para uma nova posição no mundo

    @param modelo_mundo: modelo do mundo actual
    @param direccao: direcção da deslocação do agente

    @method aplicar: aplica o operador ao estado actual do agente, deslocando-o
        para uma nova posição, ou seja, um novo estado, caso este seja válido
    @method custo: custo da deslocação do agente para a nova posição
    """

    def __init__(self, modelo_mundo, direccao):
        """
        Método construtor da classe que guarda os parâmetros recebidos
        convertendo a direcção recebida para um valor do ângulo correspondente
        à mesma e implementa a acção de deslocamento nessa direcção

        @param modelo_mundo: estado actual do modelo do mundo
        @param direccao: direcção na qual se pretende deslocar o agente
        """
        self._ang = direccao.value
        self._modelo_mundo = modelo_mundo
        self._accao = Accao(direccao)

    @property
    def ang(self):
        """
        Propriedade que retorna o valor do ângulo da acção, correspondente ao
        valor da direcção do deslocamento
        """
        return self._ang

    @property
    def accao(self):
        """
        Propriedade que retorna a acção a executar pelo agente, correspondente
        à deslocação do estado actual para o estado de destino
        """
        return self._accao

    def aplicar(self, estado):
        """
        Método que permite aplicar o operador ao estado actual do agente

        É obtida a posição actual do agente, correspondente à posição do estado
        actual, e a esta posição é aplicada a transformação correspondente ao
        valor de um passo na direcção da acção do operador através de um vector
        calculado através de trigonometria, obtendo assim a posição final para
        onde o agente se deve deslocar. É então criado o estado final após a
        aplicação do operador e caso este seja um estado válido para o agente
        se deslocar, é retornado o novo estado do agente, efectivamente aplicando
        o operador e deslocando o agente para a nova posição

        @param estado: estado actual em que o agente se encontra
        @returns: novo estado do agente após aplicação do operador, caso este seja
            um estado válido no modelo do mundo, None em caso contrário
        """
        x, y = estado.posicao
        dx = round(self._accao.passo * math.cos(self._ang))
        dy = - round(self._accao.passo * math.sin(self._ang))
        novo_estado = EstadoAgente((x+dx, y+dy))

        if novo_estado in self._modelo_mundo.estados():
            return novo_estado

    def custo(self, estado, estado_suc):
        """
        Método que retorna o custo de mover o agente para a nova posição
        que consiste na obtenção do valor máximo entre 1 e a distância
        compreendida entre a posição inicial e a posição final - qualquer
        operador tem um custo mínimo de 1

        @param estado: estado actual do agente
        @param estado_suc: estado final do agente após aplicação do operador
        @returns: 1 ou valor da distância entre os estados
        """
        return max(1, math.dist(estado.posicao, estado_suc.posicao))
