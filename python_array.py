fruits = ['apple', 'banana', 'cherry']

print(fruits)

fruits.append("blueberry")
print(f"Append print - {fruits}")


fruits.insert(2,"flask")
print(f" Insert Print -  {fruits}")

fruits.remove("flask")
print(f"Remove print - {fruits}")

cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(f"Extend print - {fruits}")


print(f"Index function - {fruits.index('banana')}") 
