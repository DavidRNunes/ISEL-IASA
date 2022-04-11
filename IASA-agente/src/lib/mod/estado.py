from abc import abstractmethod


class Estado:
    """
    
    """

    @abstractmethod
    def id_valor(self):
        """
        
        @returns: int
        """

    def __hash__(self):
        """
        
        @returns: int
        """

    def __eq__(self, other):
        """
        
        @returns: boolean
        """