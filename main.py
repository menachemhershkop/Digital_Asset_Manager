from classes.asset_protfolio import AssertPortfolio
from classes.mobile_app import MobileApp
from classes.webside import Webside

my_portfolio=AssertPortfolio()
my_portfolio.load_portfolio()
website=Webside("news",154.6,1500,45.3)
mobile=MobileApp("game",168.4,1500,4.8)
my_portfolio.add_asset(website)
my_portfolio.add_asset(mobile)
print(my_portfolio.calculate_total_net_worth())
my_portfolio.save_portfolio()
print(mobile.asset_type())
reloaded_portfolio=AssertPortfolio()
reloaded_portfolio.load_portfolio()
print(reloaded_portfolio.calculate_total_net_worth())