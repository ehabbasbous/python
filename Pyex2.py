# check the number
numb =float(input("Enter a number:"))
if numb > 0:
  print("the number is positive.")
elif numb<0:
  print("the number is negative.")
else:
  print("the number is zero")
# or you can use like array to check the number  
numbers =[5, -3,0 ,10 ,-12]
for num in numbers:
  if num>0:
    print(f"{num} is positive")
  elif num <0:
    print(f"{num} is negative")
  else:
    print(f"{num} is zero")  
# loop 1 to 10
for x in range( 1, 11 ):
  print(x)
print( "Done" )

# loop 10 to 1
num = 10
while num >= 1:
    print( num )
    num -= 1
print( "Done" )

# write even number

for y in range( 2, 20,2 ):
  print(y)
print( "Done" ) 
# check number
numbs =float(input("Enter a number:"))
if numbs > 100:
  print("big number.")
elif numbs==0:
  print("the number is zero")
else:
  print("small number")