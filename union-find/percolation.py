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

    def __get_open_neighbours(self, index: int) -> List[int]:
        # Return list of neighbourhood indices
        neighbours = [[index // self.num, index % self.num] for _ in range(4)] # Create four neighbours

        # Top, bottom
        neighbours[0][0] = neighbours[0][0] - 1
        neighbours[1][0] = neighbours[1][0] + 1

        # Left, right
        neighbours[2][1] = neighbours[2][1] - 1
        neighbours[3][1] = neighbours[3][1] + 1

        # Keep only indices that are within the grid and are open
        open_flat_indices = []
        for n in neighbours:
            # If any of the indices is out of bound discard neighbour
            keep = True
            for i in n:
                if i < 0 or i >= self.num:
                    keep = False
                    break
            
            if keep:
                flat_index = n[0] * self.num + n[1]
                if self.open[flat_index]:
                    open_flat_indices.append(flat_index)

        return open_flat_indices

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