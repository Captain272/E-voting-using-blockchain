import json
from web3 import Web3



ganache_url="http://127.0.0.1:8545"
web3=Web3(Web3.HTTPProvider(ganache_url))


web3.eth.defaultAccount = web3.eth.accounts[0]


# account="0xC26Ae1B9395CeF7BF93Fda4F1D94B225Aada67B9"



abi=json.loads('[{"inputs":[],"name":"Result","outputs":[{"internalType":"string[]","name":"","type":"string[]"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"address","name":"add","type":"address"}],"name":"add_candidate","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"addhar","type":"uint256"},{"internalType":"uint32","name":"age","type":"uint32"},{"internalType":"address","name":"add","type":"address"},{"internalType":"string","name":"p","type":"string"}],"name":"add_voter","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"all_results","outputs":[{"components":[{"internalType":"address","name":"id","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"vote","type":"uint256"}],"internalType":"struct voting.result[]","name":"","type":"tuple[]"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"cand","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"j","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"passw","type":"string"}],"name":"login","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"result_list","outputs":[{"internalType":"address","name":"id","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"vote","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"st","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"vot","outputs":[{"internalType":"uint32","name":"","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"voteFor","type":"address"},{"internalType":"address","name":"add","type":"address"}],"name":"vote","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"passw","type":"string"}],"name":"voter_address","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"voter_list","outputs":[{"internalType":"address","name":"id","type":"address"},{"internalType":"string","name":"name","type":"string"},{"internalType":"string","name":"password","type":"string"},{"internalType":"uint256","name":"addhar","type":"uint256"},{"internalType":"bool","name":"voted","type":"bool"},{"internalType":"uint32","name":"age","type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"winnerdis","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
address=web3.toChecksumAddress("0x18E2CA79709063F9211DD75B9c7AAc9A8a27E68C")
candidates_list=['0x40C262C71A9c44E378Df7027e9e9011725CBeDEe','0x98A86a8b3B7f3be75E4760de97EcD401CfeF8AA2','0xe43095654E09D430b462D2ACDe9C6c1Ee7e9F80C','0x000CbE1ab1acf4027388705c23ED0CCF0cd348F8','0x9b79D2dB7E69fF553DBeab9E10c6ed7755B98092','0x99fAee9f69ADADAB58031D9551d01FcDDe5C4030']

# tx_hash=Ballot.constructor().transact()
# tx_reciept=web3.eth.waitForTransactionReceipt(tx_hash)


Ballot =web3.eth.contract(
    address=address,
    abi=abi
)
# capcan=Ballot.functions.add_candidate("cap",123,23,"0x000CbE1ab1acf4027388705c23ED0CCF0cd348F8").transact()
# capcan_reciept=web3.eth.waitForTransactionReceipt(capcan)
# capcan=Ballot.functions.add_candidate("cap",123,23,"0x000CbE1ab1acf4027388705c23ED0CCF0cd348F8").call()


# capvot=Ballot.functions.add_voter("cap",123,23,"0x000CbE1ab1acf4027388705c23ED0CCF0cd348F8","123456").transact()
# capvot_reciept=web3.eth.waitForTransactionReceipt(capvot)
# capvot=Ballot.functions.add_voter("cap",123,23,"0x000CbE1ab1acf4027388705c23ED0CCF0cd348F8","123456").call()
# print(capvot)

# rajvot=Ballot.functions.add_voter("raj",123,23,"0x40C262C71A9c44E378Df7027e9e9011725CBeDEe").transact()
# rajvot_reciept=web3.eth.waitForTransactionReceipt(rajvot)
# rajvot=Ballot.functions.add_voter("raj",123,23,"0x40C262C71A9c44E378Df7027e9e9011725CBeDEe").call()


# rajcan=Ballot.functions.add_candidate("raj",123,23,"0x40C262C71A9c44E378Df7027e9e9011725CBeDEe").transact()
# rajcan_reciept=web3.eth.waitForTransactionReceipt(rajcan)
# rajcan=Ballot.functions.add_candidate("raj",123,23,"0x40C262C71A9c44E378Df7027e9e9011725CBeDEe").call()

# tt=Ballot.functions.vote("0x000CbE1ab1acf4027388705c23ED0CCF0cd348F8","0x40C262C71A9c44E378Df7027e9e9011725CBeDEe").transact()
# tt_reciept=web3.eth.waitForTransactionReceipt(tt)
# tt=Ballot.functions.vote("0x000CbE1ab1acf4027388705c23ED0CCF0cd348F8","0x40C262C71A9c44E378Df7027e9e9011725CBeDEe").call()
# print(tt)



# tt=Ballot.functions.Result().transact()
# tt_reciept=web3.eth.waitForTransactionReceipt(tt)
# Result=Ballot.functions.Result().transact()
# tt_reciept=web3.eth.waitForTransactionReceipt(Result)
winner=Ballot.functions.Result().call() 
print(winner)
Result=Ballot.functions.all_results().call() 
print(Result[0][2])


# contract =web3.eth.contract(
#     address=tx_receipt.contractAddress,
#     abi=abi
# )


# print(contract.functions.winnerName().call())

# winnerName=contract.functions.winningProposal().call()
# tx_reciept=web3.eth.waitForTransactionReceipt(tx_hash2)
# winnerName=contract.functions.winnerName().call()
# print(tx)
# print(t)