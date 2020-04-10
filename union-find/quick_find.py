from base import UnionFindBase

class QuickFind(UnionFindBase):
    def union(self, first: int, second: int) -> bool:
        if self.connected(first, second):
            return False
        
        first_id = self.ids[first]
        second_id = self.ids[second]
        
        # If any element belongs to the first group change it to the second
        self.ids = [second_id if id == first_id else id for id in self.ids]
        self.components -= 1
    
    def connected(self, first: int, second: int) -> bool:
        return self.ids[first] == self.ids[second]

if __name__ == "__main__":
    algorithm = QuickFind()

    while True:
        algorithm.parse_input(input())