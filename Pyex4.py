# # ex1
import random
answers = [
    "It is certain", "It is decidedly so", "Without a doubt",
    "Yes, definitely", "You may rely on it", "As I see it, yes",
    "Most likely", "Outlook good", "Yes", "Signs point to yes",
    "Reply hazy try again", "Ask again later", "Better not tell you now",
    "Cannot predict now", "Concentrate and ask again", "Don't count on it",
    "My reply is no", "My sources say no", "Outlook not so good",
    "Very doubtful"
]
input("Ask the magic 8-ball a question: ")
print(random.choice(answers))
# # ex2
queue = []
while True:
    user_input = input("Enter something (or ? to pop, Enter to quit): ")
    if user_input == "":
        print("Program ended.")
        break
    if user_input == "?":
        if len(queue) > 0:
            item = queue.pop(0)
            print("Popped:", item)
        else:
            print("Queue is empty!")
    else:
        queue.append(user_input)
        print(f"Added '{user_input}' to queue.")
        
# ex3
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
        
fib(1000)
# ex4
def counting_number(sub, text):
    count = text.count(sub)
    return count

def remove_duplicates(sub, text):
    return text.replace(sub, "")
print(counting_number("an", "banan"))   
print(remove_duplicates("an", "banan")) 

# ex5
def is_palindrome(s):
    return "Yes" if s == s[::-1] else "No"

print(is_palindrome("malayalam"))  
print(is_palindrome("geeks"))
print(is_palindrome("ehab"))      

# ex6
def largest_number(nums):
    return max(nums)
numbers = [3, 5, 2, 8, 1]
print(largest_number(numbers))