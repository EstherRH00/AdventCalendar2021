f = open('input.txt', 'r')
l = f.readlines()
f.close()

lines = [int(i) for i in l]

prev = None
contador = -1
sumA=0
sumB=0
for i in range(len(lines)-2):
    #Actualitzo el A sistematicament
    sumB = sumA
    sumA=lines[i]+lines[i+1]+lines[i+2]
    if(sumA > sumB):
        contador += 1
    #print("previ", sumB, "actual", sumA, "contador", contador)

print(len(lines), contador)
