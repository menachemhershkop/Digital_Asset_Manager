from logging import setLogRecordFactory

from classes.digital_asset import DigitalAsset
from classes.repotable import Reportable


class MobileApp(DigitalAsset,Reportable):
    def __init__(self,name, cost:float, downloads: int, avg_rating:float):
        super().__init__(name,cost)
        self._downloads=downloads
        self._avg_rating=avg_rating
    def asset_type(self) -> str:
        return "MOBILE_AOO"
    def calculate_value(self) -> float:
        value=self._downloads*0.5+self._avg_rating*1000
        return value
    def to_report_line(self):
        return "type:", self.asset_type(),"name:",self.name,"date:",self.time, "cost: ", self.cost,"downloads: ",self._downloads,"rating: ",self._avg_rating, "value: ",self.calculate_value()