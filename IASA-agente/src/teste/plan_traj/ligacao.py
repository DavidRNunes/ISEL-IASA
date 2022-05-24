from dataclasses import dataclass


@dataclass
class Ligacao:
    """
    Classe que guarda o formato de dados permitindo que estes sejam
    implementados por outra classe. Permite criar a ligação entre
    duas localidades, associando as mesmas e o custo da operação de
    transição entre a origem e o destino
    """

    origem: str
    destino: str
    custo: int
