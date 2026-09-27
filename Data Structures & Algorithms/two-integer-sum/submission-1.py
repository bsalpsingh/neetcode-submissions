class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # validate the inputs
        if len(nums)==0 or len(nums)==1:
            raise ValueError("invalid nums list")
        # keep a dict of nums and indexes as key value

        record={}

        for idx,num in enumerate(nums):
            record[num]=idx
        # find the compliment and then loop over each num to see if compliment exist in record
        for idx,num in enumerate(nums):
            compliment=target-num
            if record.get(compliment) is not None and idx!= record[compliment]:
                return [idx,record[compliment]]
        return [0,0]
        
        
        