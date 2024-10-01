class CityData:
    def __init__(self, name):
        self.name = name
        self.outConCount = 0
        self.outCons = []
        self.seen = False
        self.predecessor = -1

def read_city_data():
    cities = [CityData("Lahore"),CityData("Kasur"),CityData("Jazira"),CityData("Bakhar"),CityData("Okara"),CityData("Jhang"),CityData("Khosab"),CityData("Sahiwal")]
    cities[0].outCons = [1, 3]
    cities[1].outCons = [7]
    cities[2].outCons = []
    cities[3].outCons = []
    cities[4].outCons = [1, 3, 6]
    cities[5].outCons = [0, 3]
    cities[6].outCons = [4]
    cities[7].outCons = [5]
    return cities

def find_city_index(cities, city_name):
    for i in range(len(cities)):
        if cities[i].name == city_name:
            return i
    return -1

def dfs(cities, current_index, destination_index):
    cities[current_index].seen = True

    if current_index == destination_index:
        return True

    for i in cities[current_index].outCons:
        if not cities[i].seen:
            cities[i].predecessor = current_index
            if dfs(cities, i, destination_index):
                return True

    return False

def construct_path(cities, start_index, destination_index):
    path = []
    current = destination_index
    while current != -1:
        path.append(cities[current].name)
        path.append('--->')
        current = cities[current].predecessor
    return path[::-1]

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
        return path[1:]

    else:
        return f"No path from {start_city} to {destination_city}."

def main():
    start_city = input("Enter the name of the starting city: ")
    destination_city = input("Enter the name of the destination city: ")
    result = find_route(start_city, destination_city)
    print(result)

main()

