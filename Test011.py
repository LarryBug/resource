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

class Athlete(list):
    def __init__(self,a_name,a_job=None,a_times=[]):
        self.name=a_name
        self.job=a_job
        self.time=a_times

    def top3(self):
        return (sorted(set([sanitize(t) for t in self.time]))[0:3])

def add_time(self,time_value):
    self.time.append(time_value)

def add_time(self,list_of_times):
    self.time.extend(list_of_times)

"""
larry=Athlete("Larry Wang", "2012-3-15",["2:58","2.59","2:39","2-24","2-55","2:54","2.19","2-21","2.23"])
print larry.name + larry.job
"""
#Open new txt function
def open_txt_new(file):
    try:
     with open(file) as temp:
         data=temp.readline().strip().split(",")
         return Athlete(data.pop(0),data.pop(0),data)
    except IOError as error:
        print ("File error:"+error)
        return None

larry=open_txt_new("LA.txt")
print (larry.name+"'s fastest 3 time are:"+str(larry.top3()))