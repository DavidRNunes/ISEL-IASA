from abc import ABC, abstractmethod


class Problema(ABC):
    """
    Classe abstrata representativa de um problema

    Um problema consiste no estado inicial em que se encontra o agente,
    os operadores (acções que geram a transformação do estado) e os
    objetivos (um ou mais) que se pretende que o agente atinja. Para um
    problema é ainda relevante o custo das acções que o agente executa
    uma vez que a solução óptima será a sequência de acções que forma um
    caminho com menor custo até ao objetivo final

    @param estado_inicial: estado em que o agente se encontra no início
        do problema
    @param operadores: lista de acções que o agente pode executar para
        alterar o seu estado
    
    @method objetivo: método abstrato que permite saber se um estado em
        estudo é um objetivo do problema
    """

    def __init__(self, estado_inicial, operadores):
        """
        Método construtor da classe Problema que guarda os atributos em
        variáveis locais

        @param estado_inicial: estado inicial do agente
        @param operadores: lista de acções que o agente pode executar
        """
        self._estado_inicial = estado_inicial
        self._operadores = operadores

    @property
    def operadores(self):
        """
        Propriedade que permite obter os operadores constituintes do
        problema
        """
        return self._operadores

    @property
    def estado_inicial(self):
        """
        Propriedade que permite obter o estado inicial do problema
        """
        return self._estado_inicial

    @abstractmethod
    def objectivo(self, estado):
        """
        Método abstrato que permite identificar se um estado fornecido
        é um objetivo deste problema
        
        @param estado: estado em teste
        @returns: valor booleano que permite saber se o estado em estudo
            é um objetivo deste problema
        """