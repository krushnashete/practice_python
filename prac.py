# mylist = [2,4,8,9]
# mylist2 = ["j","k","j","jkd"]
# mylist.append(mylist2)
# print(mylist)


# mylist = [2,4,8,9]
# mylist2 = ["j","k","j","jkd"]
# mylist.extend(mylist2)
# print(mylist)
def print_all_lists(lst):
    for item in lst:
        if isinstance(item, list):
            print(item)
            print_all_lists(item)  # Recursively go deeper if item is also a list

# Test data
nested_list = [1,6,[2,5,[1,4,6,[4,4,3],7,0],9,2],5,0]

print_all_lists(nested_list)


ak = [2,3,4,2,1,3,4,4555,2]
for i in ak:
    if isinstance(i, int):
       print(True)