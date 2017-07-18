# The input data required for your program is provided in an ASCII text format:
# - The stop which is the starting point of the journey
# - The stop which is the final point of the journey
# - The list of all the stops
# - The routes between the stops

# List of all the stops:
# A series of lines representing the stops (one stop per line) and which
# contains the following fields:
# - The unique identifier of the stop
# - The full name of the stop, between quote marks"
# - The description of the stop (not used)
# - The latitude of the stop (in degrees)
# - The longitude of the stop (in degrees)
# - The identifier of the zone (not used)
# - The url of the stop (not used)
# - The type of stop
# - The mother station (not used)

# These fields are separated by a comma ,
# Example:
# StopArea:ABDU,"Abel Durand",,47.22019661,-1.60337553,,,1,

# The routes between stops:

# A list of lines representing the routes between the stops (one route per
# line). Each line contains two stop identifiers separated by a white space. ​

# Each line represents a one-directional route running from the first
# identifier to the second. If two stops A and B are reciprocally accessible,
# then there will be two lines to represent this route:
# A B
# B A

# Example:
# StopArea:LAIL StopArea:GALH
# StopArea:GALH StopArea:LAIL

# DISTANCE

# The distance d between two points A and B will be calculated using the
# following formula:
# x = (longitudeB - longitudeA) x cos((latitudeB + latitudeA) / 2)
# y = (latitudeB - latitudeA)
# d = sqrt(x² + y²) x 6371

# Note: the latitudes and longitudes are expressed in radians. 6371 corresponds
# to the radius of the earth in km.

# The program will display the list of the full names of the stops along which
# the shortest route passes. If there is no possible route between the starting
# and final stops, the program will display IMPOSSIBLE.


from math import radians, cos, sqrt


def dist(A, B):
    lonB, latB, lonA, latA = B['lon'], B['lat'], A['lon'], A['lat']
    x = (lonB - lonA) * cos((latA + latB) / 2)
    y = (latB - latA)
    d = sqrt(pow(x, 2) + pow(y, 2)) * 6371
    return d


def bellman_ford():
    cost = {n: float('inf') for n in nodes}
    path = {n: [] for n in nodes}
    cost[start] = 0
    path[start] = [start]
    changed = 1
    
    while changed:
        changed = 0
        for link in links:
            a, b = link
            if cost[a] + distances[link] < cost[b]:
                cost[b] = cost[a] + distances[link]
                path[b] = path[a] + [b]
                changed = 1
    if start != end and not len(path[end]):
        return 'IMPOSSIBLE'
    return '\n'.join(stops[stop]['name'] for stop in path[end])


start = input()
end = input()
stops = {}
for i in range(int(input())):
    stop_id, stop_name, _, stop_lat, stop_lon, _, _, stop_type, _ = input().split(',')
    stops[stop_id] = {'name': stop_name.strip('"'),
                      'lat': radians(float(stop_lat)),
                      'lon': radians(float(stop_lon)),
                      'type': stop_type}
links = {tuple(input().split()) for _ in [0]*int(input())}
distances = {}
nodes = {n: set() for n in stops}
for a, b in links:
    distances[(a, b)] = dist(stops[a], stops[b])
    nodes[a].add(b)


print(bellman_ford())