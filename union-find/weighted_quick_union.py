from base import UnionFindBase

class WeightedQuickUnion(UnionFindBase):
    def __init__(self, instructions=True):
        super().__init__(instructions)
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

        self.components -= 1

    def connected(self, first: int, second: int) -> bool:
        return self.__root(first) == self.__root(second)

    def get_tree(self, node):
        node_root = self.__root(node)
        children = self.get_children(node_root) + [node_root]
        return children

    def get_children(self, node, elements=[]):
        children = [i for i, e in enumerate(self.ids) if e == node and i != e]

        for ch in children:
            children = children + self.get_children(ch, elements)

        return children
        
    def __root(self, id: int) -> int:
        p = self.ids[id]
        if p != id:
            root = self.__root(p)
            #self.ids[id] = root
            return root
        else:
            return id


if __name__ == "__main__":
    algorithm = WeightedQuickUnion()

    while True:
        algorithm.parse_input(input())