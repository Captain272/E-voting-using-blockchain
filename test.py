import json

from web3 import Web3
from solc import compile_standard

# Solidity source code
compiled_sol = compile_standard({
    "language": "Solidity",
     "sources": {
         "Greeter.sol": {
             "content": '''
                 pragma solidity ^0.5.0;

                 contract Greeter {
                   string public greeting;

                   constructor() public {
                       greeting = 'Hello';
                   }

                   function setGreeting(string memory _greeting) public {
                       greeting = _greeting;
                   }

                   function greet() view public returns (string memory) {
                       return greeting;
                   }
                 }
              ''' 
         }
     },
     "settings":
         {
             "outputSelection": {
                 "*": {
                     "*": [
                         "metadata", "evm.bytecode"
                         , "evm.bytecode.sourceMap"
                     ]
                 }
             }
         }
 })

# web3.py instance
w3 = Web3(Web3.EthereumTesterProvider())

# set pre-funded account as sender
w3.eth.defaultAccount = w3.eth.accounts[0]

# get bytecode
bytecode = compiled_sol['contracts']['Greeter.sol']['Greeter']['evm']['bytecode']['object']

# get abi
abi = json.loads(compiled_sol['contracts']['Greeter.sol']['Greeter']['metadata'])['output']['abi']

Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

# Submit the transaction that deploys the contract
tx_hash = Greeter.constructor().transact()

# Wait for the transaction to be mined, and get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

greeter = w3.eth.contract(
     address=tx_receipt.contractAddress,
     abi=abi
 )

greeter.functions.greet().call()


tx_hash = greeter.functions.setGreeting('Nihao').transact()
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
greeter.functions.greet().call()
