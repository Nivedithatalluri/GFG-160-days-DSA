class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        if len(arr)<2:
            return -1
        unique_arr=list(set(arr))
        if len(unique_arr)<2:
            return -1
        unique_arr.sort()
        return unique_arr[-2]
