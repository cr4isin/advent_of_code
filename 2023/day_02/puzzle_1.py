
from re import findall

color_limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def CheckGames(games: str):
    for game in games.split(';'):
        for color in color_limits:
            if colorCount := findall(f'(\d+) {color}', game):
                if int(colorCount[0]) > color_limits[color]:
                    return False
    return True


def main():
    with open('day_02\\input.txt') as file:
        file_text = file.read().splitlines()

    total = 0
    for line in file_text:
        game_id = int(findall('Game (\d+)', line)[0])
        if CheckGames(line):
            total += game_id

    print(total)


if __name__ == '__main__':
    main()
