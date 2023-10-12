# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """
#
#    def length(self):
#        """
#        :rtype int
#        """

class Solution(object):

    def findInMountainArray(self, target, mountain_arr):
        size = mountain_arr.length()
        start = 0
        end = size-1
        while start<=end:
            middle = (start+end)/2
            if mountain_arr.get(middle) > mountain_arr.get(middle+1): end = middle-1
            else: start = middle+1
        
        start = 0
        end = middle
        while start<=end:
            middle = (start+end)/2
            value = mountain_arr.get(middle)
            if value == target:
                return middle
            elif value > target: end = middle-1
            else: start = middle+1
        start = middle
        end = size-1
        while start <= end:
            middle = (start+end)/2
            value = mountain_arr.get(middle)
            if value == target:
                return middle
            elif value > target: start = middle+1
            else: end = middle-1
        return -1

        """
        :type target: integer
        :type mountain_arr: MountainArray
        :rtype: integer
        """
        