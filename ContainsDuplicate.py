class Solution:
    def hasDuplicate(self, nums):
        store = set()
        for i in nums:
            store.add(i)
        print(store)    
        if len(store) < len(nums):
            return True
        elif len(store) == len(nums):
            return False  