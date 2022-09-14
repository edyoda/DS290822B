no = 678 # 876



mul = 0

while no != 0:
    mod = no % 10        # 8            | 7               | 6
    mul = mul * 10 + mod # 0 + 8 = 8    | 80 + 7 = 87     | 870 + 6 = 876
    no  = no // 10       # 67           | 6               | 0
    
print(mul)