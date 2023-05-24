class TimeServer:
    def __init__(self, clocks):
        self.clocks = clocks

    def synchronize_clocks(self):
        total_sum = sum(self.clocks)
        average = total_sum // len(self.clocks)

        # Adjust each clock to the average time
        self.clocks = [average] * len(self.clocks)

    def get_clocks(self):
        return self.clocks

# Entry point of the program
if __name__ == "__main__":
    # Create a list of clocks with their initial times
    clocks = [100, 200, 150, 180]

    # Create a time server with the clocks
    time_server = TimeServer(clocks)

    # Synchronize the clocks using the Berkeley algorithm
    time_server.synchronize_clocks()

    # Get the synchronized clocks
    synchronized_clocks = time_server.get_clocks()

    # Print the synchronized clocks
    print("Synchronized Clock Times:")
    for clock in synchronized_clocks:
        print(clock)

