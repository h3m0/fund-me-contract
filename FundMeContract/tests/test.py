from brownie import FundMe, MockV3Aggregator, config, network, accounts, exceptions
from scripts.helpful import get_account, deploy_mocks, persistent
from scripts.deploy import deploy_fundMe
from scripts.fund_withdraw import fund, withdraw, entrance_fee, value
from web3 import Web3
import pytest
fake_value = Web3.toWei(0.01, "ether")
bad_actor = accounts.add()


def test_can_fund():
	# arrange
	account = get_account()
	fund_me = deploy_fundMe()	
	# action
	fund()	
	# assert
	assert fund_me.addrtoamnt(account.address) >= entrance_fee

def test_can_fund_withdraw():
	# arrange
	account = get_account()
	fund_me = deploy_fundMe()
	# action
	withdraw()
	# assert
	assert fund_me.addrtoamnt(account.address) == 0

def test_only_owner_withdraw():	
	# arrange
	account = get_account()
	fund_me = deploy_fundMe()	
	# action
	with pytest.raises(exceptions.VirtualMachineError):
		fund_me.withdraw({"from": bad_actor})
	
	
	