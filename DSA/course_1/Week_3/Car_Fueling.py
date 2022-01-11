def compute_min_refills(travel_distance,
                        max_distance_coverabele, no_of_stations, stops):
    stops.insert(0, 0)
    stops.append(travel_distance)
    count = 0
    while len(stops) > 1:
        index = 1
        while index < len(stops) and stops[index] - stops[0] <= max_distance_coverabele:
            index += 1
            # index now points to farthest reachable gas station
        index -= 1
        # cannot move further, so impossible to reach destination
        if index == 0:
            return -1
        count += 1
        stops = stops[index:]
  # decrease count by 1 to exclude 'refill' that took place at destination
    return count - 1

if __name__ == '__main__':
    while True:
        travel_distance = int(input())
        max_distance_coverabele = int(input())
        no_of_stations = int(input())
        stops = list(map(int, input().split()))
        print(compute_min_refills(travel_distance,
            max_distance_coverabele, no_of_stations, stops))

