from .aprend_ref import AprendRef


class AprendQ(AprendRef):
    """
    Classe que implementa a classe abstrata AprendRef implementando assim
    um método de aprendizagem, neste caso, recorrendo a um algoritmo de
    Q-Learning

    Este método implementa o algoritmo Q-Learning fornecido nos slides da
    disciplina (p.22), que consiste em executar uma acção com base numa
    política de selecção de acção (neste caso sôfrega) e observar o estado
    seguinte e o reforço obtido. Para o estado actual onde se executou a
    acção é então obtido o valor de efectuar essa acção em função da
    expressão Q(s,a) + alfa * (reforço + gama * max_a'Q(s', a') - Q(s,a)).
    Este valor é então memorizado permitindo assim que o agente aprenda
    as características do mundo que o rodeia

    @param mem_aprend: tipo de memória utiizado pelo agente
    @param sel_accao: política de selecção de acção
    @param alfa: factor de aprendizagem
    @param gama: 

    @method aprender: método que permite ao agente aprender sobre o mundo
    """

    _alfa: float
    """ Factor de aprendizagem """
    _gama: float
    """ Gama é... """

    def __init__(self, mem_aprend, sel_accao, alfa, gama):
        """
        Método construtor da classe

        @param mem_aprend: tipo de memória do agente
        @param sel_accao: política de selecção de acção
        @param alfa: factor de aprendizagem
        @param gama:
        """
        self._alfa = alfa
        self._gama = gama
        super().__init__(mem_aprend, sel_accao)

    def aprender(self, s, a, r, sn):
        """
        Método que implementa o algoritmo Q-Learning levando à aprendizagem
        do agente

        É implementado o algoritmo dos slides da cadeira, obtendo o valor
        de execução da acção a para o estado s através da expressão
        Q(s,a) + alfa * (reforço + gama * max_a'Q(s', a') - Q(s,a)), sendo
        depois este valor enviado para memória através do método actualizar
        da memória de aprendizagem do agente

        @param s: estado actual observado pelo agente
        @param a: acção efectuada
        @param r: reforço obtido pelo agente para a acção efectuada
        @param sn: estado seguinte após efectuar a acção
        """
        an = self._sel_accao.accao_sofrega(sn)
        qsa = self._mem_aprend.q(s, a)
        qsnan = self._mem_aprend.q(sn, an)
        q = qsa + self._alfa * (r + self._gama*qsnan - qsa)
        self._mem_aprend.actualizar(s, a, q)
