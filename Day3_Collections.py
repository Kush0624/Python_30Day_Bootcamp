# 1️⃣ Create a list of 5 cities. Add a new city at the second position.

cities=["agra","delhi","mumbai","lucknow","banglore"]
# print(cities)
cities.insert(1,"hyderabad")
print(cities)

# 2️⃣ Remove the last city from the list.
cities.pop()
print(cities)

# 3️⃣ Create a tuple of your birth date (day, month, year) and print it.

birth_date=(24,6,2003)
# print(birth_date)

# 4️⃣ Create a set of numbers {1, 2, 3, 4, 4, 5} and show that duplicates are removed.

data={1,2,3,4,4,5}
# print(data)

# 5️⃣ Find common numbers between {10, 20, 30, 40} and {30, 40, 50, 60}.

set1={10, 20, 30, 40}
set2={30, 40, 50, 60}
# print(set1.intersection(set2))


# 🎯 Mini-Task

# Write a Python script that:

# Takes two lists from the user.

# Removes duplicates from both.

# Prints elements common in both lists.

list1=input("enter list1 values with spaces").split()
list2=input("enter list2 values with spaces").split()

set1=set(list1)
set2=set(list2)
print(set1)
print(set2)
print(set1.intersection(set2))