def find_duplicate(nums):
    i = nums[0]
    j = nums[0]
    
    while True:
       i = nums[i]  
       j = nums[nums[j]]   
       if i == j:
            break 

   
    i = nums[0] 
    while i != j:
        i = nums[i]  
        j = nums[j]        

    return j 
input_array = [1, 3, 4, 2, 2]
duplicate = find_duplicate(input_array)
print("Duplicate number is:",duplicate)  
