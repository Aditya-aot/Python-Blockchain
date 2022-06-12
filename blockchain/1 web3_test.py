from web3 import Web3


infura_url = "https://mainnet.infura.io/v3/04adbe925d134c9c92b7ae2e0899a16a"

web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)

balance= web3.eth.getBalance("0x384D60c0d44b9ffDD38c13Cb7c7E2B44786db500")
print(web3.fromWei(balance,"ether"))