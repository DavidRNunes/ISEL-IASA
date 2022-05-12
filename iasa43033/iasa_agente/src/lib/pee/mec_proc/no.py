from mod.estado import Estado
from mod.operador import Operador


class No():
    """
    Classe que representa uma etapa de procura numa árvore de procura

    Nos algoritmos de procura é comum abordar o processo de procura como
    uma árvore de procura em detrimento de um grafo do espaço de estados,
    onde a árvore de procura permite descrever os caminhos entre os estados
    caminhando para o objetivo, podendo existir multiplos caminhos para um
    qualquer estado, traduzindo-se isso em múltiplos nós cada um com um
    caminho único até ao estado inicial (raiz). Um nó é portanto uma das
    etapas de procura da árvore, ou seja, um dos estados do espaço de
    estados do problema

    @param estado: estado ao qual o nó corresponde
    @param operador: operador associado ao nó, default = None
    @param antecessor: estado antecessor, default = None

    @method __lt__: método do Python que compara dois objetos verificando
        se o primeiro é menor que o segundo
    """

    _profundidade = 0
    """ Profundidade do nó """
    _custo = 0.0
    """ Custo da operação do nó (double) """

    def __init__(self, estado, operador = None, antecessor = None):
        """
        Método construtor da classe, guarda os seus atributos

        @param estado: estado ao qual o nó corresponde
        @param operador: operador que associa o estado inicial (antecessor)
            ao estado sucessor (estado), default = None
        @param antecessor: estado antecessor, default = None
        """
        self._estado = estado
        self._operador = operador
        self._antecessor = antecessor
        if operador:
            self._custo = operador.custo(antecessor, estado)

    @property
    def profundidade(self):
        """
        Propriedade que permite obter o valor da profundidade do nó
        """
        return self._profundidade

    @property
    def custo(self):
        """
        Propriedade que permite obter o valor do custo da operação do nó
        """
        return self._custo

    @property
    def estado(self):
        """
        Propriedade que permite obter o estado correspondente ao nó actual
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
        Propriedade que permite obter o estado antecessor do nó
        """
        return self._antecessor

    def __lt__(self, no):
        """
        Método de comparação do Python que verifica se o primeiro objeto
        fornecido é menor do que o segundo objeto fornecido

        Através deste método podemos fazer a comparação entre dois nós
        para saber se o nó actual tem um custo menor do que o nó com o qual
        pretendemos comparar

        @param no: nó com o qual se pretende comparar o custo do próprio nó
        @returns: valor booleano da comparação entre dois nós, retorna true
            se o nó actual tiver um custo menor do que o nó com o qual
            estamos a comparar
        """
        return self.custo < no.custo