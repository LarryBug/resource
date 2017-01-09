def Remove_Duplicates(List):
    List_new = []
    for t in List:
        if t not in List_new:
            List_new.append(t)

    print List_new

List1 =["ax","ed" ,"al","tro","ed"]
List2 =[3,5,6,1,2,3]

Remove_Duplicates(List1)
Remove_Duplicates(List2)