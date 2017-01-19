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

#mins change to secs
mins=[1,2,3]
secs=[m*60 for m in mins]
print secs

#m change to feet
m=[1,10,3]
feet=[m*3.281 for m in mins]
print feet

#change to upper
lower=["i","want","to","get","you"]
upper=[s.upper() for s in lower]
print upper

#change time correctly
dirty=["2-33","2.41","2.12"]
clean=[sanitize(t) for t in dirty]
print clean

#change float
clean1=[float(s) for s in clean]
print clean1

#conenct
clean2=[float(sanitize(t)) for  t in ["2.3","1-2","3:3"]]
