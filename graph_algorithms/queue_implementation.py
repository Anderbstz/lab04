class Queue:
    def __init__(self):
        self.items = []
        self.size = 0
    
    def enQueue(self, item):
        """Add an item to the rear of the queue"""
        self.items.append(item)
        self.size += 1
    
    def deQueue(self):
        """Remove and return the front item from the queue"""
        if self.size == 0:
            return None
        item = self.items.pop(0)
        self.size -= 1
        return item
    
    def isEmpty(self):
        """Check if the queue is empty"""
        return self.size == 0
    
    def getSize(self):
        """Return the size of the queue"""
        return self.size