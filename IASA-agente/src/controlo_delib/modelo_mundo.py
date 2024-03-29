from mod import EstadoAgente
from plan import ModeloPlan
from sae import Direccao

from .operador_mover import OperadorMover


class ModeloMundo(ModeloPlan):
    """
    Classe que implementa o modelo do mundo através da interface ModeloPlan

    Consiste nos elementos constituintes do mundo que rodeia o agente,
    os operadores que permitem mudanças de estado e os estados que o
    mundo pode tomar - uma representação interna do mundo percepcionado
    pelo agente

    @method actualizar: actualiza o modelo do mundo caso este tenha sofrido
        alterações, como por exemplo, caso um alvo seja capturado
    @method estado: retorna o estado actual do agente
    @method estados: retorna a lista de estados que o agente pode atingir
    @method operadores: retorna a lista de operadores - movimentos - que é
        permitido o agente executar
    @method obter_elem: permite verificar que elemento do enumerador de
        elementos ocupa a posição desse estado (se está vazio, ocupado
        por um obstáculo, alvo, etc.)
    @method mostrar: actualiza a vista do mundo na interface visual
    """

    _alterado: bool
    """ Variável que permite ao agente saber se houve alterações ao
        modelo do mundo, percepcionando-o novamente se necessário """

    def __init__(self):
        """
        Método construtor do Modelo do Mundo

        Inicia o dicionário dos elementos e a lista de estados a vazio,
        e cria uma lista dos operadores possíveis para o agente se mover,
        neste caso, o agente pode mover-se na vertical e na horizontal,
        recorrendo então às direções presentes no enumerador Direccao
        """
        self._elementos = {}  # key posição, entrada elemento
        self._operadores = list(OperadorMover(self, direccao)
                                for direccao in Direccao)
        self._estado = None
        self._estados = []
        self._alterado = False

    @property
    def alterado(self):
        """
        Propriedade que permite ao agente saber se o modelo do mundo sofreu
        alterações
        """
        return self._alterado

    @property
    def elementos(self):
        """
        Propriedade que permite obter os elementos presentes no mundo
        """
        return self._elementos

    def actualizar(self, percepcao):
        """
        Método que actualiza o mundo verificando as alterações
        que o mesmo sofreu

        Quando o agente captura um alvo, os elementos percepcionados
        e os elementos presentes no modelo do mundo deixam de ser os
        mesmos, sendo necessária uma actualização do mundo, nomeadamente
        uma atualização dos elementos e dos estados. As alterações são
        sinalizadas para o agente através da variável booleana _alterado

        @param percepcao: percepção actual do modelo do mundo que rodeia
            o agente
        """
        self._estado = EstadoAgente(percepcao.posicao)
        if not percepcao.elementos == self._elementos:
            self._elementos = percepcao.elementos
            self._estados = list(EstadoAgente(posicao)
                                 for posicao in percepcao.posicoes)
            self._alterado = True
        else:
            self._alterado = False

    def estado(self):
        """
        Método que retorna o estado actual do agente

        @returns: estado actual do agente
        """
        return self._estado

    def estados(self):
        """
        Método que retorna a lista de estados possíveis do agente no
        mundo

        @returns: lista de estados possíveis
        """
        return self._estados

    def operadores(self):
        """
        Método que retorna os operadores do mundo

        Apenas movimentos permitidos são incluídos na lista, ou seja,
        um movimento que colocasse o agente "dentro" de um obstáculo
        (ou que colidisse com o mesmo) não é um movimento possível,
        logo não faz parte desta lista

        @returns: lista de operadores possíveis
        """
        return self._operadores

    def obter_elem(self, estado):
        """
        Método que permite obter o elemento na posição do estado
        fornecido

        Permite verificar para um determinado estado se a posição desse
        estado se encontra vazia ou se está ocupada por um dos possíveis
        elementos do enumerador de elementos

        @param estado: estado do qual se pretende obter o elemento
        @returns: elemento do enumerador de elementos (agente, alvo,
            obstaculo, vazio)
        """
        return self._elementos.get(estado.posicao)

    def mostrar(self, vista):
        """
        Método que actualiza a vista do mundo na janela de visualização

        @param vista: visualização actual do mundo
        """
        vista.mostrar_alvos_obst(self._elementos)
        vista.marcar_posicao(self._estado.posicao)
