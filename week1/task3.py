A = float(input())
integer = int(A)      
fractional= int(round((A - integer) * 100)) 
new_number = fractional + integer / 100
print(new_number)