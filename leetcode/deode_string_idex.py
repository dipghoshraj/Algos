
def decodestr(s):

    """
    
    """

    stack = []
    size =0 

    for char in s:
        if char.isdigit():
            size *= int(char)
        else:
            size += 1

    # Start from the end of the encoded string
    for char in reversed(s):
        k %= size
        if k == 0 and char.isalpha():
            return char
        
        if char.isdigit():
            size //= int(char)
        else:
            size -= 1


if __name__ == "__main__":
    x = decodestr("leet2code3")
    print(x)
