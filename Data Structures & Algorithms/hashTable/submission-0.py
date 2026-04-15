class Pair:
    
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

TOMBSTONE = object()

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.mp = [None] * capacity

    def getHash(self, key: int):
        return key % self.getCapacity()

    def insert(self, key: int, value: int) -> None:

        index = self.getHash(key)
        first_tombstone = None
        start = index

        while True:
            if self.mp[index] == None:
                insert_at = first_tombstone if first_tombstone is not None else index
                self.mp[insert_at] = Pair(key, value)
                self.size += 1
                if self.size / self.capacity >= 0.5:
                    self.resize()
                return
            elif self.mp[index] is TOMBSTONE:
                if first_tombstone is None:
                    first_tombstone = index
            elif self.mp[index].key == key:
                self.mp[index].value = value
                return
            index += 1
            index = index % self.getCapacity()
            
            if index == start:
                self.mp[first_tombstone] = Pair(key, value)
                self.size += 1
                if self.size / self.capacity >= 0.5:
                    self.resize()
                return 

    def get(self, key: int) -> int:
        index = self.getHash(key)

        while self.mp[index] is not None:
            if self.mp[index] is not TOMBSTONE and self.mp[index].key == key:
                return self.mp[index].value
            index += 1
            index = index % self.getCapacity()
        return -1

    def remove(self, key: int) -> bool:
        index = self.getHash(key)

        while self.mp[index] is not None:
            if self.mp[index] is not TOMBSTONE and self.mp[index].key == key:
                self.mp[index] = TOMBSTONE
                self.size -= 1
                return True
            index += 1
            index = index % self.getCapacity()
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity = self.capacity * 2
        oldMp = self.mp
        self.mp = [None] * self.capacity
        self.size = 0
        for pair in oldMp:
            if pair and pair is not TOMBSTONE:
                self.insert(pair.key, pair.value)
            
        

