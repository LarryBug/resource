#coding:utf-8
#sanitize functions
def sanitize(time_sting):
    if "-" in time_sting:
        splitter ="-"
    elif ":" in time_sting:
        splitter=":"
    else:
        return (time_sting)

    (mins,secs)=time_sting.split(splitter)
    return (mins+"."+secs)

#Open txt function
def open_txt(file):
    try:
     with open(file) as temp:
         data=temp.readline()
         return data.strip().split(",")
    except IOError as error:
        print ("File error:"+error)
        return None

larry=open_txt("LA.txt")

"""
#pop(0) delete and return list two up of front, then assigen to 2 variabke
(larry_name, larry_dob) = larry.pop(0), larry.pop(0)
print (larry_name +"'s fastest time is:"+str(sorted(set([sanitize(t) for t in larry]))[0:1]))
"""

larry_data={}
larry_data["name"]=larry.pop(0)
larry_data["dob"]=larry.pop(0)
larry_data["time"]=sorted([sanitize(t) for t in larry])

print (larry_data["name"] +"'s time is:"+str(larry_data["time"]))

#Open new txt function
def open_txt_new(file):
    try:
     with open(file) as temp:
         data=temp.readline().strip().split(",")
         return {
             "name":data.pop(0),
             "dob":data.pop(0),
             "time":sorted([sanitize(t) for t in data])
         }
    except IOError as error:
        print ("File error:"+error)
        return None

larry_data1=open_txt_new("LA.txt")
print (larry_data1["name"]+"'s time is:"+str(larry_data1["time"]))