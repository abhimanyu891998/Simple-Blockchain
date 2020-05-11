import hashlib
from time import time
from hashlib import sha256
from MerkleTree import MerkleTree

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.transaction_list = []

    def hasPath(self,root, arr, x, pos): 
        
        if (not root): 
            return False
        
        # push the node's value in 'arr'  
        arr.append({pos:root.data})      

        if (root.data == x):      
            return True
        

        if (self.hasPath(root.left, arr, x, "left") or 
            self.hasPath(root.right, arr, x, "right")):  
            return True


        arr.pop(-1)  
        return False
    

    def printPath(self,root, x): 
        
        # vector to store the path  
        arr = []  
        
        # if required node 'x' is present  
        # then print the path  
        if (self.hasPath(root, arr, x, "")): 
            return arr
        
        # 'x' is not present in the  
        # binary tree  
        else: 
            return None

    def new_transaction(self, sender, recipient, amount):
        #Adds a transaction to the transaction list
        timestamp = time()
        transaction = "[" + str(timestamp) + "]" + sender + "->" + recipient + ":" + str(amount)
        self.transaction_list.append(transaction)
        print(transaction)
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

    def check_block_index_for_transaction(self, transaction):
        transaction_time = float(transaction[1 :( transaction.rindex(']') ) ])
        print("transaction_time is", transaction_time)
        index_of_block = None
        print(self.chain[0]['timestamp'])
        if transaction_time < self.chain[3]['timestamp']:
            index_of_block = 0

        else: 
            for i in range (1, len(self.chain) -1):
                block_n = self.chain[i]
                block_n_minus_1 = self.chain[i-1]
                timestamp_block_1 = block_n['timestamp']
                timestamp_block_previous = block_n_minus_1['timestamp']
                # print('Current timestamp', transaction_time)
                # print('N block', timestamp_block_1)
                # print(transaction_time > timestamp_block_1, '   ', transaction_time < timestamp_block_next )
                # print('N + 1', timestamp_block_next)
                if transaction_time < timestamp_block_1 and transaction_time > timestamp_block_previous: 
                    print('Condition true')
                    index_of_block = i
                    break

        print(index_of_block)
        return index_of_block



    def generate_proof(self, transaction):
        #Returns a proof of the transaction
        # proof = []
        # first check the block in which the transaction is 
        block_index = self.check_block_index_for_transaction(transaction)
        for block in self.chain:
            #Just check if a path is there in this block, then just return the path
            continue
        
        return proof

    def verify_transaction(self):
        #Verify if a transaction T is in the blockchain
        return 0

    def generate_block(self):
        #Creates a new block
        block = {
            'previous_hash': None,
            'timestamp': time(),
            'transaction_list': self.transaction_list,
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
        print("block generation time", block['timestamp'])
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
