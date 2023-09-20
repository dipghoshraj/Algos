
class Solution:

    def sol(self, x, y):
        merged = x+y
        sorted_array = self.quciksort(merged)
        if len(sorted_array) % 2 == 0:
            median = len(sorted_array) // 2
            sum_val = (sorted_array[median] + sorted_array[median -1]) /2
            return sum_val
        else:
            median = len(sorted_array) // 2
            return (sorted_array[median])

    def quciksort(self, arr):

        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr)//2]
        arr.remove(pivot)
        left, right = [], []

        for i in arr:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
        return self.quciksort(left) + [pivot] + self.quciksort(right)

print(Solution().sol([1,3, 4, 2, 0], [4,9.2]))