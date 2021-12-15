def totsTenenEnd(camins):
    trobat = False
    i = 0
    while i < len(camins) and not trobat:
        if('end' not in camins[i]):
            trobat = True
        else:
            i+=1
    return not trobat

def pucVisitar(camins, lloc):
    if lloc not in cami:
        return True
    if not lloc.islower():
        return True
    #Si n'hi ha un altre de visitat dos cops, retorno false
    i = 0
    while i < len(camins):
        ara = camins[i]
        if ara.islower() and ara in camins[i+1:]:
            return False
        i+=1
    return True

f = open('input','r')
lines = f.readlines()
f.close()

for i in range(len(lines)):
    lines[i] = lines[i][:len(lines[i])-1]
    lines[i] = lines[i].split("-")

print(lines)

paths = []
for linia in lines:
    if 'start' in linia:
        if(linia[0] != 'start'):
            linia[0], linia[1] = linia[1], linia[0]
        paths.append([linia[0], linia[1]])

while not totsTenenEnd(paths):
    #print("inici iteracio, no tots tenen end", paths)
    pathsMod = paths[:]
    for j in range(len(paths)):
        #print("paths", paths, "pathsMod", paths)

        cami = paths[j]
        busco = cami[len(cami)-1]
        #print("cami", cami, "busco", busco)
        if(busco != 'end'):
            aux = []
            for parella in lines:
                camiMod = cami[:]
                if busco in parella and 'start' not in parella:
                    if busco == parella[0]:
                        altre = parella[1]
                    else:
                        altre = parella[0]
                    if pucVisitar(camiMod, altre):
                        camiMod.append(altre)
                        aux.append(camiMod)
            #print("he acabat de buscar", busco, aux)
            for path in aux:
                pathsMod.append(path)

            #print("els he afegit", pathsMod)
            pathsMod.remove(cami)

    paths = pathsMod[:]
    #print("acabada iteracio", j, paths)

print(len(paths))
