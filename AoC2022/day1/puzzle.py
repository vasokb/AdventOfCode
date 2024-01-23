from pathlib import Path

lines = Path('AoC2022/day1/data.txt').read_text().rstrip().split('\n')

# Part 1
calories_sum = 0
calories_elves = []
for calorie in lines:
    if calorie != '':
        calories_sum = calories_sum + int(calorie)
    else:
        calories_elves.append(calories_sum)
        calories_sum = 0 
print(f"Part 1: {calories_sum}")

# Part 2 
print(f"Part 2: {sum(sorted(calories_elves)[-3:])}")
