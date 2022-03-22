from abc import ABC, abstractmethod

"""
Interface abstrata que indica qual o estímulo que um dado sensor
detectou. Define o método abstrato detectar que tem como atributo a
percepção do ambiente por parte do sensor.
"""
class Estimulo(ABC):

    """
    Método abstrato que recebe como atributo a percepção do exterior
    e traduz a mesma num float que permite obter a sua intensidade.
    Este método quando implementado na classe Reacção permite saber
    se existe algum estímulo, ou seja, detectar um estímulo.
    """
    @abstractmethod
    def detectar(self, percepcao):
        """Detetectar estímulo numa percepção"""
