a = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
widthh =  4
new = ""
for i in range(len(a)):
    new += a[i]
    if (i+1) % widthh == 0:
        new += "\n"
print(new)



