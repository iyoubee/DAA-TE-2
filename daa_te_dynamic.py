import tracemalloc
import time


def read_graph_from_file(input_file):
    """
    Reads an adjacency matrix from a text file and returns it as a list of lists.

    Parameters:
    - input_file: Name of the input text file.

    Returns:
    - A list of lists representing the adjacency matrix.
    """
    graph = []
    with open(input_file, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            graph.append(row)
    return graph


def Hamiltonian_path(adj, N):

    dp = [[False for i in range(1 << N)]
          for j in range(N)]

    # Set all dp[i][(1 << i)] to
    # true
    for i in range(N):
        dp[i][1 << i] = True

    # Iterate over each subset
    # of nodes
    for i in range(1 << N):
        for j in range(N):

            # If the jth nodes is included
            # in the current subset
            if ((i & (1 << j)) != 0):

                # Find K, neighbour of j
                # also present in the
                # current subset
                for k in range(N):
                    if ((i & (1 << k)) != 0 and
                        adj[k][j] == 1 and
                        j != k and
                            dp[k][i ^ (1 << j)]):

                        # Update dp[j][i]
                        # to true
                        dp[j][i] = True
                        break

    # Traverse the vertices
    for i in range(N):

        # Hamiltonian Path exists
        if (dp[i][(1 << N) - 1]):
            return True

    # Otherwise, return false
    return False


# Driver Code
# Example usage:
# generated_graph_16, generated_graph_18, generated_graph_20
# non_hamiltonian_graph_16, non_hamiltonian_graph_18, non_hamiltonian_graph_20
input_file = 'non_hamiltonian_graph_20.txt'
loaded_graph = read_graph_from_file(input_file)
N = len(loaded_graph)

start_time = time.time()
tracemalloc.start()
if (Hamiltonian_path(loaded_graph, N)):
    print("YES")
else:
    print("NO")
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 10**6} MB")
print(f"Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()
end_time = time.time()
execution_time = end_time - start_time
print(f"Running Time: {execution_time} seconds")
