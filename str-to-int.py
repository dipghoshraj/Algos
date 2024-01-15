

def str_to_int(s):

    def clamp32bit(val):
        min_value = -2**31
        max_value = 2**31 - 1

        return min_value if val < min_value else ( max_value if val > max_value else val )
        


    val = s.strip()
    int_val = ''

    for i in val:
        if i == '-':
            int_val += str(i) 
        if i.isdigit():
            int_val += str(i)
        if i not in ['+', '-'] and not i.isdigit(): break
        

    return clamp32bit(int_val)



   


if __name__ == '__main__':

    x = "+-912.83472332"
    print(str_to_int(x))