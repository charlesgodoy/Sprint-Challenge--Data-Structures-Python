class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    if self.current == self.capacity:   # checks to see if full
      self.current = 0
      self.storage[self.current] = item
      self.current += 1

    else:
      self.storage[self.current] = item   # if not full, then just add item and increase current
      self.current += 1

  def get(self):
    return [i for i in self.storage if i]   # only returns true values