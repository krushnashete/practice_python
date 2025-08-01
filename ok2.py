s = "i love programming"
res = s.split(" ")

for i in range(len(res)):
    word = res[i]
    word2 = word[0].upper()
    new_word = word2 + word[1:]
    res[i] = new_word

final_str = " ".join(res)

print(final_str)