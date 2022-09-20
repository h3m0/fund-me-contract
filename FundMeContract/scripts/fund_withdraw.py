from brownie import FundMe, MockV3Aggregator, config, network, accounts
from scripts.helpful import get_account, deploy_mocks, persistent
from web3 import Web3

entrance_fee = Web3.toWei(0.032, "ether")
value = Web3.toWei(0.033, "ether")

def fund():	
	account = get_account()
	fundme = FundMe[-1]
	print("Funding...")
	if value >= entrance_fee:
		fund_txn = fundme.fund({"from": account, "value": value})
		print(f"Success!! {value} has been funded to {account}")	
	else:
		print(f"{value} wei is not enough!!")

	

def withdraw():
	account = accounts[0]
	fundme = FundMe[-1]
	print("Withdrawing funds....")
	fundme.withdraw({"from": account})

def main():
	fund()
	withdraw()