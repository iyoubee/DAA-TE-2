import random


def generate_non_hamiltonian_graph_txt(num_vertices, output_file):
    """
    Generates a random non-Hamiltonian graph and saves the adjacency matrix to a text file.

    Parameters:
    - num_vertices: Number of vertices in the graph.
    - output_file: Name of the output text file.
    """
    # Generate a random graph
    graph = [[random.randint(0, 1) for _ in range(num_vertices)]
             for _ in range(num_vertices)]

    # Ensure the graph is not Hamiltonian
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            # Set the edges between vertices i and j to 0
            graph[i][j] = graph[j][i] = 0

    with open(output_file, 'w') as file:
        for row in graph:
            file.write(' '.join(map(str, row)) + '\n')


# Example usage:
# Nama file yang disarankan:
# non_hamiltonian_graph_16, non_hamiltonian_graph_18, non_hamiltonian_graph_20
num_vertices = 20
output_file = 'non_hamiltonian_graph_20.txt'

generate_non_hamiltonian_graph_txt(num_vertices, output_file)
