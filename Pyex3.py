# ex1
def multiply( ):
  for x in range( 1, 11 ):
    result = x * 12
    print( result )
multiply()
# ex2 NUMBER OF COMMON CHARACTERS
def common_characters(str1,str2):
  set1=set (str1)
  set2=set (str2)
  return len(set1 & set2)
word1= input("ENter the first word: ")
word2= input("ENter the second word: ")
result=common_characters(word1,word2)
print("NUMBER OF COMMON CHARACTERS: ", result)
# ex guess number
from random import randint
def guess_number(user_number):
    held_number = randint(1, 10)

    if user_number > held_number:
        return "Too big"
    elif user_number < held_number:
        return "Too small"
    else:
        return "You are SUPER"
user_input = int(input("Enter a number between 1 and 10: "))
result = guess_number(user_input)
print(result)

