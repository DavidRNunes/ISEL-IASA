from abc import ABC
from pee import MecanismoProcura
from pee import No
from pee import Solucao


class ProcuraGrafo(MecanismoProcura, ABC):
    """
    
    """

    def resolver(self, problema):
        """
        Altera o método da superclasse
        """
        no = No(problema.estado_inicial, problema.operadores)
        if problema.objetivo(no.estado):
            return Solucao(no)

        self._fronteira.inserir(no)
        self._explorados = [no.estado]
        while not self._fronteira.vazia:
            no = self._fronteira.remover
            for noSuc in self._expandir(problema, no):
                estado_noSuc = noSuc.estado
                if problema.objetivo(estado_noSuc):
                    return Solucao(noSuc)
                self._memorizar(noSuc)
        return None

    def _memorizar(self, no):
        """
        Implementa o método da superclasse
        """
        if self._manter(no):
            self._explorados.append(no.estado)
            self._fronteira.inserir(no)

    def _manter(self, no):
        """
        
        """
        for estado_explorado in self._explorados:
            if no.estado.__eq__(estado_explorado):
                return False

        return True