from pathlib import Path

lines = Path('AoC2022/day3/data.txt').read_text()

def find_seq_length(text):
    return len(text)

## item prioity 
def item_type_priority(item):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    if item.islower():
        priority = alphabet.index(item) + 1
    else:
        priority = list(map(lambda x: x.upper(), alphabet)).index(item.upper()) + 1 + 26
    return priority

sum_item = 0
for item in lines.rsplit('\n'):
    len_item = find_seq_length(item)
    first_comp = item[0:len_item // 2]
    second_comp = item[len_item // 2:]
    common_comp = list(set(first_comp)&set(second_comp))
    item_priority = item_type_priority(common_comp[0])
    sum_item = sum_item + item_priority

print(f"Part 1: {sum_item}")


# Part 2
sum_item = 0 
items = lines.rsplit('\n')

i = 0
while i< len(items):
    group_badge = list(set(items[i])&set(items[i+1])&set(items[i+2]))
    item_priority = item_type_priority(group_badge[0])
    sum_item = sum_item + item_priority
    i += 3
    if i == (len(lines)):
        break
print(f"Part 2: {sum_item}")

