from itertools import accumulate
op_lst = []
numbers = [0, 10, 10, 0]
query = [[1, 2, 5], [2, 4, 10]]
zer_idx = [0]*len(numbers)
cnt = 0
for i, j in enumerate(numbers,0):
    if j == 0:
        cnt += 1
        zer_idx[i] = cnt
    else:
        zer_idx[i] = cnt
zer_idx = [0] + zer_idx
numbers = [0] + list(accumulate(numbers, lambda a,b : a+b))
print(zer_idx)
for rec in query:
    val = numbers[rec[1]] - numbers[rec[0]-1] + rec[2]*(zer_idx[rec[1]] - zer_idx[rec[0]-1])
    op_lst.append(val)
print(op_lst)
