
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    
    for i in range(0,len(nums)) :   
        output = list()
        output.append(i)
        for j in range(i+1,len(nums)) : 
            if nums[i] + nums[j] == target : 
                output.append(j)
                return output
        

