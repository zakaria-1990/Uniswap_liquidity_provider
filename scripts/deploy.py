from scripts.helpful_scripts import get_account
from brownie import LiquidityProviding, network, config


def deploy():
    nonfungible_position_manager = "0x"
    account = get_account()
    swap = LiquidityProviding.deploy(nonfungible_position_manager, {"from": account})
    return swap


def main():
    deploy()
