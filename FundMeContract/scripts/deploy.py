from brownie import FundMe, MockV3Aggregator, config, network, accounts
from scripts.helpful import get_account, deploy_mocks, persistent

def deploy_fundMe():
	account = get_account()
	if network.show_active() not in persistent:
		padress = config[network.show_active()]["pfadress"]
	else:
		deploy_mocks()
		padress = MockV3Aggregator[-1].address

	deploy_txn = FundMe.deploy(padress,{"from": account})
	return deploy_txn
	
def main():
	deploy_fundMe()
