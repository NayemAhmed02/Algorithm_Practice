#!/usr/bin/env python
# coding: utf-8

# In[13]:


def bubbleSort(list):
    length = len(list)
    
    for i in range(0,length-1):
        for j in range(0,length-i-1):
            if list[j] > list [j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp


list = []
num = int(input("Enter the size of array: "))
print("Now, Enter array elements : \n")

for i in range(0,num):
    ele = int(input())
    list.append(ele)

print("Before sorted: ")
print(list)
print("\n\n")

print("After sorted in ascending order: ")
bubbleSort(list)
print(list)


# In[ ]:





# In[ ]:




