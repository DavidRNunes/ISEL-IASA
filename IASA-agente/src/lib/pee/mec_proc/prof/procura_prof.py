from pee.mec_proc.fronteira.fronteira_lifo import FronteiraLIFO
from pee.mec_proc.mecanismo_procura import MecanismoProcura


class ProcuraProf(MecanismoProcura):
    """
    Classe que implementa o mecanismo de procura em profundidade

    O mecanismo de procura em profundidade expande sempre o nó mais recente
    traduzindo-se no último nó adicionado à lista de nós da fronteira de
    exploração. O processo repete-se até ao maior nível de profundidade
    do ramo, até onde o nó explorado não tenha sucessores, voltando então
    atrás ao nó mais profundo que ainda tenha sucessores por expandir. O
    algoritmo termina quando encontra a primeira solução, independentemente
    do custo da solução encontrada.

    @method _iniciar_fronteira: inicia uma fronteira LIFO sem nós
    @method _memorizar: adiciona um nó ao fim da lista da fronteira
    """

    def _iniciar_fronteira(self):
        """
        Implementa o método da superclasse, retornando uma fronteira LIFO
        sem nós

        @returns: fronteira do tipo LIFO vazia
        """
        self._fronteira = FronteiraLIFO()

        return self._fronteira

    def _memorizar(self, no):
        """
        Implementa o método da superclasse, memorizando o nó fornecido na
        fronteira de exploração com um método LIFO, colocando o novo nó
        no fim da lista de nós

        @param no: nó que se pretende memorizar
        """
        self._fronteira.inserir(no)
        