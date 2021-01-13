class Station:
    def __init__(self, line: str, name: str, coord: tuple):
        self.line = set()
        self.line.add(line)
        self.name = name
        self.coord = coord
        self.connections = set()

    def __repr__(self):
        return "{}{}{}".format(self.line, self.name, self.coord)

    def __str__(self):
        return "{}: {}".format(self.line, self.name, self.coord)

    @staticmethod
    def are_nearby(station_a: 'Station', station_b: 'Station'):  # forward reference
        ax, ay = station_a.coord
        bx, by = station_b.coord
        return abs(ax - bx) < 10 and abs(ay - by) < 10

    def __eq__(self, other: 'Station'):
        return self.name == other.name and self.are_nearby(self, other)

    def __hash__(self):
        return hash(self.name) ^ hash(self.coord[0])

    def add_line(self, line):
        self.line.add(line)

    def add_connection(self, station):
        if station is None:
            pass
        else:
            self.connections.add(station)  # add new station as connection to the self
            station.connections.add(self)