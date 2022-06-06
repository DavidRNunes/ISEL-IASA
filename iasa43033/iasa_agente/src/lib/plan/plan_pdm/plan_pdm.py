from pdm import PDM

from ..planeador import Planeador
from .modelo_pdm_plan import ModeloPDMPlan


class PlanPDM(Planeador):
    """
    Classe que implementa um planeador automático com base em PDM

    Esta classe permite delinear um plano para o estado actual do agente sob
    forma de processos de decisão de Markov. Através do modelo do mundo actual
    são obtidos os dicionários do valor da utilidade de cada estado no mundo
    e a política de cada estado, permitindo ao agente deslocar-se no mundo até
    que este sofra uma alteração. Como tratamos de um mundo determinista o que
    se passa efectivamente é que é definido um caminho óptimo entre o agente e
    o objetivo mais próximo, com a política a indicar-nos a acção que o agente
    deveria efectuar caso ele sofresse um desvio - que não acontece num ambiente
    determinista.

    @method planear: obtém os dicionários da utilidade e política para o modelo
        do mundo actual
    @method obter_accao: caso o plano seja válido retorna a política para o
        estado actual do agente
    @method plano_valido: verifica a validade do plano para a política definida
    @method terminar_plano: termina o plano actual definindo os dicionários da
        utilidade e política para None
    @method mostrar: permite visualizar a utilidade e a política na janela
    """

    _gama: float
    _delta_max: int
    _utilidade: None
    _politica: None

    def __init__(self):
        """
        Método construtor da classe

        O gama definido afecta a política e a utilidade em função da
        profundidade de procura, uma vez que o gama se traduz no factor
        de desconto no tempo: para gamas baixos (por exemplo 0.1) o valor
        de desconto torna-se muito elevado rapidamente, levando a que o
        sistema se torne reactivo uma vez que não tem em conta o futuro,
        mas para gamas insuficientemente altos (por exemplo 0.7) o sistema
        ainda assim pode não conseguir atingir os objetivos caso a utilidade
        da acção calculada se torne inferior ao delta máximo (correspondente
        à recompensa mínima) - nesta situação a deslocação por parte do
        agente torna a não ser devidamente recompensada, levando-o a preferir
        ficar imobilizado, por exemplo. O valor definido ainda assim pode
        não ser o suficiente para todos os cenários, mas tem de se ter em
        conta o tempo de execução do algoritmo, uma vez que quão mais perto
        de 1 se encontra o gama mais próximo de infinitas iterações serão
        necessárias para obter a utilidade de cada estado.
        """
        self._gama = 0.9
        self._delta_max = 1
        self._utilidade = None
        self._politica = None

    def planear(self, modelo_plan, objetivos):
        """
        Método que recebe o modelo do mundo e lhe aplica um modelo de processos
        de decisão de Markov por meio da classe ModeloPDMPlan, obtendo a representação
        do mundo sob a forma de PDM, fornecendo essa representação à classe PDM
        de forma a obter a utilidade e política para o mundo actual

        Através do método resolver da classe PDM obtemos os dicionários de política
        e utilidade para cada estado do mundo actual

        @param modelo_plan: modelo de planeamento correspondente ao estado modelo
            do mundo actual
        @param objetivos: lista de objetivos que se pretendem atingir no mundo
        """
        modelo_pdm = ModeloPDMPlan(modelo_plan, objetivos)
        pdm = PDM(modelo_pdm, self._gama, self._delta_max)
        self._utilidade, self._politica = pdm.resolver()


    def obter_accao(self, estado):
        """
        Método que utiliza o método plano_valido para verificar a validade do plano
        actual para o estado fornecido, e caso este seja válido retorna a política
        para esse estado

        @param estado: actual do agente
        @returns:
        """
        if self.plano_valido(estado):
            return self._politica[estado]

    def plano_valido(self, estado):
        """
        Método que verifica a validade do plano, verificando se existe uma política
        definida para o estado actual do mundo e de seguida verificando também se o
        estado fornecido faz parte do dicionário da política definida

        @param estado: estado actual do agente
        @returns: valor booleano da condição definida
        """
        return self._politica and estado in self._politica

    def terminar_plano(self):
        """
        Método que termina o plano actual, efectivamente definindo a utilidade e a
        politica a None de forma a serem novamente obtidas através de um novo plano
        """
        self._utilidade = None
        self._politica = None

    def mostrar(self, vista):
        """
        Método que permite mostrar a solução na janela de visualização
        """
        vista.mostrar_valor(self._utilidade)
        vista.mostrar_politica(self._politica)
