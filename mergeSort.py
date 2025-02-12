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


def mergeSortAD(list, sort: bool):
    sortType = sort
    if sortType == True:
        result = mergeSortAscending(list)
        return result
    elif sortType == False:
        result = mergeSortDescending(list)
        return result
    else:
        print("Please Input either 1 for Ascending Sort or 0 for Descending Sort")


l = [1 , 6, 32, 5, 12, 553, 132221, 33, 2, 4]
print(mergeSortDescending(l))
print(mergeSortAscending(l))

print(mergeSortAD(l, True))
print(mergeSortAD(l, False))

