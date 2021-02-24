from __future__ import annotations
from abc import ABC, abstractmethod








class CarFactory(ABC):
    @abstractmethod
    def CreateVenchile(self)->Venchile:
        pass

    @abstractmethod
    def CreateManual(self) -> Manual:
        pass










class TruckFactory(CarFactory):
    """
    The Driving class declares the factory method that is supposed to return an
    object of a Venchile class. 
    """
    def CreateVenchile(self) -> Venchile:
        return Truck()

    def CreateManual(self) -> Manual:
        return TruckManual()




class PlaneFactory(CarFactory):
    """
    The Driving class declares the factory method that is supposed to return an
    object of a Venchile class. 
    """
    def CreateVenchile(self) -> Venchile:
        return Plane()

    def CreateManual(self) -> Manual:
        return PlaneManual()



class BusFactory(CarFactory):
    """
    The Driving class declares the factory method that is supposed to return an
    object of a Venchile class. 
    """
    def CreateVenchile(self) -> Venchile:
        return Bus()

    def CreateManual(self) -> Manual:
        return BusManual()






def client_code(factory: CarFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    product_a = factory.CreateVenchile()
    product_b = factory.CreateManual()

    print(f"{product_a.Driving()}")
    print(f"{product_b.ReadManual()}")










class Venchile(ABC):
    @abstractmethod
    def Driving(self):
        pass

class Plane(Venchile):
    def Driving(self) -> str:
        return "Driving plane"

class Truck(Venchile):
    def Driving(self) -> str:
        return "Driving truck"
    
class Bus(Venchile):
    def Driving(self) -> str:
        return "Driving bus"



class ManualFactory(ABC):
    def CreateTruck(self) -> Manual:
        return TruckManual()

    def CreateBus(self) -> Manual:
        return BusManual()

    def CreatePlane(self) -> Manual:
        return PlaneManual()



class Manual(ABC):
    @abstractmethod
    def ReadManual(self):
        pass


class PlaneManual(Manual):
    def ReadManual(self) -> str:
        return "Manual for plane"

class TruckManual(Manual):
    def ReadManual(self) -> str:
        return "Manual for truck"
    
class BusManual(Manual):
    def ReadManual(self) -> str:
        return "Manual for bus"




if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    client_code(TruckFactory())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(PlaneFactory())


    print("Client: Testing the same client code with the third factory type:")
    client_code(BusFactory())

  