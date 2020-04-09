class UnionFindBase(object):
    def __init__(self):
        print("To initialise array: num [number of elements]")
        print("To perform union: union [first element] [second element]")
        print("To check if connected: connected [first element] [second element]")
        print("To print number of components: components")

    def parse_input(self, data: str):
        payload = data.strip().split(" ")
        input_type = payload[0]

        if (input_type == "num"):
            num_elements = int(payload[1])
            self.initialize(num_elements)

        elif (input_type == "union"):
            first, second = int(payload[1]), int(payload[2])
            self.union(first, second)

        elif (input_type == "connected"):
            first, second = int(payload[1]), int(payload[2])
            print(self.connected(first, second))

        elif (input_type == "components"):
            print("Number of components: {}".format(self.components()))


    def initialize(self, num: int):
        # Initialize IDs array that relates each object (index) to the component it belongs to (value)
        pass

    def union(self, first: int, second: int):
        # Change all the IDs of the first object's component to the ID of the second object
        pass

    def connected(self, first: int, second: int) -> bool:
        # Check if objects belong to the same component
        pass

    def components(self) -> int:
        # Return number of components formed
        pass