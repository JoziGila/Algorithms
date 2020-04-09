from base import UnionFindBase

class QuickUnion(UnionFindBase):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.tree_sizes = []

    def initialize(self, num: int):
        for i in range(num):
            self.ids.append(i)
            self.tree_sizes.append(1)

    def union(self, first: int, second: int):
        first_root = self.__root(first)
        second_root = self.__root(second)

        first_tree_size = self.tree_sizes[first_root]
        second_tree_size = self.tree_sizes[second_root]

        if second_tree_size > first_tree_size:
            self.ids[first_root] = second_root
            self.tree_sizes[second_root] += first_tree_size
        else:
            self.ids[second_root] = first_root
            self.tree_sizes[first_root] += second_tree_size

    def connected(self, first: int, second: int) -> bool:
        return self.__root(first) == self.__root(second)

    def components(self) -> int:
        return len([i for i in range(len(self.ids)) if self.ids[i] == i])

    def __root(self, id: int) -> int:
        p = self.ids[id]
        if p != id:
            gp = self.__root(p)
            self.ids[id] = gp
            return gp
        else:
            return id


if __name__ == "__main__":
    algorithm = QuickUnion()

    while True:
        algorithm.parse_input(input())