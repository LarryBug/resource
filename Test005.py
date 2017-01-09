import os

#get AX fastest time
ax1=open("AX.txt")
ax_data=ax1.readline()
#use "," for split and strip blank
axtemp1=ax_data.strip().split(",")
axtemp2=[]

for values in axtemp1:
    if "-" in values:
        axtemp2.append(values.replace("-",":"))
    else:
        axtemp2.append(values)

axtemp2.sort()
print axtemp2[0]

#get ED fastest time
ed1=open("ED.txt")
ed_data=ed1.readline()
edtemp1=ed_data.strip().split(",")
edtemp2=[]

for values in edtemp1:
    if "-" in values:
        edtemp2.append(values.replace("-",":"))
    else:
        edtemp2.append(values)

edtemp2.sort()
print edtemp2[0]

if edtemp1[0]>edtemp2[0]:
    print "ax first "+edtemp2[0]
elif edtemp1[0]<edtemp2[0]:
    print "ed first" + edtemp1[0]
else:
    print "As fast as they can"