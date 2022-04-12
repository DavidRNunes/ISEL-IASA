from pee.mec_proc.fronteira.fronteira import Fronteira


class FronteiraLIFO(Fronteira):
    """
    
    """

    def inserir(self, no):
        """
        Implementação do método inserir da superclasse
        insere o elemento no fim
        """
        self._nos.append(no)