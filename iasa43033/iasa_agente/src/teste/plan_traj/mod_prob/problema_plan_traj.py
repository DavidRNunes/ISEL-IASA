from mod.problema.problema import Problema
from teste.plan_traj.mod_prob.estado_localidade import EstadoLocalidade
from teste.plan_traj.mod_prob.operador_ligacao import OperadorLigacao


class ProblemaPlanTraj(Problema):

    _estado_final: EstadoLocalidade

    def __init__(self, ligacoes, loc_inicial, loc_final):
        """
        
        """
        self._estado_inicial = EstadoLocalidade(loc_inicial)
        self._estado_final = EstadoLocalidade(loc_final)
        self._operadores = []
        for ligacao in ligacoes:
            self._operadores.append(OperadorLigacao(ligacao.origem, ligacao.destino, ligacao.custo))
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