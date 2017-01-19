# -*- coding: utf-8 -*-
import pickle
from AthleteList import AthleteList

#Open new txt function
def open_txt_new(file):
    try:
     with open(file) as temp:
         data=temp.readline().strip().split(",")
         return AthleteList(data.pop(0),data.pop(0),data)
    except IOError as error:
        print ("File error:"+error)
        return None

#store data function
def put_to_store(file_list):
    all_athletes={}
    for each_file in file_list:
        #讲文件转换成AthleteList对象，并把选手数据加到字典
        ath=open_txt_new(each_file)
        #每个对象作为字典的键-值，是AthleteList对象
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            #讲整个AthleteList增加到pickle中
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error (put_and_store): ' + str(ioerr))
    return all_athletes

#get data function
def get_in_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            #用load，将整个pickle入字典
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_from_store): ' + str(ioerr))
    return(all_athletes)


the_files=["LA.txt"]
data=put_to_store(the_files)
print data

for each_data in data:
    print (data[each_data].name+""+data[each_data].dob)

data1=get_in_store()
for each_data in data1:
    print (data[each_data].name+data[each_data].dob)
