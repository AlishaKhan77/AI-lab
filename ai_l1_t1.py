class CityData:
    def _init_(self, name, outConCount, outCons):
        self.name = name
        self.outConCount = outConCount
        self.outCons = outCons
        self.seen = False
        self.predecessor = -1

def read_city_data(filename):
    cities = []
    with open(filename, 'r') as f:
        num_cities = int(f.readline().strip())
        for _ in range(num_cities):
            data = f.readline().strip().split()
            index = int(data[0])  # City index
            name = data[1]        # City name
            outConCount = int(data[2])  # Number of outgoing connections
            outCons = [int(c) for c in data[3:]]  # Indices of outgoing connections
            cities.append(CityData(name, outConCount, outCons))
    return cities

def find_city_index(cities, city_name):
    for i, city in enumerate(cities):
        if city.name == city_name:
            return i
    return -1

def dfs(cities, start_index, destination_index):
    cities[start_index].seen = True
    stack = [start_index]

    while stack:
        current_city = stack.pop()

        if current_city == destination_index:
            return construct_path(cities, start_index, destination_index)

        for neighbor in cities[current_city].outCons:
            if not cities[neighbor].seen:
                cities[neighbor].seen = True
                cities[neighbor].predecessor = current_city
                stack.append(neighbor)

    return None  # No path found

def construct_path(cities, start_index, destination_index):
    path = []
    current = destination_index
    while current != -1:
        path.append(cities[current].name)
        current = cities[current].predecessor
    return path[::-1]  # Reverse the path

def find_route(filename, start_city, destination_city):
    cities = read_city_data(filename)
    start_index = find_city_index(cities, start_city)
    destination_index = find_city_index(cities, destination_city)

    if start_index == -1:
        return f"{start_city} is not a valid city."
    if destination_index == -1:
        return f"{destination_city} is not a valid city."

    path = dfs(cities, start_index, destination_index)

    if path:
        return " -> ".join(path)
    else:
        return f"No path from {start_city} to {destination_city}."

# Example Usage
filename = 'pb.txt'
start_city = input("Enter the name of the starting city: ")
destination_city = input("Enter the name of the destination city: ")
result = find_route(filename, start_city, destination_city)
print(result)
