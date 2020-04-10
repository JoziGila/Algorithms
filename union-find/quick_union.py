from base import UnionFindBase

class QuickUnion(UnionFindBase):
    def union(self, first: int, second: int) -> bool:
        first_root = self.__root(first)
        second_root = self.__root(second)

        if first_root == second_root:
            return False

        self.ids[first_root] = second_root
        self.components -= 1
    
    def connected(self, first: int, second: int) -> bool:
        return self.__root(first) == self.__root(second)
    
    # Recursive root finding because why not
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