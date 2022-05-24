from controlo_delib import ControloDelib
from controlo_react import ControloReact, Explorar, Recolher
from plan import PlanPEE
from sae import Controlo, Simulador


class ControloTeste(Controlo):
    """
    Teste ao agente usando um controlo de teste

    Apenas testamos o ambiente de simulação
    """

    def processar(self, percepcao):
        print("processar")


"""
Teste ao agente usando um controlador reactivo

No caso de se pretender testar o comportamento explorativo do agente
recorremos ao comportamento explorar, que leva o agente a mover-se
de forma aleatória no ambiente que o rodeia, chocando com as paredes
(que podemos observar visualmente quando a cor do agente muda para
vermelho) e recolhendo alvos que aleatóriamente passe por cima.

No caso de se pretender testar o comportamento composto Recolher,
constituído pelos comportamentos AproximarAlvo, EvitarObst e Explorar,
podemos observar que o agente se desloca de uma forma muito menos
aleatória, uma vez que quando detecta um alvo o agente se desloca
directamente em direcção ao alvo, recolhendo-o e avaliando em todos
os momentos a proximidade de obstáculos, tanto que o agente com este
comportamento activo não choca com as paredes. O movimento do agente
torna-se errático como no comportamento explorativo apenas quando não
detecta nenhum alvo (situações que já tenha recolhido todos os alvos
presentes numa área e tenha de se deslocar para detectar outro alvo).
"""
explorar = Explorar()
recolher = Recolher()
controlo_react = ControloReact(recolher)

"""
Teste ao agente usando um controlador deliberativo

Para testar o agente deliberativo criamos um plano recorrendo aos
planeadores da biblioteca plan e fornecemos esse planeador ao controlador
do controlo deliberativo. Caso se pretenda testar diferentes mecanismos
de procura é necessário alterar o mecanismo em uso no planeador.

Quando executado podemos ver o agente em acção, recolhendo os alvos com
precisão, não aleatóriamente como no controlo reactivo. A rapidez com que
o agente captura todos os alvos depende apenas do mecanismo de procura a
ser utilizado, sendo que alguns permitem obter o percurso com menor custo
a custo da rapidez de execução do algoritmo.
"""
planeador = PlanPEE()
controlo_delib = ControloDelib(planeador)


"""
Ativação do controlador no ambiente de simulador

i - iniciar; t - terminar; p - pausa; e - executar passo; v - velocidade 
"""
Simulador(4, controlo_delib).executar()
