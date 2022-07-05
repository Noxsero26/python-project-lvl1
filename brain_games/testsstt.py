from random import randint
s = []
result = ''
step = randint(2, 5)
a = randint(10, 15)
b = randint(60, 65)
print(a)
print(b)
print(step)
n = range(a, b, step)
for i in n:
    s.append(i)
k = s
random_position = randint(0, 5)
b = s[random_position]
s[random_position] = '..'
t =' '.join(map(str,s))
t = t[0:28]
print(t,b)
