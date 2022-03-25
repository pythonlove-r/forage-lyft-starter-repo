from abc import ABC, abstractmethod

class Car(Serviceable):
	def __init__(self, engine,battery):
        self.Engine = Engine
        self.Battery=Battery
    def needs_service(self, Engine, Battery):
        self.__Car.append(Engine,Battery);
