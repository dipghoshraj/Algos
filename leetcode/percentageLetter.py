def percentageLetter(s: str, letter: str) -> int:
    """
    
    """

    length = len(s)
    counter = s.count(letter)
    persent = (counter/length) *100

    return int(persent)



if __name__ == '__main__':
    s = "foobar"
    letter = "o"
    y = percentageLetter(s, letter)
    print(y)
