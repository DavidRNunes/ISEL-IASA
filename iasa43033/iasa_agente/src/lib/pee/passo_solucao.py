from dataclasses import dataclass

from mod import Estado, Operador


@dataclass
class PassoSolucao:
    """
    Classe que guarda o formato de dados permitindo que estes sejam
    implementados por outra classe. Permite criar os passos da solução
    compostos por um estado actual e uma operação que permite atingir
    o próximo estado, alterando o estado do agente
    """

    estado: Estado
    operador: Operador
