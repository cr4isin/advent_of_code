
denoms = 'AKQJT98765432'
num_denoms = len(denoms)

def evaluate_hand(line):
    hand, bid = line
    hand_key = sum(denoms.find(card)*pow(num_denoms, index) for index, card in enumerate(reversed(hand)))
    card_counts = []
    for card in set(hand):
        card_counts.append(hand.count(card))
    # 5 of a kind
    if card_counts.count(5):
        hand_type = 0
    # 4 of a kind
    elif card_counts.count(4):
        hand_type = 1
    # Full House
    elif card_counts.count(3) and card_counts.count(2):
        hand_type = 2
    # 3 of a kind
    elif card_counts.count(3):
        hand_type = 3
    # 2 Pair
    elif card_counts.count(2) > 1:
        hand_type = 4
    # 2 of a kind
    elif card_counts.count(2):
        hand_type = 5
    # High Card
    else:
        hand_type = 6
    return (hand_type, hand_key)


with open('day_07\\input.txt') as file:
    file_text = file.read().splitlines()

hands = []
for line in file_text:
    hand, bid = line.split(' ')
    bid = int(bid)
    hands.append((hand, bid))

hands.sort(key=evaluate_hand, reverse=True)
print(sum(rank*bid[1] for rank, bid in enumerate(hands, start=1)))

