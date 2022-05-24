from abc import ABC, abstractmethod

from mod import EstadoAgente, Operador
from sae import Elemento


class ModeloPlan(ABC):
    """
    Interface abstrata do modelo de planeamento

    O modelo de planeamento permite manter o estado actual do agente e
    a lista de estados que o mesmo pode atingir, bem como os operadores
    que permitem a alteração entre os vários estados. A aplicação desta
    interface permite criar uma representação interna do mundo que rodeia
    o agente permitindo apicar um processo de tomada de decisões sobre
    o ambiente
    """

    @abstractmethod
    def estado(self):
        """
        Método abstrato que quando implementado permite obter o estado
        actual do agente no ambiente
        """

    @abstractmethod
    def estados(self):
        """
        Método que quando implementado retorna a lista de estados que o
        agente pode alcançar
        """

    @abstractmethod
    def operadores(self):
        """
        Método que quando implementado retorna a lista de operadores
        que permitem ao agente alcançar novos estados válidos no ambiente
        """
