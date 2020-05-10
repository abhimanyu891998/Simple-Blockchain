class MerkleNode: 
  def __init__(self, left, right, data):
    self.left = left
    self.right = right
    self.data = data
  
  def __str__(self): 
    return self.data