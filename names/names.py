import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        self.left.insert(value)

    elif value > self.value:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    if target == self.value:
        return self.value
    elif self.left and target < self.value:
        return self.left.contains(target)
    elif self.right and target > self.value:
        return self.right.contains(target)
    else:
        return None

newNode = BinarySearchTree('hola')
duplicates = []
for name_1 in names_1:
    newNode.insert(name_1)

for name_2 in names_2:
    if newNode.contains(name_2):
        duplicates.append(name_2)

    # for name_2 in names_2:
    #     if name_1 == name_2:
    #         duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

