class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = []
        self.cap = capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.cap == len(self.arr):
            self.resize()

        self.arr.append(n)

    def popback(self) -> int:
        return self.arr.pop()

    def resize(self) -> None:
        self.cap *= 2

    def getSize(self) -> int:
        return len(self.arr)
    
    def getCapacity(self) -> int:
        return self.cap
