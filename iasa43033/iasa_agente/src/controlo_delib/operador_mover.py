import math
from mod.agente.estado_agente import EstadoAgente
from mod.estado import Estado
from mod.operador import Operador
from sae.agente.accao import Accao


class OperadorMover(Operador):
    """
    Classe que implemementa a interface Operador permitindo criar os
    operadores entre os diferentes estados no modelo do mundo

    Através desta classe são criados os operadores que permitem ao
    agente deslocar-se no mundo que o rodeia
    """

    def __init__(self, modelo_mundo, direccao):
        """
        
        """
        self._ang = direccao.value
        self._modelo_mundo = modelo_mundo
        self._accao = Accao(direccao)

    @property
    def ang(self):

        return self._ang

    @property
    def accao(self):

        return self._accao

    def aplicar(self, estado):
        """
        
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
        que consiste no máximo entre 1 e a distância de se mover o agente

        """
        return max(1, math.dist(estado.posicao, estado_suc.posicao))
