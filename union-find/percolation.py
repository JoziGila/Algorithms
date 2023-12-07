from weighted_quick_union import WeightedQuickUnion
from random import randint
from typing import List

class Percolation:
    def __init__(self, num: int, logging=False):
        self.num = num
        self.wqu = WeightedQuickUnion(instructions=False)

        self.grid_elements = num ** 2
        self.wqu.initialize(self.grid_elements + 2) # Create grid and add two virtual nodes
        self.__connect_virtual_nodes() # Connect virtual nodes to top and bottom rows
        self.open = [False] * self.grid_elements # Keep track of open element indices in grid
        self.closed_ids = [i for i in range(self.grid_elements)] # To easily select opening

        self.logging = logging
        self.log = []

        if self.logging:
            self.log.append("num {}".format(str(self.num)))

    def percolate(self) -> float:
        open_count = 0
        percolated = False
        while not percolated:
            self.__open_random()
            open_count += 1
            percolated = self.__check_percolate()

        # Log open operation
        if self.logging:
            self.log.append("percolation {}".format(",".join(str(x) for x in self.wqu.get_tree(self.grid_elements))))
            self.save_log()

        return open_count / self.grid_elements

    def save_log(self):
        with open('percolation_log.txt', 'w') as f:
            for log in self.log:
                f.write("%s\n" % log)
    
    def __open(self, index: int):
        # Open index and connect with open neighbours
        self.open[index] = True
        neighbours = self.__get_open_neighbours(index)

        for n in neighbours:
            self.wqu.union(index, n)
        
        # Log open operation
        if self.logging:
            self.log.append("open {}".format(index))

    def __open_random(self):
        random_index = randint(0, len(self.closed_ids) - 1)
        random_id = self.closed_ids[random_index]

        self.__open(random_id)
        del self.closed_ids[random_index]


    def __check_percolate(self) -> bool:
        return self.wqu.connected(-1, -2)

    def __connect_virtual_nodes(self):
        # Connect top virtual node
        for i in range(self.num):
            self.wqu.union(-2, i)

        # Connect bottom virtual node
        for i in range(self.num):
            self.wqu.union(-1, -3 - i) # Start from the third last element

if __name__ == "__main__":
    p = Percolation(10, logging=True)
    print(p.percolate())