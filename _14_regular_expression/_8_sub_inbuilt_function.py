import re

mobile_no = "913-789 8948" # 9137898948
res = re.sub("\D","",mobile_no)
print(res)