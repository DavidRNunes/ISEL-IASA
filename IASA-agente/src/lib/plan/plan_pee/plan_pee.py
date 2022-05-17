from pee.solucao import Solucao
from plan.plan_pee.heur_dist import HeurDist
from plan.plan_pee.problema_plan import ProblemaPlan
from plan.planeador import Planeador
from pee.mec_proc.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.mec_proc.melhor_prim.procura_aa import ProcuraAA
from pee.mec_proc.melhor_prim.procura_sofrega import ProcuraSofrega


class PlanPEE(Planeador):
    """
    
    """

    _solucao: Solucao

    def __init__(self):
        """
        
        """
        self._solucao = None
        self._mec_pee = ProcuraCustoUnif() # Alterar posteriormente para procura informada

    def planear(self, modelo_plan, objetivos):
        """
        
        """
        estado_final = objetivos.pop(0)
        problema = ProblemaPlan(modelo_plan, estado_final)
        heuristica = HeurDist(estado_final)
        self._solucao = self._mec_pee.resolver(problema)
        print(self._solucao.dimensao)

        return self._solucao
    
    def obter_accao(self, estado):
        """
        
        """
        passo = self._solucao.remover_passo()
        if passo.estado == estado:
            return passo.operador

    def plano_valido(self, estado):
        """
        
        """
        if self._solucao:
            return self._solucao[0] == estado

    def terminar_plano(self):
        """
        
        """
        self._solucao = None

    def mostrar(self, vista):
        """
        
        """
        vista.mostrar_solucao(self._solucao)