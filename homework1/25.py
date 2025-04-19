numbers = list(range(1, 11))
#filter to get even numbers only
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
#double each even number
doubled_numbers = list(map(lambda x: x * 2, even_numbers))
#square each doubled number
squared_evens = [x**2 for x in doubled_numbers]
#sort in descending order
sorted_squares = sorted(squared_evens, key=lambda x: -x)
#print
print("Original numbers:", numbers)
print("Even numbers:", even_numbers)
print("Doubled even numbers:", doubled_numbers)
print("Squared doubled even numbers:", squared_evens)
print("Sorted in descending order:", sorted_squares)

