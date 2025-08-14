# 1.Create a string "Python is powerful" and print:
# First 6 characters

# Last 6 characters

# Reverse the string
string1 = "Python is powerful"
# print(string1[:6])
# print(string1[-6:])
# print(string1[::-1])


# 2️⃣ Count how many vowels are in "I love AI and Python"

string2 = "I love AI and Python"
vowels = "aeiouAEIOU"
count = sum(1 for char in string2 if char in vowels)
# print(count)

# 3. Replace "Python" with "NVIDIA" in "I love Python"

str="I love Python"
# print(str.replace("Python","Nvidia"))

# 4.Check if "deep" is present in "deep learning with Python"

str="deep learning with python"
# print("deep" in str)

# 5️⃣ Create a formatted string:
# "My name is <your name>, I am <your age> years old, and I earn ₹<your income> per month."

name="Kushagra"
age=22
income=50000
# print(f"My name is {name}, I am {age} years old, and I earn ${income} per month. ")


# 🎯 Mini-Task

# Write a Python script that:

# Takes a sentence from the user.

# Prints it in uppercase, lowercase, reverse order, and without spaces.

sentence=input("Enter any sentence:")
print(sentence.upper())
print(sentence.lower())
print(sentence[::-1])
print(sentence.replace(" ",""))
