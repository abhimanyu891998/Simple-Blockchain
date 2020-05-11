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
        

        if (self.hasPath(root.left, arr, x, "UpRight") or 
            self.hasPath(root.right, arr, x, "UpLeft")):  
            return True


        arr.pop(-1)  
        return False
    

    def getPath(self,root, x): 
        
        # vector to store the path  
        arr = []  
        
        # if required node 'x' is present  
        # then print the path  
        if (self.hasPath(root, arr, x, "Root")): 
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
        return 0

    def generate_hash(self):
        #Generates a hash
        return 0

    def previous_hash(self):
        #returns the previous hash
        return 0

    def generate_merkle_tree(self):
        mT = MerkleTree()
        mT.generateMerkleTree(self.transaction_list)
        return mT.getMerkleRoot()


    def generate_proof(self, block_index, transaction_index):
        block = self.chain[block_index]
        transaction = block['transaction_list'][transaction_index]
        merkle_root = block['merkle_tree_root']
        hashValue = sha256(str(transaction).encode()).hexdigest()

        path_from_t_to_root = self.getPath(merkle_root, hashValue)[::-1]
        print("Path from transation :", transaction, " with hash ", hashValue," to root is as follows:")
        print(path_from_t_to_root)

        if len(path_from_t_to_root):
            return (hashValue, path_from_t_to_root, merkle_root)
        return None


    def verify_transaction(self, transaction_hash, proof_of_t, merkle_root):
        path_from_root_to_t = self.path_from_root_to_t(proof_of_t)
        computed_path = []
        for direction_item in path_from_root_to_t:
            for direction in direction_item:
                hashValue = direction_item[direction]
                newDirection = None
                if(direction == 'Root'):
                    newDirection = 'Root'
                elif (direction == 'UpLeft'):
                    newDirection = 'DownRight'
                elif (direction == 'UpRight'):
                    newDirection = 'DownLeft'
                else:
                    continue
                if newDirection:
                    computed_path.append({newDirection: hashValue})

        # traverse merkle tree on computed path to check hashes 
        merkleTreeUtil = MerkleTree()
        validated_transation_hash = merkleTreeUtil.trasverseMerkleTreeFromRootAtPath(merkle_root, computed_path)
        if validated_transation_hash.data == transaction_hash:
            print('Transaction with hash :', transaction_hash, ' is validated. ')
        else: 
            print('Transaction with hash :', transaction_hash, ' is invalid. ')
        
            
            

    def path_from_root_to_t(self, path_from_t):
        path_from_root = path_from_t[::-1]
        return path_from_root

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
            transaction_list = block['transaction_list']
            print('Previous Block\'s Hash :', previous_blocks_hash)
            print('Merkle Tree Root :', merkleRoot)
            print('Block\'s Nonce Value :', block_nonce)
            print('Timestamp of creation :', timestamp)
            print('Block\'s Hash:', block_hash)
            print('Number of Transactions in Block: ', len(transaction_list))
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


    # FIRST TESTING
    print("\n\n--------------------------------------------------------------")
    (transaction_hash, proof_of_t, merkle_root_block) = blockchain.generate_proof(2,0)
    if proof_of_t: 
        blockchain.verify_transaction(transaction_hash, proof_of_t, merkle_root_block)
    else: 
        print("Not existing in block")
    print("--------------------------------------------------------------\n\n")
    

    # SECOND TESTING 
    print("\n\n--------------------------------------------------------------")
    (transaction_hash, proof_of_t, merkle_root_block) = blockchain.generate_proof(3,1)
    if proof_of_t:  
        blockchain.verify_transaction(transaction_hash, proof_of_t, merkle_root_block)
    else: 
        print("Not existing in block")
    print("----------------------------------------------------------------\n\n")
    

    

if __name__ == "__main__":
    main()
