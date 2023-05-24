from mpi4py import MPI

def calculate_partial_sum(arr):
    partial_sum = sum(arr)
    return partial_sum

def distribute_array(arr):
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    if rank == 0:
        # Distribute the array to all processes
        chunk_size = len(arr) // size
        remainder = len(arr) % size

        for i in range(1, size):
            start = i * chunk_size
            end = start + chunk_size

            if i == size - 1:
                # Include the remaining elements in the last chunk
                end += remainder

            chunk = arr[start:end]
            comm.send(chunk, dest=i, tag=0)

        # Calculate the partial sum for the first chunk
        partial_sum = calculate_partial_sum(arr[:chunk_size])

    else:
        # Receive the chunk of the array
        chunk = comm.recv(source=0, tag=0)

        # Calculate the partial sum for the received chunk
        partial_sum = calculate_partial_sum(chunk)

    # Display the intermediate sums calculated at different processors
    print("Rank", rank, "Partial Sum:", partial_sum)

    # Gather all the partial sums at the root process (rank 0)
    total_sum = comm.reduce(partial_sum, op=MPI.SUM, root=0)

    if rank == 0:
        # Display the final sum
        print("Final Sum:", total_sum)

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Example array
    distribute_array(arr)

