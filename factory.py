from __future__ import annotations
from abc import ABC, abstractmethod





class VenchileFactory(ABC):
    """
    The Driving class declares the factory method that is supposed to return an
    object of a Venchile class. 
    """

    @abstractmethod
    def factory_method(self) -> Venchile:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()

        # Now, use the product.
        result = f"Creator: The same creator's code has just worked with {product.Driving()}"

        return result


class TruckCreator(VenchileFactory) :
    def factory_method(self) -> Venchile:
        return Truck()


class PlaneCreator(VenchileFactory):
    def factory_method(self) -> Venchile:
        return Plane()


class BusCreator(VenchileFactory):
    def factory_method(self) -> Venchile:
        return Bus()



def client(creator : VenchileFactory) -> None:
    print(creator.Driving())




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


if __name__ == "__main__":
    print("App: Launched with the Plane.")
    client(Plane())

    print("App: Launched with the Bus.")
    client(Bus())
    print("App: Launched with the Truck.")
    client(Truck())
    print("\n")

  