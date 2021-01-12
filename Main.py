from Utils import *
from pprint import pprint

FILE_NAME = "stations.json"


def main():

    graph = read_stations(FILE_NAME)
    start = get_user_selection(graph, prompt="Please enter the name of your starting station:")
    end = get_user_selection(graph, prompt="Please enter the name of your ending station:")


if __name__ == '__main__':
    main()