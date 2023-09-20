def majority(nums):

    hashmap ={}
    highest = [0, 0]

    for i in nums:
        if hashmap.get(i):
            hashmap[i] += 1
        else:
            hashmap[i] = 1
        print(hashmap.get(i))
        highest = [i, hashmap.get(i)] if hashmap.get(i) > highest[1] else highest

    return highest[0]


if __name__ == "__main__":
    nums =[6,5,5]
    print(majority(nums))

