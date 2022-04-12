
from ecr.estimulo import Estimulo


class EstimuloObst(Estimulo):
    """
    Classe associada à classe Estimulo correspondendo ao estímulo de detectar
    um obstáculo na proximidade do agente percepcionado pelo mesmo

    Esta classe implementa o estímulo detetado pelo sensor implementando o
    construtor e métodos da classe Estimulo recorrendo à direcção em que o
    obstáculo se encontra e à detecção do mesmo e da distância ao agente

    @param direccao: direcção que se pretende verificar a existência de um
        obstáculo
    @param intensidade: intensidade da percepção, relacionada com a distância
        a um obstáculo, default = 1.0

    @method detectar: metódo que permite ao agente detectar um obstáculo
    """

    def __init__(self, direccao, intensidade=1.):
        """
        Método construtor da classe EstimuloObts

        Através da direcção que o sensor do agente analisa o ambiente em redor
        do mesmo e da intensidade da percepção é criado um estímulo correspondente
        à detecção de um obstáculo próximo do agente

        @param direccao: direcção em estudo por parte do sensor
        @param intensidade: intensidade da percepção, relacionada com a distância
            a um obstáculo, default = 1.0
        """
        self._direccao = direccao
        self._intensidade = intensidade
    
    def detectar(self, percepcao):
        """
        Método que permite ao agente percepcionar o ambiente em seu redor e
        detectar obstáculos na direcção em estudo

        Através deste método a percepção do agente é traduzida num float que
        corresponde à intensidade do estímulo, permitindo assim saber se a
        percepção activa um estímulo do agente ou não, ou seja, permite saber
        se o agente se encontra nas imediações de um obstáculo ou não

        @param percepcao: percepção do ambiente atual por parte do agente
        @returns: intensidade da percepção, correspondente a 0 caso o agente
            não se encontre nas imediações de um obstáculo ou à intensidade
            em função da distância a que se encontra o agente do obstáculo
            em causa
        """
        if percepcao.contacto_obst(self._direccao):
            return self._intensidade
        else:
            return 0