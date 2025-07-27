ab = [2, 5, [1, 4, 6, [4, 4, 3], 7, 0], 9, 2]

ba =[]
result = ab.copy()

while result :
    i = result.pop(0)
    if isinstance(i,list):
        result = i + result
    else:
        ba.append(i)
print(ba)

