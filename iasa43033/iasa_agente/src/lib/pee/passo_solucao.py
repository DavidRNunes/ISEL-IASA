from dataclasses import dataclass

from mod.estado import Estado
from mod.operador import Operador


@dataclass
class PassoSolucao:
    """
    Classe que guarda o formato de dados permitindo que estes sejam
    implementados por outra classe. Permite criar os passos necessários
    para obter a solução partindo do estado do nó e do operador que
    altera esse estado.
    """

    estado: Estado
    operador: Operador