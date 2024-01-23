from pathlib import Path

lines = Path('AoC2022/day4/data.txt').read_text().rsplit('\n')

def elf_tasks(elf):
    # return range of elf's tasks, e.g [2,3,4]
    return [id for id in range(int(elf[:elf.index('-')]), int(elf[elf.index('-')+1:]) +1)]

fully_overlapping_pairs_part1 = 0
fully_overlapping_pairs_part2 = 0
for line in lines:
    first_elf = line[:line.index(",")]
    second_elf = line[line.index(",")+1:]
    first_elf_tasks = elf_tasks(first_elf)
    second_elf_tasks = elf_tasks(second_elf)
    if all(item in first_elf_tasks for item in second_elf_tasks) or all(item in second_elf_tasks for item in first_elf_tasks):
        fully_overlapping_pairs_part1 = fully_overlapping_pairs_part1 + 1
    
    if any(item in first_elf_tasks for item in second_elf_tasks) or any(item in second_elf_tasks for item in first_elf_tasks):
        fully_overlapping_pairs_part2 = fully_overlapping_pairs_part2 + 1

print(f"Part 1: {fully_overlapping_pairs_part1}")
print(f"Part 2: {fully_overlapping_pairs_part2}")