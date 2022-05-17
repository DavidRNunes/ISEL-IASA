from pee.mec_proc.fronteira.aval.aval_sofrega import AvalSofrega
from pee.mec_proc.melhor_prim.procura_informada import ProcuraInformada


class ProcuraSofrega(ProcuraInformada):
    """
    Classe que implementa a classe abstrata da ProcuraInformada seguindo uma
    variante sôfrega, onde não se tem em conta o custo do percurso já explorado,
    apenas importa a minimização do custo local

    A procura sôfrega obtém soluções sub-óptimas mas obtém as soluções sem necessitar
    de testar tantas soluções como a procura A*, pelo que é um mecanismo mais rápido
    de executar do que a procrura A*, uma vez que se baseia apenas na função h(n) - 
    função heurística que permite obter a estimativa do custo, n, até ao objetivo

    @method _iniciar_avaliador: inicia o avaliador heurístico da procura sôfrega
    """

    def _iniciar_avaliador(self):
        """
        Método que inicia o avaliador heurístico do problema

        É iniciado o avaliador de procura sôfrega obtendo o custo mínimo
        local do nó, ou seja, apenas o custo desde o estado actual até ao
        objetivo, sem ter em conta o custo do percurso explorado

        @returns: avaliador da procura sôfrega
        """
        self._avaliador = AvalSofrega(self._heuristica)

        return self._avaliador