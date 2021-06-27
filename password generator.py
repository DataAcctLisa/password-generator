# password generator that generates passwords for 9 characters (which covers the "at least 8 rule")
# that also includes numbers and special characters


import random
a = random.randint(1, 1000)
myList1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r','s','t','u','v','w','x','y','z']
b = random.choice(myList1)
c = random.choice(myList1)
d = random.choice(myList1)
e = random.choice(myList1)
f = random.choice(myList1)
g = random.choice(myList1)
h = random.randint(1, 1000)
myList2 = ['!', '@', '#', '$', '%', '^', '&', '*']
i = random.choice(myList2)

print(a)
print(b)
print(c)
print(d)
print(str(a)+b+c+d+e+f+g+str(h)+i)