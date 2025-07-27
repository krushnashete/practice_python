s = "aeiou is having 5 vowel"

d = sorted(s)
count = 0
for char in (d):
    if char == 'a':
        count += 1
    elif char == 'e':
        count += 1
    elif char == 'i':
        count += 1
    elif char == "o":
        count += 1
    elif char == "u":
        count += 1
    else:
        continue
print(count)
