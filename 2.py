def anagram(s1,s2):

    if sorted(s1) == sorted(s2):
        print(True)
    else:
        print(False)

anagram("dream","maerd")