import heapq

class LineGraph:
    def __init__(self):
        self.vertices = {}

    def add_vertices(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, source, target, weight, time):
        """Add a weighted edge between source and target vertices with time."""
        self.add_vertices(source)
        self.add_vertices(target)
        self.vertices[source].append((target, weight, time))
        self.vertices[target].append((source, weight, time))

    def __str__(self):
        return str(self.vertices)

def dijkstra_shortest_time(graph, start):
    """Dijkstra's algorithm to find the shortest path based on time from the start vertex."""
    pq = [(0, 0, start)]  # (time, distance, vertex)
    times = {start: 0}
    distances = {start: 0}
    predecessors = {start: None}
    
    while pq:
        current_time, current_distance, current_vertex = heapq.heappop(pq)

        if current_time > times.get(current_vertex, float('inf')):
            continue

        for neighbor, weight, time in graph[current_vertex]:
            new_time = current_time + time
            new_distance = current_distance + weight
            if new_time < times.get(neighbor, float('inf')):
                times[neighbor] = new_time
                distances[neighbor] = new_distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(pq, (new_time, new_distance, neighbor))

    return times, distances, predecessors

def print_shortest_time_path(predecessors, times, distances, start, target):
    """Reconstruct and print the shortest path based on time with instructions."""
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = predecessors.get(current)
    path.reverse()

    if path[0] == start:
        print(f"Shortest path from {start} to {target}:")
        print(" -> ".join(path))
        print("\nTravel Instructions:")

        line = None
        instructions = []
        start_station = path[0]
        for i in range(len(path) - 1):
            current_station = path[i]
            next_station = path[i + 1]
            new_line = determine_line(current_station, next_station)

            if line is None:
                line = new_line

            if new_line != line and new_line != "Interchange":
                instructions.append(f"Board {line} at {start_station} station, drop at {current_station} station.")
                line = new_line
                start_station = current_station

        instructions.append(f"Board {line} at {start_station} station, drop at {target} station.")

        for instruction in instructions:
            print(instruction)

        total_time = times.get(target, float('inf'))
        total_distance = distances.get(target, float('inf'))
        print(f"\nTotal travel time: {total_time} minutes")
        print(f"Total travel distance: {total_distance} kilometers")
    else:
        print(f"No path exists from {start} to {target}.")

def determine_line(station1, station2):
    """Determine the train line for a given pair of stations."""
    lrt1_stations = [
        'Roosevelt', 'Balintawak', 'Monumento', '5th Avenue', 'R. Papa', 'Abad Santos', 
        'Blumentritt', 'Tayuman', 'Bambang', 'Doroteo Jose', 'Carriedo', 'Central Terminal', 
        'United Nations', 'Pedro Gil', 'Quirino', 'Vito Cruz', 'Gil Puyat', 'Libertad', 
        'EDSA', 'Baclaran'
    ]
    lrt2_stations = [
        'Antipolo', 'Marikina', 'Santolan', 'Katipunan', 'Anonas', 'Araneta Center Cubao - LRT 2',
        'Betty Go Belmonte', 'Gilmore', 'J. Ruiz', 'V. Mapa', 'Pureza', 'Legarda', 'Recto'
    ]
    mrt3_stations = [
        'North Avenue', 'Quezon Avenue', 'GMA Kamuning', 'Araneta Center Cubao - MRT 3',
        'Santolan Anapolis', 'Ortigas', 'Shaw Boulevard', 'Boni', 'Guadalupe', 'Buendia',
        'Ayala', 'Magallanes', 'Taft Avenue'
    ]

    if station1 in lrt1_stations and station2 in lrt1_stations:
        return "LRT1"
    elif station1 in lrt2_stations and station2 in lrt2_stations:
        return "LRT2"
    elif station1 in mrt3_stations and station2 in mrt3_stations:
        return "MRT3"
    else:
        return "Interchange"

# Define the MRT graph with travel times and distances between stations
line_graph = LineGraph()

# LRT Line 1
line_graph.add_edge('Roosevelt', 'Balintawak', 1.9, 5)
line_graph.add_edge('Balintawak', 'Monumento', 2.2, 4)
line_graph.add_edge('Monumento', '5th Avenue', 1.1, 3)
line_graph.add_edge('5th Avenue', 'R. Papa', 0.9, 3)
line_graph.add_edge('R. Papa', 'Abad Santos', 0.6, 6)
line_graph.add_edge('Abad Santos', 'Blumentritt', 0.9, 4)
line_graph.add_edge('Blumentritt', 'Tayuman', 0.7, 3)
line_graph.add_edge('Tayuman', 'Bambang', 0.6, 2)
line_graph.add_edge('Bambang', 'Doroteo Jose', 0.6, 2)
line_graph.add_edge('Doroteo Jose', 'Carriedo', 0.7, 2)
line_graph.add_edge('Carriedo', 'Central Terminal', 0.7, 3)
line_graph.add_edge('Central Terminal', 'United Nations', 1.2, 3)
line_graph.add_edge('United Nations', 'Pedro Gil', 0.8, 2)
line_graph.add_edge('Pedro Gil', 'Quirino', 0.8, 2)
line_graph.add_edge('Quirino', 'Vito Cruz', 0.8, 2)
line_graph.add_edge('Vito Cruz', 'Gil Puyat', 1, 2)
line_graph.add_edge('Gil Puyat', 'Libertad', 0.7, 2)
line_graph.add_edge('Libertad', 'EDSA', 1, 3)
line_graph.add_edge('EDSA', 'Baclaran', 0.6, 9)

# LRT Line 2
line_graph.add_edge('Antipolo', 'Marikina', 3, 7)
line_graph.add_edge('Marikina', 'Santolan', 1.7, 5)
line_graph.add_edge('Santolan', 'Katipunan', 1.7, 4)
line_graph.add_edge('Katipunan', 'Anonas', 0.9, 3)
line_graph.add_edge('Anonas', 'Araneta Center Cubao - LRT 2', 1.4, 2)
line_graph.add_edge('Araneta Center Cubao - LRT 2', 'Betty Go Belmonte', 1.2, 2)
line_graph.add_edge('Betty Go Belmonte', 'Gilmore', 1.1, 2)
line_graph.add_edge('Gilmore', 'J. Ruiz', 0.9, 3)
line_graph.add_edge('J. Ruiz', 'V. Mapa', 1.2, 3)
line_graph.add_edge('V. Mapa', 'Pureza', 1.3, 3)
line_graph.add_edge('Pureza', 'Legarda', 1.4, 3)
line_graph.add_edge('Legarda', 'Recto', 1, 2)

# MRT Line 3
line_graph.add_edge('North Avenue', 'Quezon Avenue', 1.2, 2)
line_graph.add_edge('Quezon Avenue', 'GMA Kamuning', 1, 2)
line_graph.add_edge('GMA Kamuning', 'Araneta Center Cubao - MRT 3', 1.9, 3)
line_graph.add_edge('Araneta Center Cubao - MRT 3', 'Santolan Anapolis', 1.4, 3)
line_graph.add_edge('Santolan Anapolis', 'Ortigas', 2.2, 3)
line_graph.add_edge('Ortigas', 'Shaw Boulevard', 0.8, 3)
line_graph.add_edge('Shaw Boulevard', 'Boni', 1, 2)
line_graph.add_edge('Boni', 'Guadalupe', 0.7, 2)
line_graph.add_edge('Guadalupe', 'Buendia', 1.9, 3)
line_graph.add_edge('Buendia', 'Ayala', 0.9, 2)
line_graph.add_edge('Ayala', 'Magallanes', 1.2, 3)
line_graph.add_edge('Magallanes', 'Taft Avenue', 1.9, 3)

# Interchange stations (connects lines)
line_graph.add_edge('Araneta Center Cubao - LRT 2', 'Araneta Center Cubao - MRT 3', 0, 0)
line_graph.add_edge('Doroteo Jose', 'Recto', 0, 0)
line_graph.add_edge('EDSA', 'Taft Avenue', 0, 0)

if __name__ == "__main__":
    # Take user input for source and destination
    source = input("Enter the source station: ")
    destination = input("Enter the destination station: ")
    print("")

    # Calculate shortest path by time
    if source in line_graph.vertices and destination in line_graph.vertices:
        times, distances, predecessors = dijkstra_shortest_time(line_graph.vertices, source)
        print_shortest_time_path(predecessors, times, distances, source, destination)
    else:
        print("Invalid source or destination.")