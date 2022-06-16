from mod import Estado

from .memoria_aprend import MemoriaAprend


class MemoriaEsparsa(MemoriaAprend):
    """
    Classe que implementa a interface MemoriaAprend criando um dicionário
    de estados e valores estado-acção (Q(s,a)) que efectivamente permitem
    ao agente lembrar-se de acções praticadas no passado num determinado
    estado e do valor de utilidade da acção praticada

    Através desta classe o agente pode ser lançado num mundo que não conhece
    e, através de tentativa e erro, o agente aprende os contornos do mundo
    que o rodeia e define um mapa de valores de utilidade para cada estado,
    efectivamente mapeando uma política que lhe permite identificar as melhores
    acções a praticar para uma determinada posição do mundo. A memória é
    esparsa uma vez que para valores que não existam - seja por o estado
    ainda não ter sido explorado, seja porque o agente ainda não tentou
    praticar essa acção - é fornecido um valor por omissão, permitindo um
    acesso mais rápido à memória
    """

    _valor_omissao: float
    """ Valor a ser devolvido caso um estado ou acção não se encontrem em memória """
    _memoria: None
    """ Dicionário onde é guardado o conhecimento obtido """
    _estados: Estado
    """ Lista de estados explorados pelo agente """

    def __init__(self, valor_omissao=0.0):
        """
        Método construtor da classe

        @param valor_omissao: valor a retornar caso um estado ou acção não
            estejam guardados em memória
        """
        self._valor_omissao = valor_omissao
        self._estados = set()
        self._memoria = {}

    @property
    def memoria(self):
        """
        Propriedade que permite obter a memória do agente, retornando
        o dicionário da memória do agente

        @returns: dicionário da memória
        """
        return self._memoria

    def q(self, s, a):
        """
        Método que implementa o método que obtém o valor de efectuar uma
        dada acção para um determinado estado

        Através deste método é obtido o valor de utilidade de efectuar
        uma acção fornecida no estado também ele fornecido, recorrendo
        à memória passada da execução dessa acção nesse estado. Caso o
        agente ainda não tenha praticado essa acção nesse estado ou caso
        esse estado não se encontre em memória é retornado o valor por
        omissão

        @param s: estado em estudo
        @param a: acção a praticar
        @returns: valor de realizar a acção a nesse estado, ou o valor
            por omissão caso esse par estado-acção não se encontre no
            dicionário da memória
        """
        return self._memoria.get((s, a), self._valor_omissao)

    def actualizar(self, s, a, q):
        """
        Método que permite actualizar a memória do agente, adicionando
        novos pares estado-acção e o seu valor, bem como incluíndo novos
        estados à lista de estados observados pelo agente

        @param s: estado observado a adicionar ao dicionário
        @param a: acção realizada
        @param q: valor de realizar a acção no estado observado
        """
        self._memoria[s, a] = q
        self._estados.add(s)

    def obter_estados(self):
        """
        Método que permite obter a lista de estados observados pelo
        agente

        @returns: lista de estados observados
        """
        return self._estados
