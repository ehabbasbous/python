#The first example
#create a function called shift _array that takes an array as an argument
#Check if the length of this array is 0 so that means the list is empty
#I need to return a msg
#create a variable that saves the last index in this array
#remove the last index with pop()
#insert the var we created in the first index
#return the list

def shift_array(X):
    if len(X) == 0:
        return "The list is empty"
    last_number = X[-1]
    X.pop()
    X.insert(0, last_number)
    return X
X= [2,1,6,4,-7]
print(shift_array(X))

#when we start the function 
#if the length is 0 then it will return "The list is empty"
#created var last_number = last index in the array
#removed the current last one by using X.pop()
#insert it to the first index X.insert(0, last_number)
#return the array
#it will print [-7, 2, 1, 6, 4]

#The second example
#create a function remove_negatives that takes a list as an argument
#if the list is empty, return empty list
#we need to check if the first index is negative
#if it is negative, we remove it by using pop(0)
#we call the function again with the updated list
#if it is not negative, we keep it and call the function with the rest of the list
# then we return the new list
# the last step is to print the function with the list we want to remove negatives from

def remove_negatives(X):
    if len(X) == 0:
        return []
    if X[0] < 0:
        X.pop(0)
        return remove_negatives(X)
    else:
        return [X[0]] + remove_negatives(X[1:])
print(remove_negatives([1,-2,4,1]))

#run the function
#if the length is 0 then return []
#check if the first index is negative
#if it is negative then remove it by using X.pop(0)
#call the function again with the updated list
#if it is not negative then keep it and call the function with the rest of the list
#it will print [1, 4, 1]

#The third example
#create a function longest_word that takes a string as an argument
#split the string into words in array
#create a variable as empty string to compair the words with it
#create input to take string from user
#loop through the array
#compair the length of the word with the length of the created var
#if the word is bigger, we store the word in the var
#return the var

def longest_word(text):
    words = text.split()
    the_long_word = ""
    for i in words:
        if len(i) > len(the_long_word):
            the_long_word = i
    return the_long_word
#we can write it without print to take input from user
#print(longest_word("The quick brown fox jumped over the lazy dog everyday"))
user_text = input("Enter a sentence: ")
print(longest_word(user_text))

#run the function
#enter a sentence: I am Ehab jr
#split the text like this "I am Ehab jr " => ["I", "am", "Ehab", "jr"]
#var the_long_word = "" will be created
#loop:
#1- i = 0 => if len("I") > len("") => the_long_word = "I"
#2- i = 1 => if len("am") > len("I") => the_long_word = "am"
#3- i = 2 => if len("Ehab") > len("am") => the_long_word = "Ehab"
#4- i = 3 => if len("jr") > len("Ehab") => nothing => the_long_word = "Ehab"
#return the the_long_word = "Ehab"  
#it will print Ehab

# Exercise 4: largest number in each list
# create a function that takes a list of lists as an argument name it largest_in_sublists
# create an empty list to store the largest numbers
# loop through each sublist
# find the largest number in each sublist using max()
# append the largest number to the new list
# return the new list
#print(largest_in_sublists([[13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]])

def largest_in_sublists(lst):
    largest_numbers = []
    for sublist in lst:
        largest_numbers.append(max(sublist))
    return largest_numbers
print(largest_in_sublists([[13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]))

# run the function
# create an empty list largest_numbers = [] 
# loop through each sublist in the main list
# find the max in each sublist using max() and append it to largest_numbers
# return largest_numbers
# Output: [27, 39, 1001]

# Exercise 5: Title Case a String
# create a function that takes a string as an argument name it titleCase()
# split the string into words
# capitalize the first letter of each word using word.capitalize() using a loop or list comprehension
# join the words back into a single string
# return the title-cased string
def titleCase(text):
    words = text.split()
    title_cased_words = [word.capitalize() for word in words]
    return ' '.join(title_cased_words)
print(titleCase("hello world i am ehab"))

# run the function
# split the string into words
# capitalize first letter using word.capitalize() and join them back
# it will print "Hello World I Am Ehab"

