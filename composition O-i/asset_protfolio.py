from classes.digital_asset import DigitalAsset


class AssertPortfolio:
    def __init__(self):
        self.__assets=[]
        self.__filename="digital_assets.csv"
    def add_asset(self,asset:DigitalAsset):
        self.__assets.append(asset)
    def calculate_total_net_worth(self):
        value=0
        for i in self.__assets:
            value+=i.calculate_value()-i.cost
        return round(value, 2)