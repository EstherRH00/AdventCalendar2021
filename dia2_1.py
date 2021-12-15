f = open('input2', 'r')
l = f.readlines()
f.close()
hor = 0
depth = 0
aim = 0
for line in l:
    aux = line.split(" ")
    if(aux[0][0]=='f'):
        hor+=int(aux[1])
        depth+=(aim*(int(aux[1])))
    elif(aux[0][0]=='d'):
        aim+=int(aux[1])
    else:
        aim-=int(aux[1])
print(hor, depth, hor*depth)
