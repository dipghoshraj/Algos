def trap(height):

    ngl, ngr = [], []
    area = 0
    reversed_height = height.copy()
    reversed_height.reverse()

    ngl = [ max(height[:i]) if height[:i] else 0 for i in range(len(height))] 
    ngr = [ max(reversed_height[:i]) if reversed_height[:i] else 0 for i in range(len(reversed_height))] 
    ngr.reverse()
    


    for i in range(len(height)):
        a = min(ngl[i], ngr[i]) - height[i]
        if a > 0:
            area += a 


    return area

 
if __name__ == '__main__':
    water = [0,1,0,2,1,0,1,3,2,1,2,1]
    water.count(0)
    print(trap(water))