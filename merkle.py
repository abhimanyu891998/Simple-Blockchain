from MerkleRoot import MerkleRoot
from MerkleNode import MerkleNode
from hashlib import sha256

class MerkleTree(object):
  def __init__(self):
    self.merkleRoot = None

  def generateMerkleTree(self, transactions):
    nodes = []
    if len(transactions) % 2 != 0:
      lastElement = transactions[len(transactions)-1]
      transactions.append(lastElement)

    for transaction in transactions: 
      # hash this transaction
      hashValue = sha256(str(transaction).encode()).hexdigest()
      node = MerkleNode(None, None, hashValue)
      nodes.append(node)
    print('At level 0', *nodes)
    for i in range(0, int(len(transactions)/2)):
      level = []
      if len(nodes) == 1:
          break
      for j in range (0, len(nodes), 2):
        nodeA = nodes[j]
        if j==len(nodes)-1: 
          nodeB = nodes[j]
        else: 
          nodeB = nodes[j+1]
        concatenatedHash = nodeA.data + nodeB.data
        hashValue = sha256(concatenatedHash.encode()).hexdigest()
        node = MerkleNode(nodeA, nodeB, hashValue)
        level.append(node)
      nodes = level
      print('At level ',i+1, 'nodes are ', *level)
    
    if(len(level) == 1):
      self.merkleRoot = level[0]
    else: 
      print("Some thing wrong with logic")
  
  def getMerkleRoot(self):
    return self.merkleRoot




