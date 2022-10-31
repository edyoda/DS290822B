# 5! = 5*4*3*2*1


no = int(input("Enter your number : "))

fact = 1
for i in range(1,no+1):
    fact *= i  # fact = fact * i # fact = 1 * 1 = 1 * 2 = 2 * 3 = 6 * 4 = 24 * 5 = 120
    
print("Factorial : ",fact)