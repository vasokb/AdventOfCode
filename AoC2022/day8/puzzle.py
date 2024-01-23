from pathlib import Path

lines = Path('AoC2022/day8/data.txt').read_text().rstrip().split('\n')

visibility = 0
for i,tree_line in enumerate(lines):
    for j, tree in enumerate(tree_line):
        col_trees = [c[j] for c in lines]
        # check up
        if all(t < tree for t in col_trees[:i]):
            visibility += 1
        # check down
        elif all(t < tree for t in col_trees[i+1:]):
            visibility += 1
        # check left
        elif all(t < tree for t in lines[i][:j]):
            visibility += 1
        # check right
        elif all(t < tree for t in lines[i][j+1:]):
            visibility += 1


print(f"Part 1: {visibility}")