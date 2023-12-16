def calculate_percentage_equal(winner, array2, array3):
    total = len(winner)
    normal_length = len(winner)
    equal_count = 0
    print("before: ", normal_length)
    for x, y, z in zip(winner, array2, array3):
        if x == y == z:
            equal_count += 1
        elif y == '0' or z == '0':
            normal_length -= 1
    print("after: ", total - normal_length)
    percentage_equal = (equal_count / normal_length) * 100
    return percentage_equal




def calculate_percentage_equal_og(winner, array2):
    total = len(winner)
    normal_length = len(winner)
    equal_count = 0
    print("before: ", normal_length)
    for x, y in zip(winner, array2):
        if x == y:  
            equal_count += 1
        elif y == '0':
             normal_length -= 1
    print("after: ", total - normal_length)
    percentage_equal = (equal_count / normal_length) * 100
    return percentage_equal
