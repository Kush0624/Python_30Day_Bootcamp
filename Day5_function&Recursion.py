# 1.Write a function max_of_three() that takes three numbers and returns the largest.

# 2.Write a function count_vowels() that counts the number of vowels in a string.

# 3.Write a function sum_list() that takes a list of numbers and returns their sum without using sum().

# 4.Write a recursive function to calculate the nth Fibonacci number.

# 5.Write a function that accepts **kwargs and prints only the values (not the keys).

# 6.Write a function reverse_words() that takes a sentence and returns it with words in reverse order.

# 7.Write a function that takes a number and returns whether it is prime or not.

def max_of_three(a,b,c):   #can be use inbuilt max function
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    elif(b>c):
        return b
    else:
        return c
    
# print(max_of_three(5,2,6))
# print(max_of_three(1,3,2))
# print(max_of_three(10,9,5))


def count_vowels(str1): # can use capital letters also instead of making them lower
    vowels="aeiou"
    str1=str1.lower()
    count=sum(1 for char in str1 if char in vowels)
    return count
# print(count_vowels("A quick brown fox jumps over a lazy dog"))

from functools import reduce
def sum_list(list1):
    ans=reduce(lambda x,y:x+y,list1)
    return ans

    

# print(sum_list([1,2,3,4,5]))

def fibonacci(n):  ## my jistake i code factorial instead of fibonacci
    if(n==0 or n==1):
        return 1
    return n*fibonacci(n-1)
# print(fibonacci(5))


def print_values(**kwargs):
    for key,values in kwargs.items():
        print(values,end=" ")
# print_values(name="Kushagra Goyal",age=22,income=50000,location="mumbai")


def reverse_order(str1):
    list1=str1.split()
    print(" ".join(list1[::-1]))


# reverse_order("My name is Kushagra Goyal")
from math import sqrt
def prime(n):
    if(n<=1):
        return False
    elif(n<=3):
        return True
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True
print(prime(15))
print(prime(11))
print(prime(2))




