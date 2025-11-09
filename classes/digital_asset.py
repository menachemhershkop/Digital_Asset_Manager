import datetime
from abc import ABC,abstractmethod

class DigitalAsset(ABC):
    def __init__(self,name, cost:float):
        self.__name=name
        self.__registration_data=datetime.date.today()
        self.__cost=cost

    @property
    def name(self):
        return self.__name
    @property
    def time(self):
        return self.__registration_data.isoformat()
    @property
    def cost(self):
        return self.__cost
    @abstractmethod
    def calculate_value(self) -> float:
        pass
    @abstractmethod
    def asset_type(self) -> str:
        pass
