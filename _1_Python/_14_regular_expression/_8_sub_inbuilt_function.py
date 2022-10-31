import re

mobile_no = "913-789 8948" # 9137898948
res = re.sub("\D","",mobile_no)
print(res)

# data = "1800 0002 2020" # 18 2 22

import re

# Q-01
data = "1800 0002 2020"
sub_meth = re.sub('0','',data)
print(sub_meth)





