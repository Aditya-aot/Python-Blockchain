from re import T
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

print( "connections checking : ",web3.isConnected)

account_1 = "0x7ca5e4b5dbb7e85EFEdf7bC0b4e3742256b29360"
account_2 = "0xF7F9d98b512569C1C9552a5A9559A34BE72b651f"


private_key_1 = "1eff01a9a9da50b7e15f4b9dce4c6502d2216e7a979943b2167995d5453076f9"



# get the nance
nonce = web3.eth.getTransactionCount(account_1)

#  build a transaction
tx = {
    'nonce' : nonce,
    'to' : account_2,
    'value': web3.toWei(1, "ether") ,
    'gas' : 2000000,
    'gasPrice' : web3.toWei('50', 'gwei')
}

# sign transaction
signed_tx = web3.eth.account.signTransaction(tx,private_key_1)
# send transaction

# get transaction hash 
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# print(tx_hash)
print(web3.toHex(tx_hash))

