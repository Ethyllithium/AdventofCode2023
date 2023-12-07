with open("input.txt", "r") as file:
    time = int(file.readline().split(":")[1].replace(" ", ""))
    distance = int(file.readline().split(":")[1].replace(" ", ""))

for i in range(time):
    if (time - i) * i > distance:
        ways_to_win = (time + 1) - (2 * i)
        break
print(ways_to_win)
