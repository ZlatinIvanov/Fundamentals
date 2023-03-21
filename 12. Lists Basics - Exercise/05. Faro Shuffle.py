cards = input().split()
shuffles = int(input())
half_deck = len(cards) // 2
for i in range(shuffles):
    left_deck = cards[0:half_deck]
    right_deck = cards[half_deck:]
    faro_deck = []
    for j in range(len(left_deck)):
        faro_deck.append(left_deck[j])
        faro_deck.append(right_deck[j])
    cards = faro_deck
print(cards)