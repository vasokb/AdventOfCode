import pathlib

lines = pathlib.Path(r'C:\Users\vasileia.kampouraki\Python code\Main\applications\cnn_lane_boundary_visualizer\advent22\day4\data.txt').read_text().rsplit('\n')

# print(lines)

def elf_tasks(elf):
    # return range of elf's tasks, e.g [2,3,4]
    return [id for id in range(int(elf[:elf.index('-')]), int(elf[elf.index('-')+1:]) +1)]

fully_overlapping_pairs = 0
for line in lines:
    first_elf = line[:line.index(",")]
    second_elf = line[line.index(",")+1:]
    first_elf_tasks = elf_tasks(first_elf)
    second_elf_tasks = elf_tasks(second_elf)
    if all(item in first_elf_tasks for item in second_elf_tasks) or all(item in second_elf_tasks for item in first_elf_tasks):
        fully_overlapping_pairs = fully_overlapping_pairs + 1

print(fully_overlapping_pairs)


###### part 2 #####

fully_overlapping_pairs = 0
for line in lines:
    first_elf = line[:line.index(",")]
    second_elf = line[line.index(",")+1:]
    first_elf_tasks = elf_tasks(first_elf)
    second_elf_tasks = elf_tasks(second_elf)
    if any(item in first_elf_tasks for item in second_elf_tasks) or any(item in second_elf_tasks for item in first_elf_tasks):
        fully_overlapping_pairs = fully_overlapping_pairs + 1

print(fully_overlapping_pairs)

