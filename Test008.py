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

with open("AX.txt") as ax: data =ax.readline()
axiong=data.strip().split(",")

with open("ED.txt") as ed: data=ed.readline()
edward=data.strip().split(",")

print (sorted(set([sanitize(t) for t in axiong]))[0:2])
print (sorted(set([sanitize(t) for t in edward]))[0:2])

#Open txt function
def open_txt(file):
    try:
     with open(file) as temp:
         data=temp.readline()
         return data.strip().split(",")
    except IOError as error:
        print ("File error:"+error)
        return None

print (sorted(set([sanitize(t) for t in open_txt("AX.txt")]))[0:2])
print (sorted(set([sanitize(t) for t in open_txt("ED.txt")]))[0:2])




