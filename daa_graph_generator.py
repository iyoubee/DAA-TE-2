import random


def generate_graph_txt(num_vertices, output_file):
    """
    Generates a random graph and saves the adjacency matrix to a text file.

    Parameters:
    - num_vertices: Number of vertices in the graph.
    - output_file: Name of the output text file.
    """
    graph = [[random.randint(0, 1) for _ in range(num_vertices)]
             for _ in range(num_vertices)]

    with open(output_file, 'w') as file:
        for row in graph:
            file.write(' '.join(map(str, row)) + '\n')


# Example usage:
# Nama file yang disarankan:
# generated_graph_16, generated_graph_18, generated_graph_20
num_vertices = 20
output_file = 'generated_graph_20.txt'

generate_graph_txt(num_vertices, output_file)
