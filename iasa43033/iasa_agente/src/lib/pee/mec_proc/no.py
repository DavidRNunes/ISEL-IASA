from mod.estado import Estado
from mod.operador import Operador


class No():

    profundidade = 0
    """ Profundidade do nó """
    custo = 0.0
    """ Custo da operação do nó (double) """

    def __init__(self, estado, operador = None, antecessor = None):
        """
        
        """
        self._estado = estado
        self._operador = operador
        self._antecessor = antecessor

    @property
    def profundidade(self):
        """
        Propriedade que permite obter a profundidade do nó
        """
        return self.profundidade

    @property
    def custo(self):
        """
        Propriedade que permite obter o custo da operação do nó
        """
        return self.custo

    @property
    def estado(self):
        """
        Propriedade que permite obter o estado no nó actual
        """
        return self._estado

    @property
    def operador(self):
        """
        Propriedade que permite obter o operador do nó
        """
        return self._operador

    @property
    def antecessor(self):
        """
        Propriedade que permite obter o antecessor do nó
        """
        return self._antecessor

    def __lt__(self, no):
        """
        Método de comparação do Python que verifica se o primeiro objeto
        fornecido é menor do que o segundo objeto fornecido

        Através deste método podemos fazer a comparação entre dois nós
        para saber se o nó actual tem um custo menor do que o nó com o qual
        pretendemos comparar
        
        @returns: valor booleano da comparação entre dois nós, retorna true
            se o nó actual tiver um custo menor do que o nó com o qual
            estamos a comparar
        """
        return self.custo < no.custo