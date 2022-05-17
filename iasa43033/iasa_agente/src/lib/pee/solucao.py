from ast import Pass
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
    @method __iter__: método que cria um iterador para o objecto Solução,
        permitindo iterar pela lista de nós da solução
    @method __getitem__: método que permite indexar o objeto Solução,
        permitindo assim obter um nó presente na lista através de uma key
    """

    _dimensao = 0
    """ Dimensão da solução (int) """
    _custo = 0.0
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
        solução obtida. O custo e a dimensão da solução estão associados aos
        passos dados na solução, nomeadamente ao custo das operações e ao número
        de passos totais, respetivamente

        @param no_final: nó final a partir do qual se obtém os seus antecessores
            até chegar ao nó inicial, formando assim o percurso da solução
        """
        self._percurso = []
        no = no_final
        while no:
            self._percurso.insert(0, no)
            no = no.antecessor
        self._dimensao = len(self._percurso)
        """
        self._no = no_final
        passo = PassoSolucao(self._no.estado, self._no.operador)
        self._percurso.append(passo)
        self._custo = no_final.custo
        while self._no.antecessor:
            passo = PassoSolucao(self._no.antecessor.estado, self._no.antecessor.operador)
            self._percurso.append(passo)
            self._no = self._no.antecessor
            self._custo += self._no.custo
        """
        

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
        if self._dimensao > 1:
            estado = self._percurso[0].estado
            operador = self._percurso[1].operador
            self._percurso.pop(0)
            return PassoSolucao(estado, operador)

    def __iter__(self):
        """
        Método iterativo do Python que permite percorrer o objecto, retornando o
        próprio objecto, que pode ser iterado

        Neste caso se pretendermos iterar ao longo do objecto solução este este
        método implementa o iterador que nos permite percorrer a lista dos nós que
        compõem o percurso
        
        @returns: iterador de nós do percurso
        """
        return iter(self._percurso)
    
    def __getitem__(self, key):
        """
        Método que altera a forma como o Python interpreta a indexação do objeto
        solução, permitindo obter o nó presente no percurso da solução com a chave
        fornecida

        Este método permite obter um nó presente na lista do percurso através da
        indexação da key, mas para o objeto Solução, ou seja, é possível obter um
        determinado nó através da sintaxe solucao[key]
        
        @returns: nó presente na lista do percurso com key fornecida
        """
        return self._percurso[key]