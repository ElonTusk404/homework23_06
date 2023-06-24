def merge(list1, list2):
    result = list1 + list2
    for i in range(len(result)):
        for j in range(len(result) - 1):
            if result[j] > result[j+1]:
                result[j], result[j+1] = result[j+1], result[j]
    return result
test1 = [1, 5, 6, 9, 12, 2, 4, 7]
test2 = [5, 11, 223, 456, 1823]
itog = merge(test1, test2)
print(itog)
