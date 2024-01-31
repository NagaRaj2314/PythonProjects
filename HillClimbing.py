import random
import math
# Function to calculate the Euclidean distance between two cities
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)
# Function to calculate the total distance of a route       
def calculate_total_distance(route, cities):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(cities[route[i]], cities[route[i+1]])
    total_distance += calculate_distance(cities[route[-1]], cities[route[0]]) # Return to the starting city
    return total_distance 
# Hill Climbing Algorithm for TSP
def hill_climbing_tsp(cities, max_iterations=1000):
    num_cities = len(cities)
    current_route = random.sample(range(num_cities), num_cities) # Random initial route
    current_distance = calculate_total_distance(current_route, cities)
    for i in range(max_iterations):
        neighbor_route = current_route.copy()
        # Swap two random cities to generate a neighbor route
        city1, city2 = random.sample(range(num_cities), 2)
        neighbor_route[city1], neighbor_route[city2] = neighbor_route[city2], neighbor_route[city1]
        neighbor_distance = calculate_total_distance(neighbor_route, cities)
        if neighbor_distance < current_distance: # If neighbor route is shorter, update current route
            current_route = neighbor_route
            current_distance = neighbor_distance
    return current_route, current_distance
# Example usage
cities = [(0, 0), (1, 3), (4, 6), (7, 1), (2, 8)]
best_route, best_distance = hill_climbing_tsp(cities)
print("Best Route:", best_route)
print("Best Distance:", best_distance)
