

def all_subStings(string):

    '''`all_subStings'''

    sub = []

    for i in range(len(string)):
        for j in range(i+1, len(string)+1 ):
            ns = string[i:j]
            # print(ns, i, j)
            sub.append(ns)
    
    return sub

def find_palindrom(string):

    all_sub = all_subStings(string)

    maxm = 0
    lss = ''

    for i in all_sub:
        if i == i[::-1]:
            maxm, lss =  [len(i), i] if len(i) > maxm else [maxm, lss]
    return lss

if __name__ == '__main__':
    s = 'cbbd'
    print(find_palindrom(s))