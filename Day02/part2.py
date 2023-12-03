import math
answer = 0
with open("input.txt", "r") as file:
    for line in file:
        colours = {"red": 0, "green": 0, "blue": 0}
        line = line.strip().replace(" ", "")
        reveals = line.split(":")[1].replace(";", ",").split(",")
        for reveal in reveals:
            for colour in colours:
                if colour in reveal:
                    count = int(reveal.replace(colour, ""))
                    if count > colours[colour]:
                        colours[colour] = count
        power = math.prod(colours.values())
        answer += power
print(answer)