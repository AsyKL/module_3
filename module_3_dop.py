summ = 0
def calculate_structure_sum(*args):
    global summ
    for i in args:
        if isinstance(i, int):
            summ += i
        elif isinstance(i, str):
            summ += len(i)
        elif isinstance(i, list):
            calculate_structure_sum(*i)
        elif isinstance(i, dict):
            for k in i:
                key = (k, i[k])
                calculate_structure_sum(*key)
        elif isinstance(i, tuple):
            calculate_structure_sum(*i)
        elif isinstance(i, set):
            calculate_structure_sum(*i)
    return (summ)
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)

