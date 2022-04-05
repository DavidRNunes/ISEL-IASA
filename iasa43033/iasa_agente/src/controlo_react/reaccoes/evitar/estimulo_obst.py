
from ecr.estimulo import Estimulo


class EstimuloObst(Estimulo):
    """
    Classe que implementa o estímulo e representa a deteção de um obstáculo
    por parte do agente
    """

    def __init__(self, direccao, intensidade=1.):
        self._direccao = direccao
        self._intensidade = intensidade
    
    def detectar(self, percepcao):
        if percepcao.contacto_obst(self._direccao):
            return self._intensidade
        else:
            return 0