from abc import ABC, abstractmethod

from .comportamento import Comportamento


class ComportComp(Comportamento, ABC):
    """
    Classe abstrata que establece a possibilidade de formar comportamentos
    compostos, ou seja, um comportamento que possui no seu interior outros
    comportamentos, sejam eles simples ou também eles compostos.

    O comportamento composto permite ao agente definir um objetivo principal
    associado a outros subj-objetivos que lhe permitem atingir o objetivo
    principal - o comportamento define a forma de concretizar um objetivo,
    o comportamento composto permite associar sub-objetivos para concretizar
    um objetivo. Associado aos comportamentos compostos está ainda a
    prioridade das reacções, onde a selecção da acção a efectuar é decidida
    em função da prioridade da mesma.

    @param comportamentos: lista de comportamentos do comportamento composto

    @method activar: método que associa respostas aos comportamentos e retorna
        uma acção a praticar pelo agente
    @method seleccionar_accao: método abstrato que permite selecionar uma
        acção por entre as várias acções do comportamento composto
    """

    def __init__(self, comportamentos):
        """
        Método construtor da classe

        @param comportamentos: lista de comportamentos que constituem o
            comportamento composto
        """
        self._comportamentos = comportamentos

    def activar(self, percepcao):
        """
        Método que activa a reacção ao ambiente percepcionado, detectando
        os estímulos que o ambiente provoca aos vários comportamentos

        É percorrida a lista de comportamentos do comportamento composto e
        é obtida a acção correspondente à reacção à percepção do ambiente,
        caso sejam obtidas respostas aos estímulos - obtenção de uma acção
        a praticar pelo agente - é selecionada a acção a praticar através
        do método selecionar_accao.

        @param percepcao: estado atual do ambiente que rodeia o agente
        @returns: a acção a praticar por parte do agente
        """
        accoes = []

        for i in range(len(self._comportamentos)):
            accao = self._comportamentos[i].activar(percepcao)
            if accao is not None:
                accoes.append(accao)

        if accoes:
            if len(accoes) > 1:
                return self.seleccionar_accao(accoes)

            return accoes[0]

    @abstractmethod
    def seleccionar_accao(self, accoes):
        """
        Método abstrato que permite selecionar uma acção por entre as
        várias acções dos comportamentos do comportamento composto através
        de um sistema hierárquico ou através da prioridade que as acções
        apresentam

        @param accoes: lista das acções obtidas em função dos comportamentos
        """
