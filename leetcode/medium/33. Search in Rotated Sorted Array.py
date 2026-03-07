class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        if target >= nums[0]:
            left_bound = 0
            right_bound = left - 1 if left > 0 else len(nums) - 1
        else:
            left_bound = left
            right_bound = len(nums) - 1
            
        while left_bound < right_bound:
            mid = (left_bound + right_bound) // 2
            if nums[mid] >= target:
                right_bound = mid
            else:
                left_bound = mid + 1
        
        return left_bound if nums[left_bound] == target else -1