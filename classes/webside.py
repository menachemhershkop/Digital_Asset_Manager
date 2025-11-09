from classes.digital_asset import DigitalAsset
from classes.repotable import Reportable


class Webside(DigitalAsset, Reportable):
    def __init__(self,name, cost:float, monthly_traffic: int, monetization_rate:float):
        super().__init__(name,cost)
        self.monthly_traffic=monthly_traffic
        self.monetization_rate=monetization_rate
    def asset_type(self) -> str:
        return "WEBBSITE"
    def calculate_value(self) -> float:
        value=self.monthly_traffic*self.monetization_rate*12
        return value
    def to_report_line(self):
        return "name:",self.name,"type:",self.asset_type,"date:",self.time,"cost:",self.cost,"trafic:", self.monthly_traffic,"monetization: ",self.monetization_rate,"value: ", self.calculate_value()
