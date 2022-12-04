import pathlib

lines = pathlib.Path(r'C:\Users\vasileia.kampouraki\Python code\Main\applications\cnn_lane_boundary_visualizer\advent22\day1\data.txt').read_text().rstrip().split('\n')

calories_sum = 0
calories_elves = []
for calorie in lines:
    if calorie != '':
        calories_sum = calories_sum + int(calorie)
    else:
        calories_elves.append(calories_sum)
        calories_sum = 0 
print(calories_sum)

##### Part 2 #####
print(sum(sorted(calories_elves)[-3:]))
