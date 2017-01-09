import os

if os.path.exists('1.txt'):
    print "exist"
else:
    print "no"

data = open('1.txt')

for each_line in data:
    try:
        print (each_line.split(":"))
    except:
        pass
    finally:
        pass

f1=[]

try:
    file1= open("2.txt",'a+')
    file1.write("'\n'test 111")
    file1.close()
except IOError:
    pass