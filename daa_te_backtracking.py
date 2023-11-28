import tracemalloc
import time


def read_graph_from_file(input_file):
    graph = []
    with open(input_file, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            graph.append(row)
    return graph


def is_safe(graph, v, pos, path):
    if graph[path[pos - 1]][v] == 0:
        return False

    if v in path:
        return False

    return True


def ham_path_util(graph, path, pos, V):
    if pos == V:
        return True

    for v in range(V):
        if is_safe(graph, v, pos, path):
            path[pos] = v
            if ham_path_util(graph, path, pos + 1, V):
                return True
            path[pos] = -1

    return False


def ham_path(graph):

    for start_vertex in range(len(graph)):
        path = [-1] * len(graph)
        path[0] = start_vertex
        if ham_path_util(graph, path, 1, len(graph)):
            if -1 not in path:
                print_solution(path)
                return True

    print("Solution does not exist for Hamiltonian Path.")
    return False


def print_solution(path):
    print("Solution Exists: Following is one Hamiltonian Path")
    for vertex in path:
        if vertex != -1:
            print(vertex, end=" ")
    print("\n")


# Example usage:
# generated_graph_16, generated_graph_18, generated_graph_20
# non_hamiltonian_graph_16, non_hamiltonian_graph_18, non_hamiltonian_graph_20
input_file = 'generated_graph_20.txt'
# loaded_graph = read_graph_from_file(input_file)
loaded_graph = read_graph_from_file(input_file)

start_time = time.time()
tracemalloc.start()
ham_path(loaded_graph)
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 10**6} MB")
print(f"Peak memory usage: {peak / 10**6} MB")
tracemalloc.stop()

end_time = time.time()
execution_time = end_time - start_time
print(f"Running Time: {execution_time} seconds")
