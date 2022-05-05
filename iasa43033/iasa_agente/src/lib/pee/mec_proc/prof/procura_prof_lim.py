from pee.mec_proc.no import No
from pee.mec_proc.prof.procura_prof import ProcuraProf


class ProcuraProfLim(ProcuraProf):
    """
    Classe que implementa o mecanismo de procura em profundidade limitada

    O mecanismo de procura em profundidade limitada permite o uso do
    mecanismo de procura em profundidade sem que este vagueie sem rumo
    infinitamente. Ao chegar a uma certa profundidade definida os nós
    sucessores são tratados como se não tivessem sucessores eles prórprios,
    terminando a procura nesse caminho, mesmo que ainda não tenha sido
    encontrada uma solução, pelo que a profundidade escolhida deve ser obtida
    com algum cuidado relativo ao problema.
    
    @method resolver: implementa o algoritmo de resolução, guarda o valor da
        profundidade máxima que se pretende atingir de forma a limitar a
        expansão de novos nós quando a mesma é atingida
    @method _expandir: método que permite expandir a fronteira de exploração
        mediante as limitações de profundidade fornecidas
    """

    _prof_max: int

    def resolver(self, problema, prof_max = 1000):
        """
        Método que implementa o algoritmo de resolução
    
        Guarda o valor da profundidade máxima que se pretende atingir com a
        intenção de limitar a expansão de novos nós quando se atinge essa
        profundidade e chama a superclasse para usar a resolução base dos
        mecanismos de procura

        @param problema: estado inicial do agente, operadores e objetivos
        @param prof_max: profundidade máxima que se pretende atingir, default=1000
        @returns: solução do problema ou None caso não haja solução, recorrendo
            à superclasse
        """
        self._prof_max = prof_max
        return super().resolver(problema)

    def _expandir(self, problema, no):
        """
        Método que expande a fronteira de exploração tendo em conta a profundidade
        do nó actual, caso a profunidade seja superior à profundidade máxima dada
        no método resolver o nó não é mais expandido

        @param problema: estado inicial do agente, operadores e objetivos
        @param no: nó que se pretende expandir (nó em estudo)
        @returns: lista de nós filho do nó fornecido obtidos com recurso ao método
            da superclasse caso a profundidade seja menor que o máximo definido,
            retorna None caso contrário, não expandindo o nó
        """
        if no.profundidade <= self._prof_max:
            return super()._expandir(problema, no)
        else:
            return None