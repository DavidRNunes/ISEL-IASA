from pee.solucao import Solucao
from teste.plan_traj.mod_prob.problema_plan_traj import ProblemaPlanTraj
from pee.mec_proc.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.mec_proc.prof.procura_prof import ProcuraProf
from pee.mec_proc.prof.procura_prof_lim import ProcuraProfLim
from pee.mec_proc.prof.procura_prof_iter import ProcuraProfIter
from pee.mec_proc.larg.procura_larg import ProcuraLarg


class PlaneadorTrajeto():
    
    def planear(self, ligacoes, loc_inicial, loc_final):
        """
        
        """
        problema = ProblemaPlanTraj(ligacoes, loc_inicial, loc_final)
        mecanismo = ProcuraCustoUnif()
        solucao = mecanismo.resolver(problema)

        return solucao

    def mostrar_trajecto(self, solucao):
        """
        
        """
        for x in range(solucao.dimensao):
            passo = solucao.remover_passo()
            print(passo.estado.localidade)