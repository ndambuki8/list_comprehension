#Uncomprehended code
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)




#List comprehension for squares
squares = [value**2 for value in range(1,11)]
print(squares)

#List comprehension for addition, specifically even numbers

even = [value for value in range(0,12,2)]
print(even)

#List comprehension for addition, specifically even numbers
odd = [value for value in range(1,12,2)]
print(odd)
