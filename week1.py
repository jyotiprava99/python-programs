#!/usr/bin/env python
# coding: utf-8

# In[5]:


#create one variable containing following type data
x='computer'
y=["fruits","vegetables","flowers"]
z=0.6
s=(1,2,3,4)
print (type(x))
print (type(y))
print (type(z))
print (type(s))


# In[6]:


#the data type of the above given
var1=' '
var2='[DS,ML,PYTHON]'
var3=['DS','ML','PYTHON']
var4=1
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))


# In[8]:


#using following operators
a=10
b=3
print(a/b)
print(a%b)
print(a//b)
print(a**b)


# In[9]:


a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)


# In[5]:


a=int(input())
b=int(input())
if b==0:
    print("error:division by zero is not allowed")
count=0
while a>=b:
    a-=b
    count+=count
if a==0:
    print("number is divisible. it can be divided {}".format(count))
else:
    print("number is not divisible")


# In[11]:


a=[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print(type(a))
for i in a:
    pass
if i%3==0:
    print("divisible by 3")
else:
    print("is not divisible by 3")
    i+=i
print(i)


# In[ ]:




