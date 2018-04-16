#复杂度为O(N^2)
class Solution(object):
    def twoSum(self, nums, target):
        ri = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if target == nums[i] + nums [j]:
                    ri.append(i)
                    ri.append(j)
        return ri





#复杂度为O(Nlog(N))
class Solution(object):
    def twoSum(self, nums, target):
        hash_tab={}
        for ids,value in enumerate(nums):
            hash_tab[value] = ids
        for ids,value in enumerate(nums):
            dvalue = target - value
            if dvalue in hash_tab.keys():
                if ids < hash_tab[dvalue]:
                    return [ids,hash_tab[dvalue]]
