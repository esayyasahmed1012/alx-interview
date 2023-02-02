"""
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes
"""



def canUnlockAll(boxes):
    """
    boxes is a list of lists
     A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    """
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
