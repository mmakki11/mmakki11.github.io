# Source: index.html link "Max Num" (pythontutor.com)
nums = [1,4,10,6,5,42,9,8,12] 

maxNum = 0
for n in nums:
    if n > maxNum:
        maxNum = n
print('The max is', maxNum)
