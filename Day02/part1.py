colours = {"red": 12, "green": 13, "blue": 14}
answer = 0
with open("input.txt", "r") as file:
    for line in file:
        possible = True
        game_id = int(line.split(":")[0].split(" ")[1])
        line = line.strip().replace(" ", "")
        reveals = line.split(":")[1].replace(";", ",").split(",")
        for reveal in reveals:
            for colour in colours:
                if colour in reveal:
                    count = int(reveal.replace(colour, ""))
                    if count > colours[colour]:
                        possible = False
        if possible:
            answer += game_id
print(answer)
