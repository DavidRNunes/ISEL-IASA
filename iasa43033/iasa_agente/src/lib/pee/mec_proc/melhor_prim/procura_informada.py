from abc import ABC

from ..fronteira.aval.heuristica import Heuristica
from .procura_melhor_prim import ProcuraMelhorPrim


class ProcuraInformada(ProcuraMelhorPrim, ABC):
    """
    Classe abstrata que define o mecanismo de procura informada

    Procura informada tira partido de conhecimento do domínio do problema
    para ordenar a fronteira de exploração, fazendo uso dessa avaliação
    sobre o conhecimento para colocar os nós mais promissores numa posição
    prioritária para serem explorados primeiro. Esta procura torna-se muito
    mais eficiente a encontrar soluções do que a procura não informada, mas
    é necessário ter em atenção ao método de avaliação heuristico, uma vez
    que este deve ser simples de calcular de forma a não aumentar o tempo
    necessário para as estimações da prioridade.

    @method resolver: estende o método da superclasse ProcuraGrafo adicionando
        a heuristica
    """

    _heuristica: Heuristica

    def resolver(self, problema, heuristica):
        """
        Método que estende o método resolver definido na classe ProcuraGrafo
        adicionando a heuristica

        @param problema: estado inicial do agente, operadores e objetivos
        @param heuristica: heuristica definida para o problema
        @returns: solução do problema ou None caso não haja solução, recorrendo
            à superclasse
        """
        self._heuristica = heuristica

        return super().resolver(problema)
