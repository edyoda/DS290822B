from msilib.schema import ODBCDataSource


no = int(input("Enter a number to check if is +ve or -ve : "))

if no > 0:
    print("+ve no.")
elif no == 0:
    print("neutal no.")
else:
    print("-ve no.")


