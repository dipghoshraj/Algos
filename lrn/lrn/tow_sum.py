def twoSum(nums,  target ):

    for idx, n in enumerate(nums):
        n_arr = nums[idx+1:]
        print(n_arr)
        for jdx, j in enumerate(n_arr):
            sum = j + n
            if sum == target:
                nex_index = jdx
                return [idx, nex_index+(idx +1)]

nums = [2,7,11,15]
target = 9
print(twoSum(nums,  target ))