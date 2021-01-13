from Utils import *
from Map import Map
from pprint import pprint

FILE_NAME = "stations.json"


def main():

    graph = read_stations(FILE_NAME)
    map = Map(graph)

    start = get_user_selection(graph, prompt="Please enter the name of your starting station:")
    end = get_user_selection(graph, prompt="Please enter the name of your ending station:")

    p = map.get_path(start, end)
    pprint(p)


if __name__ == '__main__':
    main()