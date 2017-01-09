import pickle
import Test002

#pick can save anything object in python, dump for saving, load for restore
with open("1.pickle","wb") as mydata:
     pickle.dump([11,22,"sss"], mydata)

with open("1.pickle","rb") as myrestoredata:
    list=pickle.load(myrestoredata)
    print list

Test002.test2(100)
Test002.test1()
