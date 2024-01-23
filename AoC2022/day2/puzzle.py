from pathlib import Path


"""Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock. If both players choose the same shape, the round instead ends in a draw."""
# A = rock
# B = paper
# C = scissors

lines = Path('AoC2022/day2/data.txt').read_text().rstrip().split('\n')

opponent = []
me = []
for line in lines:
    l = line.split(' ')
    opponent.append(l[0])
    me.append(l[1])


my_score = 0
sum_score = 0
for opp, elf in zip(opponent,me):
    if opp == 'A' and elf == 'Z':
        my_score = (3 + 0)
    if opp == 'A' and elf == 'X':
        my_score = (1 + 3)
    if  opp == 'A' and elf == 'Y':
        my_score = (2 + 6)

    if opp == 'B' and elf == 'X':
        my_score = (1 + 0)
    if opp == 'B' and elf == 'Y':
        my_score = (2 + 3)
    if  opp == 'B' and elf == 'Z':
        my_score = (3 + 6)
    
    if opp == 'C' and elf == 'X':
        my_score = (1 + 6)
    if opp == 'C' and elf == 'Y':
        my_score = (2 + 0)
    if  opp == 'C' and elf == 'Z':
        my_score = (3 + 3)
    
    sum_score = sum_score + my_score
print(f"Part 1: {sum_score}")


# Part 2

# Y = draw
# Z = win
# X = lose

rock_points = 1
paper_points = 2
scissors_points = 3

loss = 0
draw = 3
win = 6

my_score = 0
sum_score = 0
for opp, elf in zip(opponent,me):    
    if elf == 'Y':
        if opp == 'A':
            my_score = (3 + 1)
        elif opp == 'B':
            my_score = (3 + 2)
        else:
            my_score = (3 + 3)     

    if elf == 'X':
        if opp == 'A':
            my_score = (0 + 3)
        elif opp == 'B':
            my_score = (0 + 1)
        else:
            my_score = (0 + 2)   

    
    if elf == 'Z':
        if opp == 'A':
            my_score = (6 + 2)
        elif opp == 'B':
            my_score = (6 + 3)
        else:
            my_score = (6 + 1)   
    
    sum_score = sum_score + my_score

print(f"Part 2: {sum_score}")
