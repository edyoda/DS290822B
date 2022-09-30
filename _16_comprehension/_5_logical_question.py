# Given numbers=range(20), produce a list containing the word ‘even’ 
# if the number in the numbers is even, and the word ‘odd’ if the number is odd. 
# Result would look like ‘odd’,’odd’,’even’…



result = ["even" if n%2 == 0 else "odd" for n in range(20)]
print(result)

