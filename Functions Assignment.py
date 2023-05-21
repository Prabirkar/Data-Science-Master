#!/usr/bin/env python
# coding: utf-8

# # Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the range of 1 to 25.

# In[110]:


# Key ward use to create the function "def"

#function to return a list of odd numbers in the range of 1 to 25.
def odd():
    odd=[]
    for i in range(1,26):
        if i % 2==1:
            odd.append(i)
    return odd


# In[111]:


odd()


# In[107]:


# another example after creting the list
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,25]


# In[108]:


def odd(a):
    odd=[]
    for i in a:
        if i % 2 ==1:
            odd.append(i)
    return odd


# In[109]:


odd(l)


# # Q2. Why \*args and \*\*kwargs is used in some functions? Create a function each for \*args and \*\*kwargs to demonstrate their use.

# In[33]:


# In function *args use to to pass the non keyword arguumrnts.
# on the other hand **args use to pass the Keyword arguumrnts.

#Example of the *args arguumrnts":

def test1(*args):
    return args


# In[34]:


# *args use to to pass the non keyword arguumrnts.

test1(1,2,3,4,5,[1,3,4,5,6],'prabrikar',[33,445,67])


# In[38]:


test1(a=34,b=23,c=[1,2,3,4],d =('prabir','kar'))


# In[39]:


#Example of the **args arguumrnts":

def test2(**args):
    return args


# In[40]:


# **args use to pass the Keyword arguumrnts.

test2(a=34,b=23,c=[1,2,3,4],d =('prabir','kar'))


# In[41]:


test2(1,2,3,4,5,[1,3,4,5,6],'prabrikar',[33,445,67])


# # Q3. What is an iterator in python? Name the method used to initialise the iterator object and the methodused for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14, 16,18, 20].

# In[20]:


# in Python iterator is a object that gets iterated through
# there are two methods 1. iter()  2.next()

# print the first five elements
l = [2, 4, 6, 8, 10, 12, 14, 16,18, 20]

iterator = iter(l)
for i in range(5):
    print(next(iterator))


# # Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator function.

# In[52]:


# Generator function is a very smart fuction which use to redure the process time and save the memory
# Which means generator function gives the result one at a time

# the yield is the keyward that we use in the generator function ,with yield function each time a value is getting Yeilded.

# here is the example of generator function

def test2(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b


# In[53]:


for i in test2(7):
    print(i)


# # Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the first 20 prime numbers.

# In[50]:


#Let's create a function to Find the Prime number
def Fnd_prime(n):
    if n <=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if  n % i ==0:
            return False
    return True


# In[51]:


# let's test if it's working or not
Fnd_prime(3)


# In[52]:


# let's test if it's working or not
Fnd_prime(4)


# In[67]:


# Let's find the first 20 prime numbers in less than 1000

def prime_generator():
    num = 2
    count = 0
    while count <20:
        if Fnd_prime(num):
            yield num
            count +=1
        num+=1
prime=prime_generator()  
for i in range(20):
    print(next(prime))


# In[ ]:




