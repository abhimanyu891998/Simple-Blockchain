import MerkleNode

class MerkleRoot(object):
  def __init__(self):
    self.merkleRoot = None

  def setMerkleRoot(self, merkleRoot): 
    self.merkleRoot = merkleRoot
  
  def getMerkleRoot(self):
    return self.merkleRoot