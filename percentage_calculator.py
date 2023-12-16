def calculate_percentage_equal(winner, array2):
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
