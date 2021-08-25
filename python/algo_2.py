''' Write an algorithm to raise power of any value to any value'''

"""
begin
define base
define power
Recursion condition power = 0,
   base = base * base
Next
write base
end
"""

def to_power(base, power):
    if power > 0:
        return base * to_power(base, power-1)
    elif power == 0:
        return 1
    elif power < 0:
        power =  abs(power)
        return 1/ (base * to_power(base, power-1))


base = int(input('Base value :: '))
power = int(input('Power value :: '))

to_power_value = to_power(base, power)

print(f'Exponent value is :: {to_power_value}')