from mod import Problema

from ..ligacao import Ligacao
from .estado_localidade import EstadoLocalidade
from .operador_ligacao import OperadorLigacao


class ProblemaPlanTraj(Problema):
    """
    Classe que implementa a classe abstrata de um Problema, definindo o
    problema de planeador de trajetos entre localidades, que consiste na
    tentativa, através das ligações entre as localidades, chegar ao destino
    pretendido em função do método de procura definido na classe PlaneadorTrajeto

    @param ligacoes: lista das ligações entre estados
    @param loc_inicial: localidade inicial, em string
    @param loc_final: localidade final (objetivo), em string

    @method objectivo: verifica se o estado fornecido é o objetivo do problema
    """

    _estado_final: EstadoLocalidade

    def __init__(self, ligacoes, loc_inicial, loc_final):
        """
        Método construtor da classe, guarda o estado inicial do agente e
        o estado final correspondente ao objetivo e as ligações entre os
        vários estados recorrendo à classe OperadorLigacao

        @param ligacoes: lista das ligações entre os vários estados do problema
        @param loc_inicial: localidade inicial onde se encontra o agente
        @param loc_final: localidade objetivo que se pretende que o agente atinja
        """
        self._estado_inicial = EstadoLocalidade(loc_inicial)
        self._estado_final = EstadoLocalidade(loc_final)
        self._operadores = []
        for ligacao in ligacoes:
            self._operadores.append(OperadorLigacao(
                ligacao.origem, ligacao.destino, ligacao.custo))

        super().__init__(self._estado_inicial, self._operadores)

    def objectivo(self, estado):
        """
        Método que permite veirficar se o estado fornecido é um objetivo
        do problema planeador de trajetos

        @param estado: estado que se pretende verificar
        @returns: True se for um objetivo do problema, ou False em caso
            contrário
        """
        return estado.__eq__(self._estado_final)
