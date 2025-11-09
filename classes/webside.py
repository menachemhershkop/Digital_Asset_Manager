from classes.digital_asset import DigitalAsset
from classes.repotable import Reportable


class Webside(DigitalAsset, Reportable):
    def __init__(self,name, cost:float, monthly_traffic: int, monetization_rate:float):
        super().__init__(name,cost)
        self._monthly_traffic=monthly_traffic
        self._monetization_rate=monetization_rate
    def asset_type(self) -> str:
        return "WEBSITE"
    def calculate_value(self) -> float:
        value=self._monthly_traffic*self._monetization_rate*12
        return value
    def to_report_line(self):
        return "name:",self.name,"type:",self.asset_type,"date:",self.time,"cost:",self.cost,"traffic:", self._monthly_traffic,"monetization: ",self._monetization_rate,"value: ", self.calculate_value()
