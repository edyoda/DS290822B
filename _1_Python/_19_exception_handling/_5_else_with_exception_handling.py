try:
    print(10/5)
except (ZeroDivisionError,TypeError) as ex:
    print(ex)
else:
    print("Else part")

# when there is no exception raised then else part will get executed