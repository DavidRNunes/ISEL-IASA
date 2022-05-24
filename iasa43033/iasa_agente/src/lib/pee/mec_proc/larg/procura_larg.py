from ..fronteira.fronteira_fifo import FronteiraFIFO
from ..procura_grafo import ProcuraGrafo


class ProcuraLarg(ProcuraGrafo):
    """
    Classe que implementa o mecanismo de procura por grafos

    O método de procura em largura permite explorar os nós mais antigos
    primeiro, consistindo numa procura que explora todos os nós de uma
    profundidade antes de passar aos nós da profundidade seguinte: o nó
    da raiz é expandido, de seguida expandem-se todos os nós filho da
    raiz, de seguida todos os nós filho desses nós, e assim por diante.
    Esta estratégia é sistemática sendo considerada completa até mesmo
    em espaços de estados infinitos. Em termos de programação apenas
    é fornecida a fronteira pois os métodos implementados na superclasse
    ProcuraGrafo já implementam o algoritmo

    @method _iniciar_fronteira: inicia uma fronteira FIFO sem nós
    """

    def _iniciar_fronteira(self):
        """
        Implementa o método da superclasse, retornando uma fronteira FIFO
        sem nós

        @returns: fronteira do tipo FIFO vazia
        """

        return FronteiraFIFO()
