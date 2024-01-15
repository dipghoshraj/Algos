def findDuplicate(nums):
        hashmap = {}

        for i in nums:
            if hashmap.get(i):
                return i
            hashmap[i] = 1
        return 0

if __name__ == '__main__':
     nums = [1,3,4,2,2]
     print(findDuplicate(nums))