import hashlib
from time import time

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.transaction_list = []

    def new_transaction(self, sender, recipient, amount):
        #Adds a transaction to the transaction list
        timestamp = time()
        transaction = "[" + timestamp + "]" + sender + "->" + recipient + ":" + amount
        self.transaction_list.append(transaction)
        return 0

    def generate_hash(self):
        #Generates a hash
        return 0

    def previous_hash(self):
        #returns the previous hash
        return 0

    def generate_merkle_tree(self):
        #Creates a merkle tree and returns the root
        


        return 0

    def generate_proof(self):
        #Returns a proof of the transaction
        return 0

    def verify_transaction(self):
        #Verify if a transaction T is in the blockchain
        return 0

    def generate_block(self):
        #Creates a new block
        block = {
            'previous_hash': None,
            'timestamp': time(),
            'nonce': len(self.chain) + 1, #Confused here, they have not given any details for nonce
            'merkle_tree_root': None,
            'hash': None
        }

        block.previous_hash = self.previous_hash()
        block.merkle_tree_root = self.generate_merkle_tree()
        block.hash = self.generate_hash()

        #Resetting the current list of transactions
        self.transaction_list = []

        #Adding a new block
        self.chain.append(block)

        return block


def main():
    print("hello blockchain")

if __name__ == "__main__":
    main()
