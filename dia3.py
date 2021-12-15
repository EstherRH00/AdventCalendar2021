#'110000011011\
#110000010001
#000100000001
f = open('input', 'r')
lines = f.readlines()
f.close()

bits = [0,0,0,0,0,0,0,0,0,0,0,0]
#bits = [0, 0, 0, 0, 0]
for num in lines:
    for i in range(len(num)):
        if num[i] == '1':
            bits[i] += 1
    # print(bits)

for i in range(len(bits)):
    numero = bits[i]
    if (numero >= len(lines) // 2):
        bits[i] = 1
    else:
        bits[i] = 0

print(bits)
#print(lines)
i = 0
while (len(lines) != 1 and i < len(bits)):

    lines = [j for j in lines if j[i] == str(bits[i])]

    #Actualitzar bits
    bits = [0,0,0,0,0,0,0,0,0,0,0,0]
    #bits = [0, 0, 0, 0, 0]
    for num in lines:
        for k in range(len(num)):
            if num[k] == '1':
                bits[k] += 1
        # print(bits)

    print(bits)

    for l in range(len(bits)):
        if(len(lines)%2 == 0):
            a = len(lines) // 2
        else:
            a = len(lines) // 2 + 1
        numero = bits[l]
        if (numero >= a):
            bits[l] = 1
        else:
            bits[l] = 0

    #print(lines)
    print(bits)
    i += 1

print("REsult", lines)