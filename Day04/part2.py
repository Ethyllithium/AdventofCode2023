next_mult = 1
cards_tuple = []
with open("input.txt", "r") as file:
    for line in file:
        winning_numbers = line.split("|")[0].split(":")[1].split()
        card_numbers = line.split("|")[1].split()
        card_temp = [winning_numbers, card_numbers, 1]
        cards_tuple.append(card_temp)

for card in cards_tuple:
    win_num = card[0]
    match_num = card[1]
    copies = card[2]
    current_card = cards_tuple.index(card)
    for copy in range(copies):
        matches = 0
        for match in match_num:
            if match in win_num:
                matches += 1
        if matches == 0:
            break
        for i in range(matches):
            cards_forward = i + 1
            if current_card + cards_forward >= len(cards_tuple):
                break
            cards_tuple[current_card+cards_forward][2] += 1

total = 0
for card in cards_tuple:
    total += card[2]
    print(card)
print(total)
