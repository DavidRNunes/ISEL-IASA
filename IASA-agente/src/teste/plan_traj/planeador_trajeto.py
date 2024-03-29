from pee import (ProcuraCustoUnif, ProcuraLarg, ProcuraProf, ProcuraProfIter,
                 ProcuraProfLim, Solucao)

from .mod_prob.problema_plan_traj import ProblemaPlanTraj


class PlaneadorTrajeto():
    """
    Classe de aplicação de testes às classes criadas

    Permite planear um trajeto entre duas localidades, ou seja, definir
    um problema que consiste na intenção de deslocação entre duas localidades
    por meio de ligações entre as várias localidades que compõem o problema.
    Este planeador utiliza um dos mecanismos previamente definidos, podendo
    utilizar qualquer um deles, servindo assim de teste à implementação dos
    mecanismos de procura

    @param ligacoes: lista das ligações entre as localidades
    @param loc_inicial: localidade inicial do agente, em string
    @param loc_final: localidade final (objetivo) do problema, em string

    @method planear: constrói o problema e define o mecanismo de procura
    @method mostrar_trajeto: imprime para a consola o trajeto da solução
    """

    def planear(self, ligacoes, loc_inicial, loc_final):
        """
        Método que constrói o problema e define qual o mecanismo de procura
        a ser utilizado para resolver esse mesmo problema

        Ao alterar o mecanismo a utilizar neste método é possível testar e
        obter diferentes soluções para o mesmo problema

        @param ligacoes: lista de ligações entre localidades e o seu custo
        @param loc_inicial: localidade inicial em que se encontra o agente
        @param loc_final: localidade que se pretende que o agente atinja

        @returns: solução do problema caso encontre uma        
        """
        problema = ProblemaPlanTraj(ligacoes, loc_inicial, loc_final)
        mecanismo = ProcuraCustoUnif()
        solucao = mecanismo.resolver(problema)

        return solucao

    def mostrar_trajecto(self, solucao):
        """
        Método que permite obter o trajeto da solução imprimindo os passos
        dados desde a localidade inicial até à localidade final para a consola,
        caso haja uma solução

        @param solucao: a solução do problema
        """
        if solucao:
            while solucao.dimensao > 1:
                passo = solucao.remover_passo()
                print(passo.estado.localidade)
            no_final = solucao[0]
            print(no_final.estado.localidade)
        else:
            print("Não foi encontrada uma solução.")
