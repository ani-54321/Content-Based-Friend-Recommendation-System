def same_values(l1, l2, case=False):
    commons = []
    if l1 is not None:
        for elem in l1:
            if elem in l2 and not case:
                commons.append(elem)
            elif str(elem).lower() in str(l2).lower() and case:
                commons.append(elem)
    else:
        commons = l2
    
    return commons

def different_values(l1, l2, case=False):
    differents = []
    if l1 is not None:
        for elem in l1:
            if elem not in l2 and not case:
                differents.append(elem)
            elif str(elem).lower() not in str(l2).lower() and case:
                differents.append(elem)
    else:
        differents = l2
    
    return differents


# l1 = ["anish", 10, 20, "shaha"]
# l2 = ["SHAHA", "10", 23, "abc"]

# # print(str(l2).lower())

# print(same_values(l1, l2, False))
# print(different_values(l1, l2, True))

# We have no built in function for comparing lists in python. It can cause troubles and can divert from the main aim of programming. This is my personal experience