#ex1
t= ("apple", "banana", "cherry", "date")
print(t[0])
print(t[-1])
print(t[1:3])

#ex2
t1=(1,2,3,4)
t2=(2,3,2,1)
t3=t1+t2
t4= tuple([x * y for x, y in zip(t1, t2)])
print(t3)
print(t4)

# ex3
t=(10, 20, 30, 40, 50)
new_t= t[:0] + ('a','b') + t[1:]
print(new_t)      
print(t)
print(t.count(20))
print(t.index(40))