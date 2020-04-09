from base import UnionFindBase

class QuickUnion(UnionFindBase):
    def __init__(self):
        super().__init__()
        self.ids = []

    def initialize(self, num: int):
        for i in range(num):
            self.ids.append(i)

    def union(self, first: int, second: int):
        first_root = self.__root(first)
        second_root = self.__root(second)

        self.ids[first_root] = second_root
    
    def connected(self, first: int, second: int) -> bool:
        return self.__root(first) == self.__root(second)

    def components(self) -> int:
        return len([i for i in range(len(self.ids)) if self.ids[i] == i])
    
    # Recursive root finding
    def __root(self, id: int) -> int:
        p = self.ids[id]
        if p != id:
            return self.__root(p)
        else:
            return id


if __name__ == "__main__":
    algorithm = QuickUnion()

    while True:
        algorithm.parse_input(input())