def removeElement(nums, val):
    length = 0
    
    for index in nums[:]: 
        if index != val:
            nums[length] = nums[index]
            length += 1
    return length