from random import choice

from sae import Accao, Direccao

from .resposta_mover import RespostaMover


class RespostaEvitar(RespostaMover):
    """
    Classe que herda os seus métodos da classe RespostaMover que por sua
    vez herda métodos da classe Resposta, consistindo na implementação de
    uma resposta perante o ambiente que consiste no movimento do agente
    numa direcção de forma a evitar um obstáculo percepcionado nas suas
    imediações

    Através desta classe é definida a resposta à percepção de um obstáculo
    na direcção fornecida, que se traduz na identificação de uma direcção
    livre entre as direcções no enumerador Direccao e por entre a lista de
    direcções livres de obstáculos seleciona-se uma para onde o agente se
    desloca

    @param dir_inicial: direcção para a qual o agente se pretendia mover,
        caso esteja ocupada com um obstáculo deve procurar-se uma outra
        direcção que esteja livre

    @method activar: método herdado da classe Resposta, activa a execução
        da acção em função do estímulo percepcionado pelo agente
    @method direccao_livre: método que permite verificar as direcções da
        lista de direcções no enumerador Direccoes por um espaço livre
        de obstáculos
    """

    def __init__(self, dir_inicial=Direccao.ESTE):
        """
        Método construtor da classe RespostaEvitar

        É definida a lista de direcções possíveis e a acção correspondente
        ao movimento do agente na direcção inicialmente fornecida, sendo
        esta direcção também ela guardada numa variável

        @param dir_inicial: direcção inicial para onde o agente se pretende
            mover, default = Direccao.ESTE
        """
        self._dir_inicial = dir_inicial
        self._direccoes = list(Direccao)
        self._accao = Accao(dir_inicial)
        super().__init__(self._accao)

    def activar(self, percepcao, intensidade):
        """
        Método herdado da classe Resposta, implementa a activação da resposta
        ao estímulo de detectar um obstáculo

        Este método, perante a detecção de um obstáculo na percepção actual,
        retorna a acção que o agente deve executar, nomeadamente mover-se na
        direcção fornecida inicialmente, caso essa direcção se encontre livre
        de obstáculos, ou recorrer ao método direccao_livre para encontrar
        uma direcção livre para o agente se mover evitando quaisquer obstáculos
        na sua proximidade

        @param percepcao: percepção atual do ambiente que rodeia o agente
        @param intensidade: intensidade do estímulo percepcionado, neste caso,
            relacionado com a distância a que o agente se encontra do obstáculo
        @returns: a acção a executar pelo agente associada à intensidade para
            identificar a prioridade de execução desta acção, consistindo no
            movimento do agente na direcção livre de obstáculos
        """
        if percepcao.contacto_obst(self._dir_inicial):
            self._accao.direccao = self.direccao_livre(percepcao)

        return super().activar(percepcao, intensidade)

    def direccao_livre(self, percepcao):
        """
        Método auxiliar da classe que permite obter a lista de direcções livres
        de obstáculos retornando uma delas aleatóriamente

        Este método recorre à variável definida no construtor para verificar
        as imediações do agente em cada direcção por obstáculos, guardando numa
        variável as direcções cujo espaço mais próximo se encontra livre de
        obstáculos, retornando de seguida um dos valores da lista aleatóriamente

        @param percepcao: percepção actual do ambiente que rodeia o agente
        @returns: uma direcção livre
        """
        dir_livres = [direccao for direccao in self._direccoes
                      if not percepcao.contacto_obst(direccao)]

        return choice(list(dir_livres))
