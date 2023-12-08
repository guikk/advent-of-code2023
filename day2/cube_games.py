import sys
from collections import defaultdict

# Day 2-1 Sum of possible game IDs
def is_possible(game: list[dict[str,int]], bag: dict[str,int]) -> bool:
    for reveal in game:
        for color, n in reveal.items():
            if not color in bag:
                return False
            if bag[color] < n:
                return False
    return True

# Day 2-2 Sum of minimal bag powers
def fewest_cubes(game: list[dict[str,int]]) -> dict[str,int]:
    bag = defaultdict(int)
    for reveal in game:
        for color, n in reveal.items():
            bag[color] = max(bag[color], n)
    return bag

def read_game(game_str: str) -> (int, list[dict[str,int]]):
    id_str, reveals_str = game_str.rstrip().split(':')

    id = int(id_str[5:])

    game = []
    for reveal_str in reveals_str.split(';'):
        reveal = {}
        for color_str in reveal_str.split(','):
            n_str, color = color_str.strip().split()
            reveal[color] = int(n_str)

        game.append(reveal)

    return id, game

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please inform the calibration document!")
        exit(0)

    bag = {
        "red":12,
        "green":13,
        "blue":14
    }

    with open(sys.argv[1],"r") as puzzle_input:
        answer = 0
        for line in puzzle_input.readlines():
            id, game = read_game(line)
            bag = fewest_cubes(game)
            answer += bag["red"] * bag["green"] * bag["blue"]
        print(f"The sum of minimal bag powers is {answer}")
