from lib2to3.pytree import LeafPattern
import re
email = input('please enter your mail id : ')
res = re.compile("^[A-z][a-zA-Z0-9._]+[@][a-z]+[.][a-z]+$")
result = res.search(email)
print(result)

if res:
    print('entered mail is correct')
else:
    print('try again')

8, 16 -> {8,16}
1. upper letter
2. lower letter 
3. digit 
4. special character