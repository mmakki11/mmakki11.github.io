# Source: index.html link "Nums &amp; While" (pythontutor.com)
#Spring 2012 Final Exam, #8

nums = [1,4,0,6,5,2,9,8,12] 
print(nums)
i=0
while i < len(nums)-1:
    if nums[i] < nums[i+1]:
        nums[i], nums[i+1] = nums[i+1], nums[i]
    i=i+1 
        
print(nums)

