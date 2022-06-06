from pdm import ModeloPDM

from ..modelo_plan import ModeloPlan


class ModeloPDMPlan(ModeloPlan, ModeloPDM):
    """
    Classe que permite obter a representação do mundo actual sob forma de
    um processo de decisões de Markov

    Através desta classe são definidos os objetivos e o modelo actual do
    mundo sobre o qual se irá obter a política e utilidade recorrendo às
    funções S, A, T e R que permitem representar o mundo sob a forma de PDM.

    @param modelo_plan: modelo de planeamento, correspondente ao modelo
        actual do mundo
    @param objetivos: lista de objetivos que se pretende atingir

    @method estado: obtém o estado actual do mundo através do modelo de planeamento
    @method estados: obtém a lista de estados possíveis do agente através
        do modelo de planeamento
    @method operadores: obtém a lista de operadores válidos através do
        modelo de planeamento
    @method S: obtém o conjunto de estados do mundo na representação de PDM
    @method A: obtém o conjunto de acções que o agente pode realizar na
        representação de PDM
    @method T: obtém o tuplo do valor da probabilidade de transição do
        estado s para um estado s' correspondente ao estado obtido por
        aplicação da acção a
    @method R: obtém o valor do retorno para a transição do estado s para um
        estado s' por meio de uma acção a
    """

    _rmax: int
    _objetivos: None
    _modelo_plan: None

    def __init__(self, modelo_plan, objetivos):
        """
        Método construtor da classe
        """
        self._rmax = 1000
        self._modelo_plan = modelo_plan
        self._objetivos = objetivos

    def estado(self):
        """
        Método que retorna o estado atual do agente, delegando para
        o método definido no modelo de planeamento (ModeloMundo)

        @returns: estado actual do agente
        """
        return self._modelo_plan.estado()

    def estados(self):
        """
        Método que retorna a lista de estados possíveis do mundo,
        obtido através do método definido no modelo de planeamento

        @returns: lista de estados possíveis no mundo
        """
        return self._modelo_plan.estados()

    def operadores(self):
        """
        Método que retorna a lista de operadores do mundo através
        do método definido no modelo de planeamento

        @returns: lista de operadores válidos
        """
        return self._modelo_plan.operadores()

    def S(self):
        """
        Método que implementa o método da classe ModeloPDM permitindo
        obter o conjunto de estados do mundo

        @returns: lista de estados do mundo
        """
        return self.estados()

    def A(self, s):
        """
        Método que implementa o método da classe ModeloPDM permitindo
        obter o conjunto de acções que o agente pode realizar

        Caso o agente se encontre num estado final - objetivo - o agente
        não se deve deslocar novamente uma vez que atingiu o objetivo e
        deve ser delineado novo processo de decisão de Markov para o próximo
        objetivo

        @param s: estado actual do agente no mundo
        @returns: lista de operadores válidos caso o estado actual não
            seja um objetivo, retornando uma lista vazia nesse caso
        """
        if s in self._objetivos:
            return []
        else:
            return self.operadores()

    def T(self, s, a):
        """
        Método que implementa o método da classe ModeloPDM obtendo-se
        o valor da probabilidade de transição do estado s para um estado
        s' correspondente ao estado obtido por aplicação da acção a

        Como o ambiente do mundo definido se trata de um ambiente determinista
        este método apenas retorna um tuplo com o estado seguinte após a
        aplicação da acção a e a probabilidade de 1.0, equivalente à
        probabilidade certa. Caso o nosso mundo não fosse determinista a
        lista retornada pelo método teria mais entradas paras as possíveis
        transições tendo a probabilidade associada a estas

        @param s: estado actual do agente no mundo
        @param a: acção a aplicar ao agente
        @returns: lista de estados possíveis após aplicação da acção a
            bem como a probabilidade de transição para esse estado
            sob formato de um tuplo (probabilidade, estado seguinte)
        """
        sn = a.aplicar(s)
        if sn:
            return [(1.0, sn)]
        else:
            return []

    def R(self, s, a, sn):
        """
        Método que implementa o método da classe ModeloPDM que permite
        obter o retorno esperado para cada transição de um estado s para
        um estado seguinte s' através da acção a, em função do custo da
        transição

        Caso o estado final seja um objetivo o retorno esperado equivale
        ao retorno máximo, pelo que a este deve ser subtraído o retorno
        correspondente ao custo de transição

        @param s: estado actual do agente no mundo
        @param a: acção a aplicar ao agente
        @param sn: estado seguinte após aplicação da acção a
        @returns: valor do retorno esperado
        """
        r = a.custo(s, sn)
        if sn in self._objetivos:
            return self._rmax - r
        else:
            return -r
