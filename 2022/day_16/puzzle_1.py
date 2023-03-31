
from re import findall


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


def max_pressure(graph: dict[str, list[str]], flow_rate: dict[str, int], time: int, pos: str, alpha: float, current_value: int = 0):
    max_pressures = dict()
    for key in graph:
        max_pressures[key] = (time-len(find_shortest_path(graph, pos, key)))*flow_rate[key]
    max_value = max(max_pressures.values())
    if max_value > 0:
        targets = [key for key in max_pressures if max_pressures[key] >= max_value*alpha]
        new_pressures = dict()
        for target in targets:
            new_flow_rate = flow_rate.copy()
            new_flow_rate[target] = 0
            new_pressures[target] = max_pressure(graph, new_flow_rate, time - len(find_shortest_path(graph, pos, target)), target, alpha, max_pressures[target])
        current_value += max(new_pressures.values())
    return current_value


graph = dict()
flow_rate = dict()
with open('day_16\\input.txt') as file:
    for line in file:
        vertex = findall('Valve (\w+)', line)[0]
        neighbors = findall('tunnels* leads* to valves* ([\w, ]+)', line)[0].split(', ')
        flow = int(findall('flow rate=(\d+)', line)[0])
        graph[vertex] = neighbors
        flow_rate[vertex] = flow

print(max_pressure(graph, flow_rate, 30, 'AA', .25))
