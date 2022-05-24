from pee import ProcuraAA, ProcuraCustoUnif, ProcuraSofrega, Solucao

from ..planeador import Planeador
from .heur_dist import HeurDist
from .problema_plan import ProblemaPlan


class PlanPEE(Planeador):
    """
    Classe que implementa a interface do planeador para implementar um
    planeador de procura em espaço de estados

    O planeador de procura em espaço de estados permite obter um plano de
    acção para o agente atingir todos os objetivos presentes no ambiente,
    apresentando uma solução que permita ao agente atingir o próximo
    objetivo. É definido um problema recorrendo ao modelo actual do mundo
    e ao próximo objetivo que se pretende atingir, a solução obtida
    permite a deslocação do agente pelo ambiente recorrendo aos mecanismos
    de procura em espaço de estados, nomeadamente a procura A* ou sôfrega
    no caso de uma procura heurística ou a procura de custo uniforme por
    exemplo

    @method planear: obtém a solução para o problema actual do mundo
    @method obter_accao: obtém o operador do próximo passo da solução
    @method plano_valido: verifica a validade do plano para o estado actual
        do agente
    @method terminar_plano: termina o plano actual, eliminando a solução
    @method mostrar: mostra a solução na janela de visualização
    """

    _solucao: Solucao
    """ Variável que guarda a solução para o problema definido atualmente """

    def __init__(self):
        """
        Método construtor da classe do planeador PEE, inicia a solução e o
        mecanismo de procura a None
        """
        self._solucao = None
        self._mec_pee = None

    def planear(self, modelo_plan, objetivos):
        """
        Método que recorre aos objetivos definidos para o modelo do mundo actual
        e obtém uma solução em função do mecanismo de procura em espaço de estados
        definido, caso uma exista

        Caso existam objetivos a atingir o método planear formula um problema do
        planeador em função do objetivo selecionado e do estado actual do mundo,
        recorre depois ao mecanismo de procura definido para resolver o problema
        e obter uma solução que é então retornada pelo método, caso esta exista

        @param modelo_plan: modelo de planeamento correspondente ao modelo do
            mundo actual
        @param objetivos: lista de objetivos que se pretende atingir
        @returns: solução para o problema definido, caso uma exista
        """
        if objetivos:
            estado_final = objetivos.pop(0)
            problema = ProblemaPlan(modelo_plan, estado_final)
            self._mec_pee = ProcuraAA()
            heuristica = HeurDist(estado_final)
            self._solucao = self._mec_pee.resolver(problema, heuristica)
            print("Custo: %s" % self._solucao.custo)

            return self._solucao

    def obter_accao(self, estado):
        """
        Método que permite obter o operador do próximo passo da solução,
        caso uma exista

        No caso de existir uma solução, é obtido o próximo passo da mesma
        e retornado o operador que permite atingir o próximo estado do
        agente no ambiente após executar a acção presente nesse operador

        @param estado: estado actual do agente no ambiente
        @returns: operador que permite alterar o estado do agente para
            o próximo estado da solução, efetivamente aplicando um passo
            da solução actual
        """
        if self._solucao:
            passo = self._solucao.remover_passo()
            if passo.estado == estado:
                return passo.operador

    def plano_valido(self, estado):
        """
        Método que verifica a validade do plano verificando se o agente se
        encontra no estado correspondente ao estado inicial da solução, ou
        seja, é verificada a validade do plano em função do estado actual
        do agente, se este se encontra em posição para executar a solução
        encontrada o plano é considerado válido

        @param estado: estado actual em que o agente se encontra
        @returns: True caso o agente se encontre em posição de realizar a
            solução encontrada, False em caso contrário
        """
        if self._solucao:
            return self._solucao[0].estado == estado

    def terminar_plano(self):
        """
        Método que termina o plano actual, removendo a solução actual uma
        vez que o plano terminou, seja por ter sido atingido o objetivo,
        seja por necessidade de reavaliar o plano actual
        """
        self._solucao = None

    def mostrar(self, vista):
        """
        Método que permite mostrar a solução na janela de visualização
        """
        vista.mostrar_solucao(self._solucao)
