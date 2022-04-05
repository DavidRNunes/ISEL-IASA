from controlo_react.controlo_react import ControloReact
from controlo_react.reaccoes.explorar.explorar import Explorar
from controlo_react.reaccoes.recolher import Recolher
from sae import Controlo
from sae import Simulador

"""
Ambiente de teste dos controlos reactivos, fornece-se o comportamento
e pode-se testar o mesmo.
"""
# Ativação
explorar = Explorar()
recolher = Recolher()
controlo = ControloReact(recolher)
Simulador(1, controlo).executar()
