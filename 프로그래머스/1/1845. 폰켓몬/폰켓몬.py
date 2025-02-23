def solution(nums):
    s = len(set(nums))
    
    if s > (len(nums) // 2):
        return len(nums) // 2
    
    return s