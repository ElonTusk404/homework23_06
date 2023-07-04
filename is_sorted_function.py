def is_sorted(onelist):
    for i in range(len(onelist)-1):
        if onelist[i] > onelist[i+1]:
            return False
    return True