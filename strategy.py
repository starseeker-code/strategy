### PATRON DE DISEÑO STRATEGY ###
# En esta version se utiliza inyeccion de dependencias para desacoplar estrategia y contexto,
# sin embargo, en caso de compartir informacion, tal vez sea buena idea acoplar informacion comun

from abc import ABC, abstractmethod
from random import randint

# 1 - Se crean la interfaz de las estrategias

class IEstrategia(ABC):
    @abstractmethod
    def algoritmo(self):
        ...
        
    def __init__(self, nombre, tiempo=12, dinero=100):
        self.nombre = nombre
        self.tiempo = tiempo
        self.dinero = dinero
        
# 2 - Se crean las estrategias

class Andar(IEstrategia):  # Cada estrategia contiene un algoritmo concreto
    def algoritmo(self):
        print(f"{self.nombre} no utilizara ningun metodo de transporte, y llegara con {self.tiempo - 60} minutos extra")
        
class Bicicleta(IEstrategia):
    def algoritmo(self):
        self.dinero -= 10
        print(f"{self.nombre} alquilara una bibicleta, y llegara con {self.tiempo - 45} minutos extra")
        print(f"A {self.nombre} le quedan {self.dinero}€")
        
class Coche(IEstrategia):
    def algoritmo(self):
        self.dinero -= 25
        print(f"{self.nombre} alquilara un coche, y llegara con {self.tiempo - 25} minutos extra")
        print(f"A {self.nombre} le quedan {self.dinero}€")
        
class Taxi(IEstrategia):
    def algoritmo(self):
        self.dinero -= 35
        print(f"{self.nombre} utilizara un taxi, y llegara con {self.tiempo - 12} minutos extra")
        print(f"A {self.nombre} le quedan {self.dinero}€")

# 3 - Se crea la interfaz de contexto

class Contexto:
    def __init__(self, nombre, tiempo, dinero=100, *, estrategia):  # Se tiene una referencia de la estrategia
        self.nombre = nombre
        self.dinero = dinero
        self.tiempo = tiempo
        self._estrategia = estrategia
        
    @property  # Se mantiene la referencia de la estrategia
    def estrategia(self):
        return self._estrategia
    
    @estrategia.setter  # Se puede cambiar en runtime la estrategia
    def estrategia(self, nueva_estrategia):
        self._estrategia = nueva_estrategia
    
    def elegir_transporte(self):  # Se ejecuta la estrategia
        result = self._estrategia.algoritmo()
        return result

    
    
if __name__ == '__main__':
    nombre = input("Nombre de la persona: ")
    tiempo = randint(12, 50)
    print(f"{nombre} tiene 100 € y necesita llegar al aeropuerto en {tiempo} minutos")
    contexto = Contexto(nombre, tiempo, estrategia=Coche(nombre, tiempo))  # En esta version hay inyeccion de dependencias
    contexto.elegir_transporte()
    print("En caso de elegir un taxi para volver...")
    contexto.estrategia = Taxi(nombre, dinero=contexto._estrategia.dinero)  # La inyeccion de dependencias desacopla pero no es conveniente
    contexto.elegir_transporte()
