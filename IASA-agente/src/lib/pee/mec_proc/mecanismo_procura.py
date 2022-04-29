from abc import ABC, abstractmethod
from no import No
from pee import Solucao
from mod import Estado
from mod import Operador
from mod.problema import Problema
from pee import Fronteira


class MecanismoProcura(ABC):
    """
    Classe abstrata que define um mecanismo de procura
    """

    def __init__(self):
        """
        
        """
        self._fronteira = _iniciar_fronteira()
    
    def resolver(self, problema):
        """
        Implementa o algoritmo
        @returns: solução
        """

    def _expandir(self, problema, no):
        """
        
        @returns: lista de nós
        """
        for operador in problema.operadores:
            estado_suc = operador.aplicar(no.estado)
            if estado_suc:
                yield No(estado_suc, operador, no)
    
    @abstractmethod
    def _iniciar_fronteira(self):
        """
        
        @returns: fronteira
        """

    @abstractmethod
    def _memorizar(self, no):
        """
        
        """