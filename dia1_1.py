f = open('input', 'r')
l = f.readlines()
f.close()

lines = [int(i) for i in l]

prev = None
contador = 0
for line in lines:
    if(prev == None):
        prev=line
    else:
        if(line > prev):
            contador += 1
        prev = line

print(len(lines), contador)

