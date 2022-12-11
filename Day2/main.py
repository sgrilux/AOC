ROCK = 1
PAPER = 2
SCISSORS = 3

WINNER = {
    frozenset({ROCK, PAPER}): PAPER ,
    frozenset({ROCK, SCISSORS}): ROCK,
    frozenset({PAPER, SCISSORS}): SCISSORS
}

def shape(play):
    return {
        'A': ROCK,
        'X': ROCK,
        'B': PAPER,
        'Y': PAPER,
        'C': SCISSORS,
        'Z': SCISSORS
    }.get(play)

def main(file):

    with open(file, 'r') as f:
        all_plays = f.readlines()

        tot_score = 0
        for play in all_plays:
            opponent_play = shape(play.split()[0])
            my_play = shape(play.split()[1])

            if my_play == opponent_play:
                score = my_play + 3
            elif my_play == WINNER.get(frozenset({opponent_play,my_play})):
                score = my_play + 6
            else:
                score = my_play + 0

            tot_score += score
    print(tot_score)

if __name__ == '__main__':
    main('./input.txt')

