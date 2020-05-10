class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.transaction_list = []

    def generate_block(self):
        #Creates a new block 
        pass

    def new_transaction(self, sender, recipient, amount):
        #Adds a transaction to the transaction list
        pass

    def generate_hash(self):
        #Generates a hash
        pass

    def generate_merkle_tree(self):
        #Creates a merkle tree and returns the root
        pass

    def generate_proof(self):
        #Returns a proof of the transaction
        pass

    def verify_transaction(self):
        #Verify if a transaction T is in the blockchain
        pass


def main():
    print("hello blockchain")

if __name__ == "__main__":
    main()
