### PATRON DE DISEÑO STRATEGY ###
# En esta version se acopla la informacion necesaria entre contexto y las estrategias

from abc import ABC, abstractmethod
from random import randint

# 1 - Se crean la interfaz de las estrategias

class IEstrategia(ABC):
    @abstractmethod
    def algoritmo(self):
        ...
        
# 2 - Se crean las estrategias

class Andar(IEstrategia):  # Cada estrategia contiene un algoritmo concreto
    def algoritmo(self):
        print(f"{self.nombre} no utilizara ningun metodo de transporte, y llegara con {self.tiempo - 60} minutos extra")
        return 0  # Coste de andar
        
class Bicicleta(IEstrategia):
    def algoritmo(self):
        print(f"{self.nombre} alquilara una bibicleta, y llegara con {self.tiempo - 45} minutos extra")
        return 10  # Coste de alquilar una bicicleta
        
class Coche(IEstrategia):
    def algoritmo(self):
        print(f"{self.nombre} alquilara un coche, y llegara con {self.tiempo - 25} minutos extra")
        return 25
        
class Taxi(IEstrategia):
    def algoritmo(self):
        print(f"{self.nombre} utilizara un taxi, y llegara con {self.tiempo - 12} minutos extra")
        return 35

# 3 - Se crea la interfaz de contexto

class Contexto:
    def __init__(self, nombre, tiempo, dinero=100, *, estrategia):  # Se tiene una referencia de la estrategia
        self._estrategia = estrategia
        self.nombre = self._estrategia.nombre = nombre  # Se pasa la info necesaria de contexto a estrategia
        self.dinero = dinero
        self.tiempo = self._estrategia.tiempo = tiempo
        
    @property  # Se mantiene la referencia de la estrategia
    def estrategia(self):
        return self._estrategia
    
    @estrategia.setter  # Se puede cambiar en runtime la estrategia
    def estrategia(self, nueva_estrategia):
        self._estrategia = nueva_estrategia
        self._estrategia.nombre = self.nombre  # Se actualiza la informacion tambien
        self._estrategia.tiempo = 90  # !Override manual para que quede bonito
    
    def elegir_transporte(self):  # Se ejecuta la estrategia
        result = self._estrategia.algoritmo()
        self.dinero -= result  # Añade el coste del transporte
        return result

    
    
if __name__ == '__main__':
    nombre = input("Nombre de la persona: ")
    tiempo = randint(12, 70)
    print(f"{nombre} tiene 100 € y necesita llegar al aeropuerto en {tiempo} minutos")
    contexto = Contexto(nombre, tiempo, estrategia=Bicicleta())  # En esta version no hay inyeccion de dependencias
    contexto.elegir_transporte()
    print(f"A {contexto.nombre} le quedan {contexto.dinero}€")
    print("En caso de elegir ir andando para volver...")
    contexto.estrategia = Andar()
    contexto.elegir_transporte()
