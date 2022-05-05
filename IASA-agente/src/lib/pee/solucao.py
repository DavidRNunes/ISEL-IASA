from pee.passo_solucao import PassoSolucao


class Solucao():
    """
    Classe que reprsenta a solução de um problema

    A solução de um problema consiste nos passos que o agente tem
    de executar para chegar até ao estado pretendido, sendo que
    esses passos consistem no estado e operador que lhe permite
    atingir o próximo estado. Desta forma a classe cria uma lista
    de passos de solução, onde a ordem é iniciada no nó com o estado
    antecessor do estado final e com o operador que permite ao agente
    chegar ao estado final da solução seguida dos nós cujos estados
    e operadores permitem chegar ao seu sucessor, sendo a última
    entrada o nó inicial com o operador que permite chegar à
    solução

    @param no_final: nó que se pretende obter o caminho da solução

    @method remover_passo: método que obtém o próximo passo da solução
    @method __iter__:
    @method __getitem__:
    """

    _dimensao: int
    """ Dimensão da solução (int) """
    custo: float
    """ Custo da solução (double) """
    _percurso: list
    """ Lista de nós que compõem a solução """

    def __init__(self, no_final):
        """
        Método construtor da classe solução

        É criada a lista de passos da solução, correspondentes aos estados
        e operadores desde a solução até à raiz, ou seja, o primeiro elemento
        da lista é o estado e o operador que permite obter a solução, o segundo
        elemento é o estado e operador que peritem obter o primeiro elemento,
        e assim sucessivamente até se chegar ao último elemento da lista que
        é o estado inicial com o operador que permite iniciar o caminho da
        solução obtida

        @param no_final: nó final a partir do qual se obtém os seus antecessores
            até chegar ao nó inicial, formando assim o percurso da solução
        """
        self._percurso = []
        self._no = no_final
        passo = PassoSolucao(self._no.estado, self._no.operador)
        self._percurso.append(passo)
        while self._no.antecessor:
            passo = PassoSolucao(self._no.antecessor.estado, self._no.antecessor.operador)
            self._percurso.append(passo)
            self._no = self._no.antecessor
        self._dimensao = len(self._percurso)

    @property
    def dimensao(self):
        """
        Propriedade que permite obter a dimensão do percurso da solução
        """
        return self._dimensao

    @property
    def custo(self):
        """
        Propriedade que permite obter o custo da solução
        """
        return self.custo

    def remover_passo(self):
        """
        Método que obtém o próximo passo da solução, caso um exista

        Remove o último elemento, correspondente ao primeiro passo a dar
        partindo do estado inicial e de seguida remove os passos seguintes
        até ao último passo que nos permite ficar no estado final correspondente
        à solução do problema

        @returns: um passo da solução caso um exista, None caso já não
            haja mais passos a dar
        """
        if self._percurso:
            return self._percurso.pop()
        else:
            return None

    def __iter__(self):
        """
        
        @returns: iterador de nós
        """
        return iter(self._percurso)
    
    def __getitem__(self, key):
        """
        
        @returns: nó
        """
        return self._percurso[key]