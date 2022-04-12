from pee.mec_proc.fronteira.fronteira import Fronteira


class FronteiraFIFO(Fronteira):
    """
    
    """

    def inserir(self, no):
        """
        Implementação do método inserir da superclasse
        """
        self._nos.insert(0, no)