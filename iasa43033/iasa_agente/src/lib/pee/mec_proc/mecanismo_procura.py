from abc import ABC, abstractmethod
from no import No
from pee import Solucao
from mod import Estado
from mod import Operador
from mod.problema import Problema


class MecanismoProcura(ABC):
    """
    Classe abstrata que define um mecanismo de procura
    """

    def __init__(self):
        """
        
        """
    
    def resolver(self, problema):
        """
        Implementa o algoritmo
        @returns: solução
        """

    def expandir(self, problema, no):
        """
        
        @returns: lista de nós
        """
        for operador in problema.operadores:
            estado_suc = operador.aplicar(no.estado)
            if estado_suc:
                yield No(estado_suc, operador, no)
    
    @abstractmethod
    def iniciar_fronteira(self):
        """
        
        @returns: fronteira
        """

    @abstractmethod
    def memorizar(self, no):
        """
        
        """