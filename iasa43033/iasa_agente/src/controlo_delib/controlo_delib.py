from controlo_delib.modelo_mundo import ModeloMundo
from sae import Controlo
from sae.ambiente.elemento import Elemento


class ControloDelib(Controlo):
    """
    Classe que implementa a classe abstrata Controlo implementando um
    controlo deliberado, ou seja, uma arquitectura deliberativa do agente

    A arquitectura deliberativa consiste num raciocínio por parte do
    agente sobre os fins e os meios, obtendo as opções que o agente dispõe
    obtendo dessa forma os seus objetivos e decidindo as acções a tomar,
    efectivamente planeando o seu curso de acção. Dado às limitações de
    recursos tanto de memória como de tempo de computação é necessário
    considerar que o ambiente que rodeia um agente pode alterar-se enquanto
    este delibra e planeia, pelo que é importante reconsiderar se o plano
    definido anteriormente ainda é válido para esta nova percepção mais
    recente do ambiente, completando assim a arquitectura deliberativa

    @param planeador: planeador do controlo

    @method processar: método que representa o processo de tomada de
        acção de um agente deliberativo
    @method _assimilar: actualiza o modelo do mundo, assimilando a
        percepção actual
    @method _reconsiderar: verifica se o modelo do mundo sofreu alterações,
        retornando True em caso afirmativo
    @method _deliberar: atualiza os objetivos para que estes se encontrem
        em conformidade com a nova percepção do mundo
    @method _planear: decide as acções a tomar de forma a atingir os objetivos
        pretendidos delineando um plano de execução
    @method _executar: executa a acção presente no operador do plano de
        execução delineado
    @method _mostrar: actualiza a vista do modelo
    """

    def __init__(self, planeador):
        """
        Método construtor da classe ControloDelib

        Inicia o planeador do controlo deliberado e o modelo do mundo,
        criando ainda a lista de objetivos do agente vazia
        """
        self._planeador = planeador
        self._objetivos = []
        self._modelo_mundo = ModeloMundo()
        super().__init__()

    def processar(self, percepcao):
        """
        Método que implementa as noções do controlo deliberativo em relação
        à escolha da acção a tomar por parte do agente

        Consiste em assimilar o mundo que o rodeia e verificar se o mesmo
        sofreu alterações desde a última vez que o agente o percepcionou,
        actualizando os seus objetivos em função das alterações em caso
        afirmativo, sendo posteriormente definido um novo plano de acção
        de forma a executar a acção que se adequa ao mundo
        
        @param percepcao: vista actual do mundo que rodeia o agente
            percepcionada pelo mesmo
        @returns: accção a ser executada pelo agente
        """
        self._assimilar(percepcao)
        if self._reconsiderar():
            self._deliberar()
            self._planear()
        return self._executar()

    def _assimilar(self, per):
        """
        Método que actualiza o modelo do mundo para assimilar a percepção
        actual por parte do agente, executando o método actualizar da
        classe ModeloMundo fornecendo a percepção actual

        @param per: a percepção actual do mundo
        """
        self._modelo_mundo.actualizar(per)

    def _reconsiderar(self):
        """
        Método que verifica se o modelo do mundo foi alterado sendo
        necessário re-avaliar a solução actual, ou seja, sendo necessário
        reconsiderar o que foi assimilado

        @returns: booleano correspondente à alteração do modelo do mundo
        """
        return self._modelo_mundo.alterado

    def _deliberar(self):
        """
        Método que actualiza os objetivos em função das alterações que
        ocorreram no mundo

        Percorre-se a lista de estados e obtém-se os estados que correspondem
        aos alvos, efectivamente obtendo a posição dos alvos - objetivo para
        onde o agente se deve deslocar
        """
        estados = self._modelo_mundo.estados()
        self._objetivos = [estado for estado in estados 
                            if self._modelo_mundo.obter_elem(estado) == Elemento.ALVO]

    def _planear(self):
        """
        Método que define o plano de execução de acções por parte do agente

        Se o mundo sofrer alterações o plano actual é terminado e é criado
        um novo plano, tal também acontece caso todos os objetivos tenham
        sido atingidos
        """
        if not self._objetivos or self._modelo_mundo.alterado:
            self._planeador.terminar_plano()

        self._planeador.planear(self._modelo_mundo, self._objetivos)

    def _executar(self):
        """
        Método que obtem a acção presente no operador do planeador e
        manda o agente efectua-la caso esta acção seja possível, ou
        seja, caso faça parte da lista de operadores do mundo
        """
        operador = self._planeador.obter_accao(self._modelo_mundo.estado())
        if operador in self._modelo_mundo.operadores():
            return operador.accao

    def _mostrar(self):
        """
        Método que actualiza a vista do modelo do mundo
        """
        self.vista.limpar()
        self._modelo_mundo.mostrar(self.vista)
        self._planeador.mostrar(self.vista)
        self.vista.mostrar_estados(self._objetivos)
