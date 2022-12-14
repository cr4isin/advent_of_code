
def play_game(opponent: int, player: int):
    # Input oppenent and players hands. 1 = Rock, 2 = Paper, 3 = Scissors
    return 3 * ((1 + player - opponent) % 3) + player

move_key = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}
score = 0
with open('day_2\\input.txt') as file:
    for line in file:
        o, p = line.strip().split(' ')
        score += play_game(move_key[o], (move_key[o] + move_key[p]) % 3 + 1)
print(score)
