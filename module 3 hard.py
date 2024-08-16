def calculate_sum(add):
    total_sum = 0
    for i in add:
        if isinstance(i, (int, float)):
            total_sum += i
        elif isinstance(i, str):
            total_sum += len(i)
        elif isinstance(i, (list, tuple, set)):
            total_sum += calculate_sum(i)
        elif isinstance(i, dict):
            for key in i:
                if isinstance(key, (int, float)):
                    total_sum += key
                if isinstance(key, str):
                    total_sum += len(key)
            total_sum += calculate_sum(i.values())
        elif isinstance(i, tuple) and isinstance(i[0], tuple):
            total_sum = sum(calculate_sum(i))
    return total_sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])
]
summa = calculate_sum(data_structure)
print(summa)