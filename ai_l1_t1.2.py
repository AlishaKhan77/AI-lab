class CityData:
    def __init__(self, name):
        self.name = name  # Name of the city
        self.outConCount = 0  # Number of outgoing connections (optional in this case)
        self.outCons = []  # List to store outgoing connections
        self.seen = False  # Track if the city has been visited
        self.predecessor = -1  # To trace back the path

def read_city_data():
    # Simulating data as per the example given in the document
    cities = [
        CityData("Lahore"),
        CityData("Kasur"),
        CityData("Jazira"),
        CityData("Bakhar"),
        CityData("Okara"),
        CityData("Jhang"),
        CityData("Khosab"),
        CityData("Sahiwal")
    ]

    # Outgoing connections (simulated from the pb.txt example in the attachment)
    cities[0].outCons = [1, 3]     # Lahore connects to Kasur, Bakhar
    cities[1].outCons = [7]        # Kasur connects to Sahiwal
    cities[2].outCons = []         # Jazira has no outgoing connections
    cities[3].outCons = []         # Bakhar has no outgoing connections
    cities[4].outCons = [1, 3, 6]  # Okara connects to Kasur, Bakhar, Khosab
    cities[5].outCons = [0, 3]     # Jhang connects to Lahore, Bakhar
    cities[6].outCons = [4]        # Khosab connects to Okara
    cities[7].outCons = [5]        # Sahiwal connects to Jhang

    return cities

def find_city_index(cities, city_name):
    for i, city in enumerate(cities):
        if city.name == city_name:
            return i
    return -1

def dfs(cities, current_index, destination_index):
    # Mark the current city as visited
    cities[current_index].seen = True

    if current_index == destination_index:
        return True  # Found the destination

    for neighbor in cities[current_index].outCons:
        if not cities[neighbor].seen:
            cities[neighbor].predecessor = current_index  # Track the predecessor
            if dfs(cities, neighbor, destination_index):
                return True

    return False

def construct_path(cities, start_index, destination_index):
    path = []
    current = destination_index
    while current != -1:
        path.append(cities[current].name)
        current = cities[current].predecessor
    return path[::-1]  # Reverse to get the correct order

def find_route(start_city, destination_city):
    cities = read_city_data()
    start_index = find_city_index(cities, start_city)
    destination_index = find_city_index(cities, destination_city)

    if start_index == -1:
        return f"{start_city} is not a valid city."
    if destination_index == -1:
        return f"{destination_city} is not a valid city."

    if dfs(cities, start_index, destination_index):
        path = construct_path(cities, start_index, destination_index)
        return " -> ".join(path)
    else:
        return f"No path from {start_city} to {destination_city}."

# Example Usage
start_city = input("Enter the name of the starting city: ")
destination_city = input("Enter the name of the destination city: ")
result = find_route(start_city, destination_city)
print(result)
