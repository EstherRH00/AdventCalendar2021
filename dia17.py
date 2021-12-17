
target = [[128,160], [-88,-142]]
#target = [[20,30],[-5,-10]]
#maximaAlcada = 0
#velocitatGuanyadora = [0,0]
contador = 0
for x in range(1000):
    for y in range(-1000,1000):
        inicial = [0, 0]
        velocitatInicial = [x,y]
        velocitat = velocitatInicial[:]
        maxAlcada = 0
        trobat = False
        while inicial[0] <= target[0][1] and inicial[1] >= target[1][1] and not trobat:
            if(target[0][0] <= inicial[0] <= target[0][1]) and target[1][0] >= inicial[1] >= target[1][1]:
                '''if maximaAlcada < maxAlcada:
                    maximaAlcada = maxAlcada
                    velocitatGuanyadora = velocitatInicial
                    '''
                contador+= 1
                trobat = True
            else:
                inicial[0] += velocitat[0]
                inicial[1] += velocitat[1]
                if(velocitat[0] > 0): velocitat[0] -= 1
                elif velocitat[0] < 0: velocitat[0] += 1
                velocitat[1] -= 1
                '''if(inicial[1] > maxAlcada):
                    maxAlcada = inicial[1]'''

print(contador)