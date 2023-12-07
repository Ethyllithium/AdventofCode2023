from collections import Counter
hands = []
bids = []

with open("input.txt", "r") as file:
    for line in file:
        temp_hand, bid = line.split()
        bids.append(int(bid))
        hand_list = []
        for char in temp_hand:
            if char.isdigit():
                hand_list.append(int(char))
            elif char == "T":
                hand_list.append(10)
            elif char == "J":
                hand_list.append(1)
            elif char == "Q":
                hand_list.append(12)
            elif char == "K":
                hand_list.append(13)
            elif char == "A":
                hand_list.append(14)
        hands.append(hand_list)

updated_hands = []
for hand in hands:
    hand_update = []
    hand_type = Counter(hand).most_common(2)
    jokers = hand.count(1)
    if jokers == 5:
        print("Five of a kind")
        hand.append(7)
        updated_hands.append(hand)
        continue
    if hand_type[0][0] == 1:
        jokers = hand_type[1][1]
    hand_jokers = hand_type[0][1] + jokers
    match hand_jokers:
        case 1:
            print("One of a kind")
            hand.append(1)
        case 2:
            match hand_type[1][1]:
                case 1:
                    print("Pair")
                    hand.append(2)

                case 2:
                    print("Two Pair")
                    hand.append(3)
        case 3:
            if hand_type[1][1] == 2:
                print("Full House")
                hand.append(5)
            else:
                print("Three of a kind")
                hand.append(4)
        case 4:
            print("Four of a kind")
            hand.append(6)
        case 5:
            print("Five of a kind")
            hand.append(7)
    updated_hands.append(hand)

updated_hands_bids = list(zip(updated_hands, bids))
updated_hands_bids.sort(key=lambda k: (k[0][5], k[0][0], k[0][1], k[0][2], k[0][3], k[0][4]))

total_bids = 0
for x, hand in enumerate(updated_hands_bids):
    rank = x + 1
    print(f"Hand: {hand[0]} Bid:{hand[1]} * Rank: {rank} = {rank * hand[1]}")
    total_bids += (rank * hand[1])
print(total_bids)