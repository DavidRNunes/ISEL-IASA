from abc import ABC, abstractmethod
from estado import Estado


class Operador(ABC):
    """
    Interface abstrata que representa um operador

    Um operador consiste numa acção que permite a transição de estado,
    ou seja, a transformação do estado actual do agente e do ambiente
    para um outro estado após aplicar uma transformação (após executar
    uma acção que altera a configuração actual do ambiente)
    """

    @abstractmethod
    def aplicar(self, estado):
        """
        Método abstrato que quando implementado aplica o novo estado ao
        agente, efectivamente gerando a transformação de estado
        
        @returns: estado após a transformação ser aplicada
        """

    @abstractmethod
    def custo(self, estado, estado_suc):
        """
        Método abstrato que quando implementado retorna o custo da
        operação actual
        
        @returns: valor do custo da operação em double
        """