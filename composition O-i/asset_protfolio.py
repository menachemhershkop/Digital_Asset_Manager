from classes.digital_asset import DigitalAsset
from classes.mobile_app import MobileApp
from classes.webside import Webside


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
    def save_portfolio(self):
        with open(self.__filename,"w") as file:
            for i in self.__assets:
                file.write(i.to_reprt_line())
    def load_portfolio(self):
        self.__assets=[]
        try:
            with open(self.__filename,"r") as file:
                file.readline()
                for i in file:
                    ",".join(i)
                    if i[1] == "WEBSITE":
                        web=Webside(i[3],float(i[7]),int(i[9]),float(i[11]))
                        self.add_asset(web)
                    if i[1] =="MOBILE_APP":
                        mob=MobileApp(i[3],float(i[7]),int(i[9]),float(i[11]))
                        self.add_asset(mob)
        except:
            raise FileNotFoundError