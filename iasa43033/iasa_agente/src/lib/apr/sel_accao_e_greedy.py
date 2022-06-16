from random import choice, random, shuffle

from .sel_accao import SelAccao


class SelAccaoEGreedy(SelAccao):
    """
    Classe que implementa a interface SelAccao criando uma estratégia de
    selecção de acção com uma estratégia e-greedy

    A estratégia e-greedy consiste numa estratégia de selecionar uma acção
    em função de uma probabilidade obtida em função a epsilon. Esta estratégia
    leva a que a acção praticada pelo agente seja escolhida aleatóriamente entre
    uma acção sôfrega, onde a acção escolhida é a que maximiza o reforço para
    o estado actual do agente, e uma acção aleatória que permita ao agente
    deslocar-se independentemente do reforço de forma a explorar o ambiente
    que o rodeia. Para um valor de epsilon baixo o agente é menos explorativo
    executando acções sôfregas a maioria do tempo, já para um valor de epsilon
    alto o agente torna-se muito explorativo mas obtém pouco aproveitamento das
    acções que efectua

    @param mem_aprend: memória do algoritmo de aprendizagem
    @param accoes: lista das acções possíveis
    @param epsilon: factor explorativo do agente

    @method seleccionar_accao: seleciona aleatóriamente uma acção em função
        do epsilon, podendo esta ser sôfrega ou explorativa
    @method accao_sofrega: obtém a acção que maximiza a recompensa
    @method explorar: obtém uma acção aleatória por entre a lista de acções
    """

    _epsilon: float
    """ Epsilon representa a taxa explorativa do agente, para valores altos
        o agente é muito explorativo, para valores baixos é sôfrego, valor
        em double no intervalo [0, 1] """

    def __init__(self, mem_aprend, accoes, epsilon):
        """
        Método construtor da classe

        @param mem_aprend: mémoria utilizada pelo algoritmo para guardar o que
            aprendeu sobre o mundo (acção a praticar num dado local)
        @param accoes: lista das acções possíveis a executar pelo agente
        @param epsilon: factor explorativo do agente
        """
        self._mem_aprend = mem_aprend
        self._accoes = accoes
        self._epsilon = epsilon

    def seleccionar_accao(self, s):
        """
        Método que implementa o método da superclasse, permitindo selecionar
        aleatóriamente a acção a executar pelo agente em função do epsilon

        Fazendo uso da biblioteca random obtemos um número entre 0 e 1 e
        caso este seja maior que epsilon é executada uma acção sôfrega,
        caso contrário é executada uma acção explorativa - aleatória

        @param s: estado actual do agente no mundo
        @returns: acção a executar pelo agente
        """
        if random() > self._epsilon:
            accao = self.accao_sofrega(s)
        else:
            accao = self.explorar()

        return accao

    def accao_sofrega(self, s):
        """
        Método que percorre as acções possíveis para a posição actual do
        agente e obtém aquela que maximiza o valor da função Q(s, a)

        É feito um baralhamento da ordem das acções de forma a evitar que
        no início da execução do algoritmo (quando não existe ainda
        memória de estados anteriores) seja retornada sempre a mesma
        acção, correspondente à acção na primeira entrada da lista

        @param s: estado actual do agente
        @returns: acção maximizante do valor da função Q(s, a)
        """
        shuffle(self._accoes)
        return max(self._accoes, key=lambda a: self._mem_aprend.q(s, a))

    def explorar(self):
        """
        Método que por entre a lista de acções possíveis escolhe uma
        aleatóriamente, permitindo ao agente explorar o mundo através
        das suas acções aleatórias

        @returns: acção a praticar pelo agente, escolhida aleatóriamente
        """
        return choice(self._accoes)
