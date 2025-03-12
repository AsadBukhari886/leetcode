
def maximumCount(nums):
    negative = 0
    positive = 0
    for x in range(len(nums)):
        if nums[x] < 0:
         negative += 1
        if nums[x] > 0:
         positive += 1
    print(max(positive, negative))
maximumCount([-2,-3,0,3,3,4,0,1])