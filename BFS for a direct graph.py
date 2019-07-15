#!/usr/bin/env python
# coding: utf-8

# In[30]:


#import defaultdictionary to store graph
#The defaultdict tool is a container in the collections class of Python

from collections import defaultdict 

#create a class for direct graph data manupulation

class BFS: 
  

    def __init__(self):
        #create defaultdictionary
        self.graph = defaultdict(list) 
        
    #store data on graph
    def edgeDetail(self,key,value): 
        self.graph[key].append(value) 
   
    def Travers(self, start): 
        
        #Find the number of vertex
        l = len(self.graph)
        
        # initialize visited list with bool value False
        visited = [False] * l 
        
        # Create a queue for BFS
        queue = [] 
        queue.append(start) 
        
        # Mark as It's already visited
        visited[start] = True
  
        while queue: 
            start = queue.pop(0) 
            print(start) 
            
            for i in self.graph[start]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
                    
# create a instance of BFS class 
g = BFS() 

g.edgeDetail(0, 1)  
g.edgeDetail(1, 2) 
g.edgeDetail(2, 0) 
g.edgeDetail(2, 3) 
g.edgeDetail(3, 3) 
g.edgeDetail(0, 2)
g.edgeDetail(1, 0)
g.edgeDetail(1, 3)

num = int(input("Enter the number of vertex,From where you want to start traveling (between 0 to 3): "))
  
print ("Following is Breadth First Traversal, Starting from vertex %d :" %num) 
g.Travers(num) 


# In[ ]:





# In[ ]:




