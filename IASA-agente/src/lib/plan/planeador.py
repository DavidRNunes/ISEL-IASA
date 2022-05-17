from abc import ABC, abstractmethod


class Planeador(ABC):
    """
    Interface abstrata do planeador
    """

    @abstractmethod
    def planear(self, modelo_plan, objetivos):
        """
        
        """

    @abstractmethod
    def obter_accao(self, estado):
        """
        
        """

    @abstractmethod
    def plano_valido(self, estado):
        """
        
        """

    @abstractmethod
    def terminar_plano(self):
        """
        
        """