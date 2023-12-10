def count_winning_cards(cards):
    card_counts = {i: 1 for i in range(1, len(cards) + 1)}
    won_cards = True
    
    while won_cards:
        won_cards = False
        for i, card in enumerate(cards):
            winning_numbers = set(card[0])
            matching = set(card[1]).intersection(winning_numbers)
            
            if matching:
                for j in range(i + 1, len(cards)):
                    if len(set(cards[j][0]).intersection(matching)) > 0:
                        card_counts[j + 1] += card_counts[i + 1]
                        won_cards = True

    return sum(card_counts.values())

# Leer el archivo input.txt y procesar las tarjetas
with open('input.txt', 'r') as file:
    lines = file.readlines()

cards = []
for line in lines:
    if line.startswith('Card'):
        continue
    parts = line.strip().split('|')
    winning_nums = list(map(int, parts[0].strip().split()))
    your_nums = list(map(int, parts[1].strip().split()))
    cards.append([winning_nums, your_nums])

total_cards = count_winning_cards(cards)
print("Total de tarjetas ganadas en total:", total_cards)
