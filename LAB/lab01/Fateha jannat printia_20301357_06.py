#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=open("Input file.txt",'r')
b=a.readlines()
dic={}
start=str(input("give starting place name: "))

queue=[start]
for i in b:
    places=i.strip("\n").split()
    dic[places[0]]=places[1:]

distance=[int(dic[start][0])]
traversed=[]
dest=input("give destination place name: ")

cost=0
parent=''
check=0

while True:
    if len(distance)==0:
        break
        
    short=min(distance) # start to parent + heuristics 
    indx=distance.index(short)

    lowest=queue.pop(indx)
    
    if lowest == dest:
        cost=distance.pop(indx)
        check=1
        break
    traversed.append(lowest)
    distance.pop(indx)
    for value in range(len(dic[lowest][1:])):  #parent to child access
        if value%2!=0:
            
            place=dic[lowest][1:][value-1]
            parentTo_childDistance= dic[lowest][1:][value]
            
            if place in traversed:
                continue
                
            if place in queue:  
                                    # dic[dic[lowest][1:][value-1]][0]= child heuristic
                x=queue.index(place)   # short-int(dic[lowest][0])= parent heuristic
                                     # short-int(dic[lowest][0])= start to parent distance calculation
    
                new_distance=int(parentTo_childDistance)+int(dic[place][0])+short-int(dic[lowest][0])
                b=min(distance[x],new_distance)
                distance[x]=b
  
                if (new_distance==distance[x]) and (place==dest):
                    parent=lowest
                
            else:
                distance.append(int(parentTo_childDistance)+int(dic[place][0])+short-int(dic[lowest][0]))
                queue.append(place) #child append
                if (place==dest):
                    parent=lowest

if start==dest:
    print('Total distance: 0 Km')
    
elif check==1:
    idx=traversed.index(parent)
    path_i = [parent,dest]
    for j in traversed[:idx:][::-1]:
        if path_i[0] in  dic[j] :
            path_i=[j]+path_i

    print('Path:',end=" ")
    for i in range(len(path_i)):
        if i==len(path_i)-1:
            print(path_i[i])
        else: 
            print(path_i[i],'->',end=" ")
    print('Total distance:',cost-int(dic[dest][0]),'Km')
else:
    print("NO PATH FOUND")


# In[ ]:




