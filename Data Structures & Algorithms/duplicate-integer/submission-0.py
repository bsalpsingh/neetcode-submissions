class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<=1:
            return False
        record={}

        for num in nums:
            if record.get(num) is None:
                record[num]=1
                continue
            record[num]=record[num]+1
        for num in nums:
            if record[num] >1:
                return True
        return False
                      
        