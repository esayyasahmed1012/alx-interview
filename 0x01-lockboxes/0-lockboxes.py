def canUnlockAll(boxes):
    if type(boxes) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    for i in range(1, len(boxes) - 1):
        boxes_checked = False
        for j in range(len(boxes)):
            boxes_checked = i in boxes[j] and i != j
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True;
