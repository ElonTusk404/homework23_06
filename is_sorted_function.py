def is_sorted(onelist):
    for i in range(1, len(onelist)):
        if onelist[i] < onelist[i+1]:
            return False
    return True