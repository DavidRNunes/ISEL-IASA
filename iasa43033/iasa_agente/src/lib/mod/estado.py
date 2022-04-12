from abc import ABC, abstractmethod


class Estado(ABC):
    """
    Classe abstrata que representa uma configuração de um sistema ou
    problema

    Esta classe permite definir os estados que compõem o modelo do problema
    do agente, ou seja, as várias formas que o agente se pode encontrar no
    ambiente em função dos alvos, tendo em conta a sua posição e a posição
    dos alvos em relação ao agente. Um estado dispõe de uma identificação
    única que permite distinguir os estados e identificar dois estados
    iguais uma vez que uma dada configuração é única
    """

    @abstractmethod
    def id_valor(self):
        """
        Método abstrato a ser implementado que irá definir um identificador
        único para o estado criado
        
        @returns: identificador único do estado em formato int
        """

    def __hash__(self):
        """
        Função built-in do Python que retorna um id único de um objeto

        Implementamos a função na classe Estado recorrendo ao id_valor
        uma vez que esse id_valor será um identificador único do estado
        quando este é criado, pelo que na função basta retornar o int
        em id_valor
        
        @returns: identificador único do estado
        """
        return self.id_valor()

    def __eq__(self, other):
        """
        Método de comparação do Python que verifica a igualdade entre
        dois objetos

        Através desta função podemos verificar se dois objetos do tipo
        Estado são iguais, ou seja, se dois estados são iguais. Para tal
        recorremos aos hashes dos objetos, ou seja, aos seus identificadores
        únicos, caso tenham o mesmo id são o mesmo objeto
        
        @returns: valor booleano da comparação entre os dois estados,
            retornando true caso sejam o mesmo Estado
        """
        return self.__hash__() == other.__hash__()