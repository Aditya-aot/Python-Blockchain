from audioop import add
import json
from web3 import Web3


ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print( "connections checking : ",web3.isConnected)


abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
address = web3.toChecksumAddress("0x7ca5e4b5dbb7e85EFEdf7bC0b4e3742256b29360")

contract = web3.eth.contract(address=address, abi=abi)

print(contract.functions.greet().call())


# Warning: SPDX license identifier not provided in source 
# file. Before publishing, consider adding a comment 
# containing "SPDX-License-Identifier: " to each source
#  file. Use "SPDX-License-Identifier: UNLICENSED" for 
#  non-open-source code. Please see https://spdx.org for 
#  more information.
-

