from Station import Station
from json import load
from typing import List


def read_stations(FILE_NAME):
    graph = dict(list())

    previous = None

    file = open(FILE_NAME, 'r')
    data = load(file)
    for line, stations in data.items():
        for s in stations:
            current = Station(line, s[0], tuple(s[1]))
            if current.name in graph:  # if a station with same name exists
                if graph[current.name] == current:  # checks if the names and locations of two stations are same
                    graph[current.name].add_line(line)
                    graph[current.name].add_connection(previous)
                    previous = graph[current.name]
                else:
                    current.add_connection(previous)
                    graph[current.name] = [graph[current.name], current]
                    previous = current
            else:  # first time seeing the station
                current.add_connection(previous)
                graph[current.name] = current  # add to dict
                previous = current
        previous, current = None, None

    return graph


def get_user_selection(graph, prompt):
    s_name = input(prompt).strip()
    try:
        if type(graph[s_name]) is list:
            print("{} stations has been found with the name '{}'".format(len(graph[s_name]), s_name))
            print(graph[s_name])
            idx = eval(input("Please enter the index of the station you would like to choose"))
            return graph[s_name][idx]
        else:
            return graph[s_name]
    except KeyError:
        print("Station doesn't exist: ", s_name)


def print_itinerary(path: List[Station]):
    print("◉ {}".format(path[0]))
    for i in range(1, len(path) - 1):
        print(" ○ {}".format(path[i]))
        if len(path[i].line) > 1:
            print(" ➲ Tranfer to {}".format(path[i + 1].line))

    print("◉ {}".format(path[-1]))
