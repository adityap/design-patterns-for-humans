class StationList:
    def __init__(self):
        self.stations = []

    def add(self, station):
        self.stations.append(station)

    def __iter__(self):
        return iter(self.stations)


stations = StationList()
stations.add("Station 1")
stations.add("Station 2")

for station in stations:
    print(station)
