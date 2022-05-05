from pee.mec_proc.prof.procura_prof_lim import ProcuraProfLim


class ProcuraProfIter(ProcuraProfLim):
    """
    Classe que implementa o mecanismo de procura de profundidade iterativa

    Esta classe implementa o mecanismo de procura em profundidade iterativa
    permitindo evitar escolher uma profundidade máxima correcta para o
    problema, podendo ser dado um valor infinitamente alto. A classe percorre
    as profundidades dos nós do problema uma a uma até à profundidade fornecida
    retornando a solução caso a encontre ou None caso não exista solução e
    já não existam nós a expandir, ou seja, atingindo a profundidade máxima
    dos nós do problema

    @method resolver: implementa o algoritmo de resolução a profundidades
        progressivamente maiores até encontrar uma solução, ou caso não haja
        solução retornar None
    """

    def resolver(self, problema, inc_prof=1, prof_max=1000):
        """
        Método que recorre aos métodos das superclasses para iterar a uma
        profundidade variante crescente até encontrar uma solução para o
        problema

        @param problema: estado inicial do agente, operadores e objetivos
        @param inc_prof: incremento da profundidade, quantos níveis pretendemos
            incrementar a cada iteração
        @param prof_max: profundidade máxima que se pretende atingir, default=1000
        @returns: solução do problema ou None caso não haja solução, recorrendo
            às superclasses
        """
        for prof in range(0, prof_max, inc_prof):
            solucao = super().resolver(problema, prof)
            if solucao is not None:
                return solucao