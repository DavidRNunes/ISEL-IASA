from dataclasses import dataclass

from mod.estado import Estado
from mod.operador import Operador


@dataclass
class PassoSolucao:
    """
    
    """

    estado: Estado
    operador: Operador