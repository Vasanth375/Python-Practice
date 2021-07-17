nums = [1,1,2,6]
count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]==nums[j]):
            count=count+1
print(count)
