from .modelo_pdm import ModeloPDM


class PDM():
    """
    Classe que define um processo de decisão de Markov

    Um processo de decisão de Markov representa a previsão dos
    estados seguintes dependendo apenas do estado actual do agente
    no mundo. O agente encontra-se inserido numa política comportamental
    não determinista, onde a acção que deve ser realizada em cada
    estado sofre influência de uma probabilidade de a mesma ser
    executada, pelo que a solução óptima é obtida iterando pela
    utilidade de cada estado, por exemplo, uma dada acção que aparente
    ser boa no imediato pode levar a um aumento da probabilidade
    de insucesso mais à frente nos estados. O cálculo da utilidade
    do estado permite obter o melhor caminho a tomar em função do
    sucesso dos estados ao longo do tempo

    @param modelo:
    @param gama:
    @param delta_max:

    @method utilidade:
    @method util_accao:
    @method politica:
    @method resolver:
    """

    _gama: float
    _delta_max: int

    def __init__(self, modelo, gama, delta_max):
        """
        Método construtor da classe

        @param modelo: modelo do processo de decisão de Markov
        @param gama: factor de desconto no tempo
        @param delta_max: valor da recompensa mínima
        """
        self._modelo = modelo
        self._gama = gama
        self._delta_max = delta_max

    def utilidade(self):
        """
        Método de cálculo da utilidade de estado para a política óptima

        Através deste estado iniciamos a utilidade de um estado a zero e de
        seguida iteramos para cada estado s presente na lista de estados S,
        de forma a obter a utilidade de cada acção do conjunto de acções
        possíveis. Esta iteração é feita até ser atingido o limiar de
        convergência - enquanto a diferença máxima de actualização é no máximo
        igual ao valor do delta máximo correspondente à recompensa mínima

        @returns: valor da utilidade de estado para a política óptima
        """
        S = self._modelo.S
        A = self._modelo.A
        U = {s: 0 for s in S()}

        while True:
            Uant = U.copy()
            delta = 0
            for s in S():
                U[s] = max([self.util_accao(s, a, Uant) for a in A(s)], default=0)
                delta = max(delta, abs(U[s] - Uant[s]))
            if delta <= self._delta_max:
                break

        return U
        

    def util_accao(self, s, a, U):
        """
        Método de suporte ao cálculo da utilidade de estado para a política
        óptima, obtendo a utilidade de uma acção por meio de um somatório

        O método realiza o somatório da probabilidade de transição de estado
        multiplicada pela recompensa esperada na transição de s para sn por
        meio de a somada à gama multiplicada pela utilidade do estado seguinte
        para cada probabilidade de transição de s por meio de a - somatório
        presente nos slides da disciplina (pg. 16) apresentado da seguinte
        forma: sum(T(s,a,s')[R(s,a,s')+ gama*U(s')])

        @param s: estado actual do modelo do mundo
        @param a: acção que permite a transição para o estado seguinte
        @param U: dicionário da utilidade do estado anterior
        @returns: valor do somatório calculado
        """
        T = self._modelo.T
        R = self._modelo.R
        gama = self._gama

        return sum(p * (R(s, a, sn) + gama * U(sn)) for p, sn in T(s, a))

    def politica(self, U):
        """
        Método que obtém o dicionário da política óptima para os estados do
        mundo

        Através do método util_accao é obtido o argumento máximo do somátorio
        fornecido pelo método auxiliar, obtendo-se a política para cada estado
        presente no espaço de estados

        @param U: dicionário do valor da utilidade para cada estado
        @returns: dicionário da política de estados, correspondente à estratégia
            de acção para cada estado
        """
        S = self._modelo.S
        A = self._modelo.A

        pol = {}
        for s in S():
            pol[s] = max(A(s), key=lambda a:self.util_accao(s, a, U))

        return pol

    def resolver(self):
        """
        Método que resolve o processo de decisão de Markov, obtendo um
        tuplo com o dicionário do valor da utilidade para cada estado do
        espaço de estados e a estratégia de acção para cada um desses
        estados

        @returns: tuplo com o dicionário da utilidade de cada estado e
            dicionário com a política para cada estado
        """
        U = self.utilidade()
        pol = self.politica(U)

        return U, pol