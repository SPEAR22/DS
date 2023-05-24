class BullyAlgorithm:
    def __init__(self, nodes):
        self.nodes = nodes
        self.coordinator = max(nodes)  # Assume the highest node as the coordinator

    def election(self, node):
        if node in self.nodes:
            higher_nodes = [n for n in self.nodes if n > node]
            if higher_nodes:
                print(f"Node {node} initiates an election.")
                for higher_node in higher_nodes:
                    print(f"Node {node} sends an election message to Node {higher_node}.")
                print(f"Node {node} is waiting for the OK message.")
                self.coordinator = None
            else:
                self.coordinator = node
                print(f"Node {node} becomes the new coordinator.")
        else:
            print(f"Node {node} is not part of the system.")

    def coordinator_message(self, node):
        if node in self.nodes:
            if self.coordinator:
                print(f"Node {node} sends a coordinator message to Node {self.coordinator}.")
            else:
                print(f"Node {node} is the coordinator.")
        else:
            print(f"Node {node} is not part of the system.")


# Example usage
nodes = [1, 2, 3, 4, 5]
bully = BullyAlgorithm(nodes)

# Simulate an election
bully.election(2)

# Simulate a coordinator message
bully.coordinator_message(4)

