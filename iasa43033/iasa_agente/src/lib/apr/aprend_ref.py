from abc import ABC, abstractmethod


class AprendRef(ABC):
    """
    Classe abstrata que implementa a aprendizagem comportamental
    por reforço

    Este tipo de aprendizagem é obtido através da interação do agente
    com o mundo, visitando os vários estados e efectuando acções que
    lhe permitem obter um valor de reforço para a acção que efectuou,
    efectivamente permitindo-lhe saber a utilidade dessa acção. Através
    desta exploração o agente fica a conhecer o mundo e é então capaz
    de delinear um modelo de utilidade e política que lhe permitem
    navegar pelo mundo de uma forma mais eficiente

    @param mem_aprend: tipo de memória do agente
    @param sel_accao: estratégia de selecção de acção por parte do
        agente
    """

    def __init__(self, mem_aprend, sel_accao):
        """
        Método construtor da classe

        @param mem_aprend: tipo de memória que o agente dispõe
        @param sel_accao: método de selecionar a acção a executar
        """
        self._mem_aprend = mem_aprend
        self._sel_accao = sel_accao

    @abstractmethod
    def aprender(self, s, a, r, sn):
        """
        Método abstrato que representa a forma de aprendizagem do agente,
        quando implementado permite definir o valor Q(s,a) - valor de no
        estado s realizar a acção a - através do algoritmo implementado

        @param s: estado actual observado pelo agente
        @param a: acção efectuada
        @param r: reforço obtido pelo agente para a acção efectuada
        @param sn: estado seguinte após efectuar a acção
        """
