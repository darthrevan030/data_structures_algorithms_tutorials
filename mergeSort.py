def mergeSortDescending(list):
    if len(list) <= 1:
        return list
    
    mid = len(list) // 2
    leftHalf = list[:mid]
    rightHalf = list[mid:]

    left = mergeSortDescending(leftHalf)
    right = mergeSortDescending(rightHalf)

    return mergeDescending(left, right)

def mergeDescending(left, right):
    newList = []

    while left and right:
        if left[0] > right[0]:
            newList.append(left[0])
            left.pop(0)
        else:
            newList.append(right[0])
            right.pop(0)
    
    if left:
        newList.extend(left)
    else:
        newList.extend(right)
    
    return newList


def mergeSortAscending(list):
    if len(list) <= 1:
        return list
    
    mid = len(list) // 2
    leftHalf = list[:mid]
    rightHalf = list[mid:]

    left = mergeSortAscending(leftHalf)
    right = mergeSortAscending(rightHalf)

    return mergeAscending(left, right)


def mergeAscending(left, right):
    newList = []
    
    while left and right:
        if left[0] < right[0]:
            newList.append(left[0])
            left.pop(0)
        else:
            newList.append(right[0])
            right.pop(0)
    
    if left:
        newList.extend(left)
    else:
        newList.extend(right)
    
    return newList


l = [1 , 6, 32, 5, 12, 553, 132221, 33, 2, 4]
print(mergeSortDescending(l))
print(mergeSortAscending(l))
