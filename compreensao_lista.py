# list comprehention

x = [1,2,3,4,5]
y = []

for i in x:
	y.append(i**2)

print(x)
print(y)

z = [1,2,3,4,5,6,7,8,9,10]
k = [i**2 for i in z ]
a = [i for i in z if i%2 == 1]
print(z)
print(k)
print(a)

