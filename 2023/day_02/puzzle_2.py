
from re import findall
from math import prod


def GetPower(games: str):
    color_counts = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for game in games.split(';'):
        for color in color_counts:
            if colorCount := findall(f'(\d+) {color}', game):
                color_counts[color] = max(
                    color_counts[color], int(colorCount[0]))
    return prod(color_counts.values())


def main():
    with open('day_02\\input.txt') as file:
        file_text = file.read().splitlines()

    total = 0
    for line in file_text:
        total += GetPower(line)

    print(total)


if __name__ == '__main__':
    main()
