

def substring(x):

    i, j = 0,0
    uniq_vals = []
    m = 0

    while i < len(x):
        if x[i] in uniq_vals:
            j = uniq_vals.index(x[i]) + 1
            uniq_vals.append(x[i])
            uniq_vals = uniq_vals[j:]
        else:
            uniq_vals.append(x[i])

        m = max( m, len(uniq_vals) )
        i += 1
    print(uniq_vals, i, j)
    return m            

if __name__ == '__main__':
    s=  ' '
    # s=  'pwwkew'
    # s=  'bbbbb'
    print(substring(s))

