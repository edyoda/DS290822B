# Logical Operator
# and - if all the conditions are true than only it will return True else False
# or - if atleast one condition is true than only it will return True else False
# not - it will return True for False and will return False for True

no1 = 30
no2 = 40

and_demo = no1 == no2 and no1 > 5
print("And : ",and_demo)

or_demo = no1 == no2 or no1 > 5 
print("Or : ",or_demo)

not_demo = not(no1 != no2) # not(True) = False
print("Not : ",not_demo)