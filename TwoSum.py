class Solutiom:
    def two_sum(self, nums, target):
        store = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in store:
                return [store[diff], i]
            store[num] = i
        return None