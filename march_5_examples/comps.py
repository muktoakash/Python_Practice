"""Comprehension examples."""
import time

# Example 1: Lists
# Using a loop
numbers = range(10)
squares = []

for number in numbers:
    squares.append(number * number)

print(squares)

# Using a Comprehension
squares = [number * number for number in numbers]
print(squares)


# Example 2: Sets
# With for loop...
cities = ['toronto', 'Toronto', 'tOronTo', 'montreal', 'Montreal']
unique_cities = set()

for city in cities:
    unique_cities.add(city.capitalize())

print(unique_cities)

# Set comprehensions
unique_cities = {city.capitalize() for city in cities}
print(unique_cities)


# Example 3: Dictionaries
words = ['banana', 'elephant', 'bat']
word_dict = {}


for word in words:
    word_dict[word] = len(word)

print(word_dict)

# Dict comprehensions
word_dict = {word: len(word) for word in words}
print(word_dict)


# Filtering
numbers = range(50)
five_factors = [
    number
    for number in numbers
    if not number % 5
]
print(five_factors)

# Filtering words
cities = ['Toronto', 'Torino', 'Hamilton', 'Tampa', 'Montreal']
t_cities = [city for city in cities if city.startswith('T')]
print(t_cities)

def t_or_h(value):
    return value.startswith('T') or value.startswith('H')


t_or_h_cities = [city for city in cities if t_or_h(city)]
print(t_or_h_cities)

is_t_or_h = [t_or_h(city) for city in cities]
print(is_t_or_h)

# Generator expressions
def square(value):
    time.sleep(0.25)
    return value * value
    
print('Result of generator expression')
print((square(x) for x in range(10)))
print('Result of list comprehension')
print([square(x) for x in range(10)])
