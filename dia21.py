pp1 = 4 #score
sp1 = 0 #position
pp2 = 2
sp2 = 0

dau = 0
p1 = True
contador = 0

#universos: 1 3 6 7 6 3 1
#punts:     3 4 5 6 7 8 9

dicc = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
victoriesP1A = 0
victoriesP1B = 0
victoriesP2A = 0
victoriesP2B = 0
universos = [[pp1,0,pp2,0,1]]
while 0 != len(universos):
    aux = []
    for univers in universos:
        for punt in dicc.keys():
            if(p1):
                pp1 = (univers[0] + punt) % 10
                if pp1 == 0: pp1 = 10
                sp1 = pp1 + univers[1]
                if sp1 >= 21:
                    victoriesP1A += univers[4]
                    victoriesP1B += dicc[punt]*univers[4]
                else:
                    aux.append([pp1, sp1, univers[2], univers[3], dicc[punt]*univers[4]])
            else:
                pp2 = (univers[2] + punt) % 10
                if pp2 == 0: pp2 = 10
                sp2 = pp2 + univers[3]
                if sp2 >= 21:
                    victoriesP2A += univers[4]
                    victoriesP2B += dicc[punt] * univers[4]
                else:
                    aux.append([univers[0], univers[1], pp2, sp2, dicc[punt]*univers[4]])
    universos = aux
    p1 = not p1

if( victoriesP1B >=  victoriesP2B):
    print( victoriesP1B)
else:
    print( victoriesP2B)
print(victoriesP1A, victoriesP1B, victoriesP2A, victoriesP2B)
'''
while sp1 < 1000 and sp2 < 1000:
    avanca = 3*dau+1+2+3
    dau = dau + 3
    if p1:
        pp1 = (pp1 + avanca) % 10
        if pp1 == 0: pp1 = 10
        sp1 += pp1
    else:
        pp2 = (pp2 + avanca) % 10
        if pp2 == 0: pp2 = 10
        sp2 += pp2
    p1 = not p1
    contador += 3
    #print(pp1, sp1, pp2, sp2)
    #a = input("he")

print(pp1, sp1, pp2, sp2)
if sp1 >= 1000:
    print(sp2 * contador)
else:
    print(sp1 * contador)
'''

