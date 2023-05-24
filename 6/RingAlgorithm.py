class RingAlgorithm:
    def __init__(self, nodes):
        self.nodes = nodes

    def election(self, node):
        if node in self.nodes:
            next_node = self.nodes[(self.nodes.index(node) + 1) % len(self.nodes)]
            if next_node > node:
                print(f"Node {node} initiates an election.")
                print(f"Node {node} sends an election message to Node {next_node}.")
            else:
                print(f"Node {node} is the coordinator.")
        else:
            print(f"Node {node} is not part of the system.")


# Example usage
nodes = [1, 2, 3, 4, 5]
ring = RingAlgorithm(nodes)

# Simulate an election
ring.election(3)

