class UnionFindBase(object):
    def __init__(self):
        self.ids = []
        self.components = 0

        self.__print_instructions()

    def __print_instructions(self):
        print("To initialise array: num [number of elements]")
        print("To perform union: union [first element] [second element]")
        print("To check if connected: connected [first element] [second element]")
        print("To print number of components: count")

    def parse_input(self, data: str):
        payload = data.strip().split(" ")
        input_type = payload[0]

        if (input_type == "num"):
            num_elements = int(payload[1])
            self.components = num_elements
            self.initialize(num_elements)

        elif (input_type == "union"):
            first, second = int(payload[1]), int(payload[2])

            # If union is successful there is one less component
            if self.union(first, second):
                self.components -= 1
             

        elif (input_type == "connected"):
            first, second = int(payload[1]), int(payload[2])
            print(self.connected(first, second))

        elif (input_type == "count"):
            print("Number of components: {}".format(self.components))


    def initialize(self, num: int):
         for i in range(num):
            self.ids.append(i)

    def union(self, first: int, second: int) -> bool:
        # Change all the IDs of the first object's component to the ID of the second object
        pass

    def connected(self, first: int, second: int) -> bool:
        # Check if objects belong to the same component
        pass