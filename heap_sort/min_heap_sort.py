from heap import Heap

class MinHeap(Heap):
    def percolateDown(self, index):
        while self.leftChildIndex(index) < self.size:
            minChildIndex = self.minimumChildIndex(index)
            if self.heapList[index] > self.heapList[minChildIndex]:
                self.heapList[index], self.heapList[minChildIndex] = self.heapList[minChildIndex], self.heapList[index]
            index = minChildIndex

    def buildHeap(self, alist):
        self.heapList = alist[:]
        self.size = len(self.heapList)
        for i in range((self.size // 2) - 1, -1, -1):
            self.percolateDown(i)

    def interchangeTopWithBottom(self):
        tmp = self.heapList[0]
        self.heapList[0] = self.heapList[self.size - 1]
        self.heapList[self.size - 1] = tmp
        self.size -= 1
        self.percolateDown(0)

if __name__ == '__main__':
    data = [10, 3, 9, 1, 2, 7, 8, 12, 465, 7767, 2, 45]
    print("====== Array Unsorted =======")
    print(data)

    heap = MinHeap()
    heap.buildHeap(data)

    print("========== Heap =============")
    print(heap.heapList)

    print("====== Start Sorted =========")
    for i in range(len(heap.heapList)):
        print(f"--- Extract {i+1} number -----")
        heap.interchangeTopWithBottom()
        print(heap.heapList)

    print("====== Array Sorted =========")
    print(heap.heapList)