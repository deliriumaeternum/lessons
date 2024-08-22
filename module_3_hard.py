
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)

def calculate_structure_sum(data_structure):
    sum = 0
    if isinstance(data_structure, (int, float)):
        sum += data_structure
    elif isinstance(data_structure, str):
        sum += len(data_structure)
    elif isinstance(data_structure, dict):
        for k, v in data_structure.items():
            sum += calculate_structure_sum(k)
            sum += calculate_structure_sum(v)
    elif isinstance(data_structure, (tuple, list, set)):
        for s in data_structure:
            sum += calculate_structure_sum(s)
    return sum

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
