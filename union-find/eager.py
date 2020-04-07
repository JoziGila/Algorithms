from base import UnionFindBase

class UnionFindEager(UnionFindBase):
    def __init__(self):
        self.ids = []

    def initialize(self, num: int):
        for i in range(num):
            self.ids.append(i)

    def union(self, first: int, second: int):
        if self.connected(first, second):
            return
        
        first_id = self.ids[first]
        second_id = self.ids[second]
        
        self.ids = [second_id if id == first_id else id for id in self.ids]
    
    def connected(self, first: int, second: int) -> bool:
        return self.ids[first] == self.ids[second]

    def components(self) -> int:
        return len(set(self.ids))


if __name__ == "__main__":
    eager = UnionFindEager()

    while True:
        eager.parse_input(input())