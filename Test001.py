"""
name = ["alice", "angus", "ED"]


name.append("Larry")
print (len(name))
print (name)

name.remove("ED")
print (len(name))
print (name)


name.pop()
print (len(name))
print (name)

name.insert(0,"ED")
print (len(name))
print (name)

name.insert(1,"1990")
name.insert(3,"1989")
name.insert(5,"1991")
print (name)



for a in name:
 if (a=="ED"):
    print (a)
 else:
     print "shit"


name = [5,32,11,7,1]

print name.sort()
print name

print sorted(name)

print name.sort(reverse=True)
print name


name = [5,32,11,7,1]

for i in range(len(name)-1,0,-1):
    print i
    for j in range(0,i):
        print ('j=')+str(j)
        if name[j] > name[j+1]:
            print(str(name[j])+"+"+str(name[j+1]))
            name[j],name[j+1] = name[j+1],name[j]
        else:
            print "Not"
        print name




List = [11.3, 61.2, 11.9, 7.5, 44]

#print sorted(List)

#print List.sort()
#print List

for i in range(len(List)-1,0,-1):
    for j in range(0,i):
        if List[j]>List[j+1]:
            List[j],List[j+1] = List[j+1],List[j]
print List

"""




