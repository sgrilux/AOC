import numpy as np

def main(calories_file):
    elves_calories = []
    journal = open(calories_file, 'r')

    elf_tot_calories = 0
    for cal in journal:
        if cal != '\n':
            elf_tot_calories += int(cal.strip())
        elif cal == '' or cal == '\n':
            elves_calories.append(elf_tot_calories)
            elf_tot_calories = 0

    max_calories = np.amax(elves_calories)
    elf_with_more_calories = elves_calories.index(max_calories) + 1
    print(f'The Elf that carries the most calories is Elf n.{elf_with_more_calories}, with {max_calories}')
    top_three = sorted(elves_calories,reverse=True)[0:3]
    print(f'Top three elves calories sum: {np.sum(top_three)}')

if __name__ == '__main__':
    main('./input.txt')
