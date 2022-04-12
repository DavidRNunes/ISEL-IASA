from pee.mec_proc.fronteira.fronteira import Fronteira
from heapq import heappush, heappop
from pee.mec_proc.fronteira import Avaliador


class FronteiraPrioridade(Fronteira):
    """
    
    """

    def __init__(self, avaliador):
        """
        
        """

    def inserir(self, no):
        """
        Implementação do método inserir da superclasse
        """
        prioridade_no = self.avaliador.prioridade(no)
        heappush(self._nos, (prioridade_no, no))
    
    def remover(self):
        """
        Alteração do método da superclasse
        """
        _, no = heappop(self._nos)
        return no