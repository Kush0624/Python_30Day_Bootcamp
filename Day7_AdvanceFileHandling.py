# Write a program to read a file line by line and print the longest line.

# Write a program to count the number of lines, words, and characters in a file.

# Write a program to append a list of numbers into a file and then read them back.

# Write a program that tries to open a file. If it doesn’t exist, create it and write "Hello World".

# Write a program to load a JSON file of student marks and print the student with the highest score.


with open("data.txt","r") as f:
    list1=f.readlines()
    longest=max(list1,key=len)
print(longest)

with open("data.txt","r") as f:
    list1=f.read()

lines=list1.split("\n")
words=list1.split()
characters=len(list1)
print(len(lines),len(words),characters)


list1=[1,2,3,4,5]
with open("data.txt","a") as f:
    for i in list1:
        f.write(str(i)+"\n")

with open ("data.txt","r") as f:
    text=f.readlines()

print(text)



        
