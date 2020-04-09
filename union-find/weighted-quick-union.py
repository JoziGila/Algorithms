from base import UnionFindBase

class QuickUnion(UnionFindBase):
    def __init__(self):
        super().__init__()
        self.tree_sizes = []

    def initialize(self, num: int):
        super().initialize(num)
        self.tree_sizes = [1] * num

    def union(self, first: int, second: int):
        first_root = self.__root(first)
        second_root = self.__root(second)

        if first_root == second_root:
            return False

        first_tree_size = self.tree_sizes[first_root]
        second_tree_size = self.tree_sizes[second_root]

        if second_tree_size > first_tree_size:
            self.ids[first_root] = second_root
            self.tree_sizes[second_root] += first_tree_size
        else:
            self.ids[second_root] = first_root
            self.tree_sizes[first_root] += second_tree_size

        return True

    def connected(self, first: int, second: int) -> bool:
        return self.__root(first) == self.__root(second)

    def __root(self, id: int) -> int:
        p = self.ids[id]
        if p != id:
            root = self.__root(p)
            self.ids[id] = root
            return root
        else:
            return id


if __name__ == "__main__":
    algorithm = QuickUnion()

    while True:
        algorithm.parse_input(input())