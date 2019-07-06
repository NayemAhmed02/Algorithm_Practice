#!/usr/bin/env python
# coding: utf-8

# In[11]:


def binarySearch(list, item, num):
    start = 0
    end = num-1
    
    while start <= end:
        mid = int((start+end) / 2)
        if item == list[mid]:
            return mid
        elif item < list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1       

list = [ ]
num = int(input("Enter the size of the array: "))
print("Now, Enter array elements: ")

for i in range(0,num):
    ele = int(input())
    list.append(ele)

item = int(input("Enter the number that you want to search in your list: "))
result = binarySearch(list, item, num)

if result == -1:
    print("\n%d is not present in you array\n"%item)
else:
    print("\n%d is present at index %d\n"%(item,result))
    


# In[ ]:





# In[ ]:




