import math

from mod import Estado
from pee import Heuristica


class HeurDist(Heuristica):
    """
    Classe que implementa a interface da heurística, criando uma
    heurística relativa à distância entre dois estados, respectivamente
    os estados correspondentes ao estado actual do agente e ao estado
    que leva o agente ao objetivo final

    @param estado_final: estado correspondente ao estado do objetivo

    @method h: método que permite obter a distância entre o agente
        e o objetivo final
    """

    _estado_final: Estado
    """ Estado final correspondente ao objetivo """

    def __init__(self, estado_final):
        """
        Método construtor da classe heurística da distância        
        """
        self._estado_final = estado_final

    def h(self, estado):
        """
        Método que cria a função heuristica que permite obter
        a distância entre o estado actual e o objetivo através
        das posições dos mesmos no mundo

        @param estado: estado actual do agente
        @returns: distância entre o agente e o objetivo
        """
        return math.dist(estado.posicao, self._estado_final.posicao)
