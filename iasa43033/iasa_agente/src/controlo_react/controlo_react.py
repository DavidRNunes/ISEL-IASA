from sae import Controlo

"""
Classe que especifica a classe abstrata Controlo, implementando-a. Neste
caso corresponde ao tipo de controlo reactivo, ou seja, controla o agente
implementando uma arquitectura reactiva, onde para uma dada percepção
do ambiente corresponde um estímulo que é activado com uma determinada
intensidade, ao qual corresponde uma resposta que se traduz numa acção
do agente. Esta classe recebe um comportamento, que se traduz num
comportamento singular (por exemplo, explorar) ou num comportamento
composto por vários comportamentos (por exemplo, recolher, sendo este
composto pelos comportamentos de aproximar, evitar e explorar). Este
comportamento é posteriormente processado, pelo que esta classe equivale
a um processador de comportamentos, onde é recebida uma percepção do
ambiente, e perante o comportamento selecionado, a percepção é processada
e obtém-se a acção a efectuar pelo agente.
"""
class ControloReact(Controlo):

    """
    Método construtor da classe ControloReact, tem como argumento o
    comportamento que o agente deve ter perante o ambiente que o rodeia
    e guarda esse argumento na variável local. A segunda variável permite
    visualizar um debug na janela.
    """
    def __init__(self, comportamento):
        self._comportamento = comportamento
        self.mostrar_per_dir = True

    """
    Método que associa o comportamento e o controlo através da
    percepção do ambiente, ou seja, perante o ambiente que rodeia o 
    agente é criado um estímulo correspondente, retornando a acção
    correspondente a esse estímulo.
    @args percepcao - percepção do ambiente que rodeia o agente
    @return acção correspondente ao estímulo obtido
    """
    def processar(self, percepcao):
        return self._comportamento.activar(percepcao)