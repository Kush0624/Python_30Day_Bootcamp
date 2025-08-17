# Write a program to import the random module and print 5 random integers between 1 and 100.

# Write a program that:

# Creates a file notes.txt

# Writes 3 lines into it

# Reads the file and prints its content.

# Write a program that handles exceptions when converting user input into an integer.

# Write a program that tries to open a file that doesn’t exist and handles the error gracefully.

# Create your own module mymath.py with functions add, subtract, multiply, and divide. Import it in another Python file and use the functions.


from random import randint
for i in range(5):
    pass
    # print(randint(1,100),end=",")


# with open("notes.txt","w") as f:
#     f.write("first line\n")
#     f.write("second line\n")
#     f.write("third line")

# with open("notes.txt","r") as f:
#     lines=f.readlines()
#     # print("".join(lines))

import mymath
# print(mymath.add(5,7))

while True:
    str1=input("Enter data and type 'stop' to end:")
    if(str1.lower()=="stop"):
        break
    with open("data.txt","a") as f:
        f.write(str1+"\n")

try:
    with open("data.txt","r") as f:
        data=f.read()
        datalist=data.split("\n")
        print("".join(datalist[::-1]))

except FileNotFoundError:
    print("Error: The file you are trying to open does not exist.")




    