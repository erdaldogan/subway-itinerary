from Station import Station
from math import sqrt
import heapq
from typing import List, Set, Dict, Tuple, Optional


class PriorityQueue:
    def __init__(self):
        self.elements: List[Tuple[float, Station]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: Station, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> Station:
        return heapq.heappop(self.elements)[1]


class Map:
    def __init__(self, graph):
        self.graph = graph
        self.open_list = set()
        self.closed_list = set()

    # heuristic function
    # euclidean distance
    @staticmethod
    def estimate_distance(station_a: Station, station_b: Station):
        ax, ay = station_a.coord
        bx, by = station_b.coord
        delta_x = abs(ax - bx)
        delta_y = abs(ay - by)
        return sqrt(delta_x ** 2 + delta_y ** 2)

    def get_path(self, start: Station, end: Station):
        frontiers = PriorityQueue()
        frontiers.put(start, 0)
        path: List[Station] = [start]
        came_from: Dict[Station, Optional[Station]] = {start: None}
        cost_so_far: Dict[Station, int] = {start: 0}

        # self.open_list.add(start)
        # q = self.get_lowest_cost_neighbors(start, end, 0)
        # print("LOWEST COST: ", q)

        while not frontiers.empty():
            current: Station = frontiers.get()
            print("Current: ", current)
            if current == end:
                print("You have reached to your destination!")
                break

            print("\tConnections: ", current.connections)
            for c in current.connections:
                # print("\tC: ", c)
                # print("\tCost so far: ", cost_so_far[current])
                _cost = cost_so_far[current] + 10
                # we add 30 because the distance (cost) of moving between two
                # subway stations are fixed. for out map, it was ~30px between stations
                if c not in cost_so_far or _cost < cost_so_far[c]:
                    print("\tin the if ", c)
                    cost_so_far[c] = _cost
                    p = _cost + self.estimate_distance(c, end)
                    print("\t\tp: ", p)
                    frontiers.put(item=c, priority=p)
                    came_from[c] = current

        return came_from, cost_so_far
