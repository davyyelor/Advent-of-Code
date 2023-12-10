with open('input.txt', 'r') as file:
    lines = file.readlines()

cards = []
for line in lines:
    winning_nums, your_nums = line.strip().split('|')
    cards.append((winning_nums.strip(), your_nums.strip()))

total_points = 0

for card in cards:
    winning_numbers, your_numbers = card
    winning_numbers = winning_numbers.split()
    your_numbers = your_numbers.split()

    matches = 0
    for number in your_numbers:
        if number in winning_numbers:
            matches += 1
            winning_numbers.remove(number)

    points = 2 ** (matches - 1) if matches > 0 else 0
    total_points += points

print(f"El valor total de los cartones es: {total_points} puntos")
