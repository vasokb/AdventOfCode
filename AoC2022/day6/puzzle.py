from pathlib import Path

lines = Path('AoC2022/day6/data.txt').read_text()

def find_first_marker(n_char):
    first_marker_idx = 0
    for line in lines.split('\n'):
        i = 0
        while i < len(line):
            batch = line[i:i+n_char]
            if len(batch) == len(set(batch)):
                first_marker_idx = i + n_char
                break
            i += 1
            if i == (len(line) - 3):
                break

    print(first_marker_idx)

# Part 1
find_first_marker(4)
# Part 2
find_first_marker(14)