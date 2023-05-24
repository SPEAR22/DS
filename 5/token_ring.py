import time

def token_ring():
    nodes = int(input("Enter the number of nodes: "))

    # Get and print all nodes
    print("Nodes: ", end="")
    for i in range(nodes):
        print(i, end=" ")
    print(0)

    # Get sender, receiver, and data; initialize token to node 0
    token = 0
    sender = int(input("Enter sender: "))
    receiver = int(input("Enter receiver: "))
    data = input("Enter data: ")

    # Keep passing the token until sender is found
    print("Token passing:", end="")
    for i in range(token, nodes):
        if i % nodes == sender:
            break
        print(" " + str((i + 1) % nodes) + "->", end="")
        time.sleep(1)
    print(" " + str(sender))

    print("--------------------TOKEN WITH SENDER NOW PASSING DATA-------------------")
    print("Sender", sender, "sending data:", data)
    for i in range(sender + 1, receiver + 2):
        print("data", i % nodes, "->", end="")
        time.sleep(1)
    print()
    print("-------------------Receiver", receiver, "received data:", data, "----------------------")
    token = sender

if __name__ == "__main__":
    token_ring()

