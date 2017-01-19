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


class AthleteList(list):
    def __init__(self,a_name,a_job=None,a_times=[]):
        list.__init__([])
        self.name=a_name
        self.job=a_job
        self.extend(a_times)

    def top3(self):
        return (sorted(set([sanitize(t) for t in self]))[0:3])

#Open new txt function
def open_txt_new(file):
    try:
     with open(file) as temp:
         data=temp.readline().strip().split(",")
         return AthleteList(data.pop(0),data.pop(0),data)
    except IOError as error:
        print ("File error:"+error)
        return None

la=open_txt_new("LA.txt")
sa=open_txt_new("SA.txt")

print (la.name+"'s first 3 times are:"+str(la.top3()))
print (sa.name+"'s first 3 times are:"+str(sa.top3()))


