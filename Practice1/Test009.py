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

mikey=["1","1:1","1-3"]
clean_arr=[]
for each in mikey:
    clean_arr.append(sanitize(each))

clean_arr1=[sanitize(each) for each in mikey]
print clean_arr
print clean_arr1

with open("AX.txt") as ax: date =ax.readline()
axiong=date.strip().split(",")

#1.
ax_arr2=[]
for each in axiong:
    ax_arr2.append(sanitize(each))
print sorted(ax_arr2)

#2.
ax_arr1=[sanitize(each) for each in axiong]
print sorted(ax_arr1)

#3.
print sorted([sanitize(each) for each in axiong])

#delete repeated
ax_temp1=sorted([sanitize(each) for each in axiong])
unique_ax=[]
for each in ax_temp1:
    if each not in unique_ax:
        unique_ax.append(each)
print unique_ax


distances=set()
distances={12,6.7,9,"two",7}
distances=set(axiong)
print distances


