#!/usr/bin/env python
# coding: utf-8

# In[1]:


y='Jack'
x='Jill'
l= "mohamed"
k="nader"
print("{1} and {0} went up {2} the hill to{3} fetch a pail of water".format(x,y,l,k))


# In[ ]:





# In[5]:


#input from user
mo=int(input("enter any number you wont\n"))
k=str(input("enter name "))
print ("my name :{} ".format(k))


# In[10]:


a = int(input("enter your age"))
#k= (a-2)
print ("in 2020 your age is",a-2,yers )


# In[4]:


for a in range (10):
    a = int (input("enter number"))
    if a%2==0:
        break
    
    

    


# 
# a='mohamed reda amer'
# print(a)

# In[6]:


a = 'mohamed amer'
for i in a :
    print (i)
a[1:8:2]


# In[2]:


print('1323'.rjust(7,"*"))


# In[3]:


print ('mohamed'.ljust (20,"&"))


# In[4]:


print ("mohamed".upper())


# In[2]:


print ("Mohamed".lower())


# In[9]:


a="mohamed amer".split()
print (a)



# In[5]:


name = 'mohamed'
if name == 'mohamed':
    print ('my  favorit name is' )
elif name =='ahmed':
    print ('my secund favorit name is ')
else :
    print "i dont have a name "


# In[8]:


for i in range (3):
    for j in range (3):
        print ('*',end=" ")
    print ("\n")


# In[11]:


(lambda m,o:(m+o))(8,8)


# In[12]:


(lambda o,m:(o*m))(8,8)


# In[15]:


while True:
    try:
        
        n=int(input('Enter your score:'))
        print('You obtained a score of ',n)
        break
    except ValueError:
        print('Enter only an integer value')


# In[21]:


colors=['violet','indigo','red','blue','green','yellow']
colors.append('white')
colors.insert(3,'pink')
colors.extend(['purple','magenta'])
colors.sort
colors.reverse() 
print (colors)


# In[ ]:





# In[24]:


l = range(5)
for i in l[::-1]:
    print ("*"*i)
    print ("\n")


# In[28]:


(list ("123-456-7890".split("-")))


# In[30]:


colors=['violet','indigo','red','blue','green','yellow']
coloorid = [1,2,3,4,5,6,7]
for d,h in zip (colors,coloorid):
    print ( d,"has a serial number",h)


# In[32]:


coloorid = [1,2,3,4,5,6,7]
colors=['violet','indigo','red','blue','green','yellow']
list(zip (colors,coloorid)) 


# In[33]:


colors=['violet','indigo','red','blue','green','yellow']
for index,item in enumerate (colors):
    print (item,"oucar at index",index) 


# In[37]:


# tuple 
a= (8,9,7)
b = (a,*_)
print (b)
print (len(b))


# In[39]:


a=[9,8,7,7]

print (set(a))


# In[40]:


#OOP


# In[55]:


class mohamed :
    name = 'mohamed'
    age =19
    def __init__(self, name, age):
        self.name= name 
        self.age= age 

    def printmeth(self):
        print("name:",self.name,'\n',"age:",self.age)
mo=mohamed("mohamed",18)
mo.printmeth()


# In[61]:


#inheritance
class Mother():
    def __init__(self,fname,sname):
        self.firstname=fname
        self.surname=sname
    def nameprint(self):
        print("Name:",self.firstname+" "+self.surname)
class Child(Mother):
    fullname = Child("mohamed","amer")
    fullname.nameprint()


# In[ ]:





# In[ ]:




