#!/usr/bin/env python
# coding: utf-8

# In[4]:


#TOPIC: Python Basics Variable
'''1. Declare two variables, `x` and `y`, and assign them integer values. Swap
the values of these variables without using any temporary variable.'''

x=10
y=20 
#variables have been declared

print('the value of x is', x)
print('the value of y is', y)

#Swapping the values of x and y
x=x+y
y=x-y
x=x-y

print('the value of x after swapping is', x)
print('the value of y after swapping is', y)


# In[7]:


'''2. Create a program that calculates the area of a rectangle. Take the length
and width as inputs from the user and store them in variables. Calculate and
display the area.'''

print('TO FIND THE AREA OF A RECTANGLE')
#declaring length and breadth as variables and taking input from user
length = int(input("Enter the length of rectangle"))
breadth = int(input("Enter the breadth of rectangle")) 
#taking input as integer values

area = length*breadth
print('The area of the rectangle is', area)


# In[9]:


'''3. Write a Python program that converts temperatures from Celsius to
Fahrenheit. Take the temperature in Celsius as input, store it in a variable,
convert it to Fahrenheit, and display the result.'''

print('CELSIUS TO FAHRENHEIT')

#Taking the value of celcius as input from user
Celsius = float(input('Enter the temperature in degree celsius'))

Fahrenheit = (Celsius*9/5)+32 #formula to convert from celsius to fahrenheit

print('the temperature in degree fahrenheit is', Fahrenheit)


# In[1]:


#TOPIC: String Based Questions


# In[3]:


'''1. Write a Python program that takes a string as input and prints the length
of the string.'''

String = str(input('Enter a string'))
#String declare as user input

print(len(String))
# KEYWORD 'len' prints the length of the string


# In[15]:


'''2. Create a program that takes a sentence from the user and counts the
number of vowels (a, e, i, o, u) in the string.'''

#Taking input from the usre
str1 = str(input('Enter the sentence'))

str2 = str1.count('a')            #Here count function counts the specific
str3 = str1.count('e')            #character in a string  
str4 = str1.count('i')
str5 = str1.count('o')
str6 = str1.count('u')

s1 = str1.count('A')
s2 = str1.count('E')
s3 = str1.count('I')
s4 = str1.count('O')
s5 = str1.count('U')
vowels = (str2 + str3 + str4 + str5 + str6 + s1 + s2 + s3 + s4 + s5)
print('The number of vowels in the sentence are', vowels)


# In[16]:


'''3. Given a string, reverse the order of characters using string slicing and 
print the reversed string.'''

Name = 'AnupamBadola'
print(Name[::-1])


# In[21]:


'''4. Write a program that takes a string as input and checks if it is a 
palindrome (reads the same forwards and backwards).'''

#taking string input from the user
string = str(input('Enter a string'))

#creating a reverse string 'pallindrome' of the input string
pallindrome = string[::-1]

#using if else statement
if pallindrome == string:
    print("Yes")
else:
    print("No")


# In[26]:


'''5. Create a program that takes a string as input and removes all the spaces 
from it. Print the modified string without spaces.'''

#Taking String input
string = str(input("Enter your sentence"))

Newstr = string.replace(" ","") #Here replace function swaps the two characters
print(Newstr)                  # in a string


# In[ ]:




