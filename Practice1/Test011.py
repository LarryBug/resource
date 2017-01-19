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

    def add_times(self,list_of_times):
        self.time.extend(list_of_times)

    def remove(self,remove_value):
         self.time.remove(remove_value)

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


vera=Athlete("BY")
vera.add_time("1.32")
print (vera.top3())
vera.add_times(["1.55","1-42"])
print (vera.top3())
vera.remove(vera.top3()[len(vera.top3())-1])
print vera.top3()

class AthleteList(list):
    def __init__(self,a_name,a_job=None,a_times=[]):
        list.__init__([])
        self.name = a_name
        self.job = a_job
        self.extend(a_times)

    def top(self):
        return (sorted(set([sanitize(t) for t in self]))[0:5])

vera=AthleteList("FF")
vera.append("1.31")
print (vera.top())
vera.extend(["1.55","1-42","1:21"])
print (vera.top())
