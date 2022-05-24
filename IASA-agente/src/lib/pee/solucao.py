from .mec_proc.no import No
from .passo_solucao import PassoSolucao


class Solucao():
    """
    Classe que reprsenta a solução de um problema

    A solução de um problema consiste nos passos que o agente tem de executar para
    chegar até ao estado pretendido, sendo que esses passos consistem no estado e
    operador que lhe permite atingir o próximo estado. Desta forma a classe cria uma
    lista de nós, obtidos a partir do objetivo até ao nó actual do agente, sendo criada
    uma lista em que o primeiro nó é o nó actual e o nó seguinte é o nó cujo operador
    permite ao agente deslocar-se do nó actual para esse nó. Por último, a última entrada
    da lista corresponde ao nó final que é o objetivo pretendido - a solução do problema

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
    _percurso = None
    """ Lista de nós que compõem a solução """

    def __init__(self, no_final):
        """
        Método construtor da classe solução

        É criada a lista de nós que compõem a solução, correspondentes aos estados
        desde a solução até à raiz, ou seja, o primeiro elemento da lista, que é o
        estado actual do agente, o segundo elemento é o estado seguinte obtido através
        de um operador associado a esse nó, permitindo atingir o segundo elemento a
        partir do primeiro, e assim sucessivamente até se chegar ao último elemento
        da lista que é o objetivo pretendido. O custo e a dimensão da solução estão
        associados aos passos dados na solução, nomeadamente ao custo das operações
        e ao número de passos totais, respetivamente

        @param no_final: nó final a partir do qual se obtém os seus antecessores
            até chegar ao nó actual, formando assim o percurso da solução
        """
        self._percurso = []
        _no = no_final
        while _no:
            self._percurso.insert(0, _no)
            _no = _no.antecessor

    @property
    def dimensao(self):
        """
        Propriedade que permite obter a dimensão do percurso da solução em função
        da dimensão da lista do percurso
        """
        return len(self._percurso)

    @property
    def custo(self):
        """
        Propriedade que permite obter o custo da solução em função do custo do
        último nó (objetivo da solução) do percurso, retorna o custo desse nó
        ou 0 caso não exista um percurso definido, ou seja, caso não exista
        solução
        """
        return self._percurso[-1].custo if self._percurso else 0

    def remover_passo(self):
        """
        Método que obtém o próximo passo da solução, caso um exista

        Remove o próximo elemento da lista, correspondente ao nó corrente e a partir
        do nó seguinte obtém a operação que permite a deslocação do agente do nó actual
        para esse nó. A informação é então retornada no formato de um passo da solução,
        correspondente ao estado actual e o operador que permite ao agente deslocar-se
        para o próximo estado

        @returns: um passo da solução caso um exista, None caso já não
            haja mais passos a dar
        """
        if self.dimensao > 1:
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
