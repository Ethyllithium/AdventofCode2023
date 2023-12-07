with open("input.txt", "r") as file:
    times = file.readline().split(":")[1].strip().split()
    distances = file.readline().split(":")[1].strip().split()
times = [int(x) for x in times]
distances = [int(x) for x in distances]

ways_to_win_prod = 1
for x, time in enumerate(times):
    ways_to_win = 0
    distance_to_beat = distances[x]
    for i in range(time):
        if (time - i) * i > distance_to_beat:
            ways_to_win = (time + 1) - (2 * i)
            break
    ways_to_win_prod *= ways_to_win
print(ways_to_win_prod)
