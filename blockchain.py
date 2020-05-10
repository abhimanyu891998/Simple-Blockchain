import hashlib
from time import time
from MerkleTree import MerkleTree

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.transaction_list = []

    def new_transaction(self, sender, recipient, amount):
        #Adds a transaction to the transaction list
        timestamp = int(time())
        transaction = "[" + str(timestamp) + "]" + sender + "->" + recipient + ":" + str(amount)
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
        mT = MerkleTree()
        mT.generateMerkleTree(self.transaction_list)
        return mT.getMerkleRoot()

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
            'timestamp': int(time()),
            'nonce': len(self.transaction_list),
            'merkle_tree_root': None,
            'hash': None
        }
        if len(self.chain) > 0: 
            block['previous_hash'] = self.chain[len(self.chain)-1]['hash']
        else: 
            block['previous_hash'] = None
        block['merkle_tree_root'] = self.generate_merkle_tree()
        block['hash'] = block['merkle_tree_root']

        #Resetting the current list of transactions
        self.transaction_list = []
        #Adding a new block
        self.chain.append(block)
        return block

    def print_chain(self):
        i = 0
        for block in self.chain:
            print('\n \n-------- BLOCK', i,'---------')
            previous_blocks_hash = block['previous_hash']
            merkleRoot = block['merkle_tree_root']
            block_nonce = block['nonce']
            timestamp = block['timestamp']
            block_hash = block['hash']
            print('Previous Block\'s Hash :', previous_blocks_hash)
            print('Merkle Tree Root :', merkleRoot)
            print('Block\'s Nonce Value :', block_nonce)
            print('Timestamp of creation :', timestamp)
            print('Block\'s Hash:', block_hash)
            print('------- END OF BLOCK ---------- \n \n')
            i= i+1

def main():
    blockchain = Blockchain()
    blockchain.new_transaction('Alice', 'Bob', 10)
    blockchain.generate_block()
    blockchain.new_transaction('Alice', 'Bob', 1)
    blockchain.new_transaction('Charlie', 'Dan', 6)
    blockchain.new_transaction('Dan', 'Bob', 2)
    blockchain.generate_block()
    blockchain.new_transaction('Bob', 'Alice', 4)
    blockchain.new_transaction('Elle', 'Alice', 9)
    blockchain.generate_block()
    blockchain.new_transaction('Bob', 'Alice', 5)
    blockchain.new_transaction('Elle', 'Alice', 3)
    blockchain.generate_block()
    blockchain.print_chain()

if __name__ == "__main__":
    main()
