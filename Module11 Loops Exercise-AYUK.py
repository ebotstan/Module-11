#!/usr/bin/env python
# coding: utf-8

# ### Exercise 1
# Create a multiplication table from 1 to 10

# In[24]:


for a in range(1, 11):
    for b in range(1, 11):
        print(a * b, end='\t')
    print('')


# ### Exercise 2
# Write a program to find the Fibonacci numbers where each number is the sum of the two preceding ones, starting from 0 and 1. 
# 
#     e.g.
#     0, 1, 1, 2, 3, 5, 8, ...
#     
# Ask a user to enter a number. Next, generate user specified number of Fibonacci numbers into a list. Then print out the list. The output should look something like this:
# 
#     How many Fibonacci numbers would you like to generate? 10    
#     10 Fibonacci numbers are [0, 1, 1, 2, 3, 5, 8, 13, 21, 34].

# In[25]:


# Displaying ten (10) Fibonacci numbers

numbs = int(input("How many Fibonacci numbers would you like to generate? "))

# first numbers in the series
mylist = []
       
mylist.append(numbs)
numb1, numb2 = [0, 1]
count = 0

# check if the number of terms is valid
if numbs <= 0:
   print("Please enter a positive integer")
# if there is only one term, return numb1
elif numbs == 1:
   print("Fibonacci sequence upto",numbs,":")
   mylist = []
   mylist.append(numb1)
   print(numb1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < numbs:
       mylist = []
       mylist.append(numb1)
       print(numb1)
       next_numb = numb1 + numb2
       # update values
       numb1 = numb2
       numb2 = next_numb
       count += 1
print(mylist)


# In[ ]:





# In[ ]:




