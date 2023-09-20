

def areamax(height):

    maxarea = 0

    for i in range(len(height)):
        for j in range(i+1, len(height)):
            area = min(height[i], height[j]) * (j - i)
            maxarea = max(area, maxarea) 
    return maxarea

def areamaxtwopointer(height):

    maxarea = 0
    left, right = 0, len(height)-1

    while left <= right:
        area = min(height[left], height[right]) * (right- left)
        if height[left]<=height[right]:
            left += 1
        else:
            right -= 1
        maxarea = max(area, maxarea)
    return  maxarea
        


if __name__ == '__main__':
    s= [1,8,6,2,5,4,8,3,7]
    # s= [1,1]
    print(areamaxtwopointer(s))
