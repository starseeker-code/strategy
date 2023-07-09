### PATRON DE DISEÑO STRATEGY ###
# Esta es la version "oficial" de refactoring.guru con un algoritmo para
# seleccionar estrategias automaticamente, corresponde a V3

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
        
class Bicicleta(IEstrategia):
    def algoritmo(self):
        print(f"{self.nombre} alquilara una bibicleta, y llegara con {self.tiempo - 45} minutos extra")
        
class Coche(IEstrategia):
    def algoritmo(self):
        print(f"{self.nombre} alquilara un coche, y llegara con {self.tiempo - 25} minutos extra")
        
class Taxi(IEstrategia):
    def algoritmo(self):
        print(f"{self.nombre} utilizara un taxi, y llegara con {self.tiempo - 12} minutos extra")

# 3 - Se crea la interfaz de contexto

class Contexto:
    def __init__(self, nombre, tiempo, dinero=100):  # Se tiene una referencia de la estrategia
        self.nombre = nombre  # Se pasa la info necesaria de contexto a estrategia
        self.dinero = dinero
        self.tiempo = tiempo
        self._estrategia = self.elegir_estrategia()
        self._estrategia.nombre = nombre
        self._estrategia.tiempo = tiempo
        
    @property  # Se mantiene la referencia de la estrategia
    def estrategia(self):
        return self._estrategia
    
    @estrategia.setter  # Se puede cambiar en runtime la estrategia
    def estrategia(self, nueva_estrategia):
        self._estrategia = nueva_estrategia
        self._estrategia.nombre = self.nombre  # Se actualiza la informacion tambien
        self._estrategia.tiempo = 60  # !Override manual para que quede bonito
    
    def elegir_transporte(self):  # Se ejecuta la estrategia
        result = self._estrategia.algoritmo()
        return result
    
    def elegir_estrategia(self):  # Selector que elige automaticamente la estrategia
        if tiempo < 25:
            estrategia = Taxi()
            self.dinero -= 35
        elif tiempo < 45:
            estrategia = Coche()
            self.dinero -= 25
        elif tiempo < 60:
            estrategia = Bicicleta()
            self.dinero -= 10
        else: estrategia = Andar()
        return estrategia


if __name__ == '__main__':
    nombre = input("Nombre de la persona: ")
    tiempo = randint(12, 70)
    print(f"{nombre} tiene 100 € y necesita llegar al aeropuerto en {tiempo} minutos")
    contexto = Contexto(nombre, tiempo)  # En esta version no hay inyeccion de dependencias
    contexto.elegir_transporte()
    print(f"A {contexto.nombre} le quedan {contexto.dinero}€")  # Asi es facil manejar los estados del contexto
    print("En caso de elegir andar para volver...")
    contexto.estrategia = Andar()  # Que haya un selector no impide que se utilice una estrategia concreta
    contexto.elegir_transporte()
