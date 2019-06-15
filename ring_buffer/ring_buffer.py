class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    self.current += 1
    if self.current == len(self.storage):
      self.current = 0

  def get(self):
    values = []
    for i in self.storage:
      if i:
        values.append(i)
    return values


buffer = RingBuffer(5)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')

buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']