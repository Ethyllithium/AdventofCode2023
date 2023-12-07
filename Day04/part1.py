points = 0
with open("input.txt", "r") as file:
    for line in file:
        matches = 0
        winning_numbers = line.split("|")[0].split(":")[1].split()
        card_numbers = line.split("|")[1].split()
        for number in card_numbers:
            if number in winning_numbers:
                matches += 1
                print(number)
        if matches != 0:
            points += 2 ** (matches - 1)
            print(points)

print(points)