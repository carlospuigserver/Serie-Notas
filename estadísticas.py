Mates = list(["math percentage"])
Lectura = list(["reading score percentage"])
Escritura = list(["writing score percentage"])

m=len(Mates)

for i in range (1,m):
    dicc = {"notas_mates":Mates, "notas_lectura":Lectura, "notas_escritura":Escritura}
print(m)

print("Cantidad de observaciones")
print("Cantidad de Observaciones={}".format(m))


#Media

print("Media aritmética")
notasmates=sum(Mates)
mediaMates=notasmates/m
print("La media aritmética de Mates es {}".format(mediaMates))

notaslectura=sum(Lectura)
mediaLectura=notaslectura/m
print("La media aritmética de Lectura es {}".format(mediaLectura))

notasescritura=sum(Escritura)
mediaEscritura=notasescritura/m
print("La media aritmética de Ecritura es {}".format(mediaEscritura))


#Mediana

print("Mediana")
mediana=int(m/2)
medMates=(Mates[mediana]+Mates[mediana+1]/2)
print("La mediana en Mates es: {}".format(medMates))

medLectura=(Lectura[mediana]+Lectura[mediana+1]/2)
print("La mediana en Lectura es: {}".format(medLectura))

medEscritura=(Escritura[mediana]+Escritura[mediana+1]/2)
print("La mediana en Lectura es: {}".format(medEscritura))


# Valor mínimos y máximos

print("Valores mínimos")
minMates=None
for numero in Mates:
    if(minMates is None or numero<minMates):
        minMates=numero
        print("La peor nota de Mates es", minMates)

minLectura=None
for numero in Lectura:
    if(minLectura is None or numero<minLectura):
        minLectura=numero
        print("La peor nota de Lectura es", minLectura)


minEscritura=None
for numero in Escritura:
    if(minEscritura is None or numero<minEscritura):
        minEscritura=numero
        print("La peor nota de Escritura es", minEscritura)


print("Valores máximos")
maxMates=None
for numero in Mates:
    if(maxMates is None or numero>maxMates):
        maxMates=numero
        print("La mejor nota de Mates es", maxMates)


maxLectura=None
for numero in Lectura:
    if(maxLectura is None or numero>maxLectura):
        maxLectura=numero
        print("La mejor nota de Lectura es", maxLectura)


maxEscritura=None
for numero in Escritura:
    if(maxEscritura is None or numero>maxEscritura):
        maxEscritura=numero
        print("La mejor nota de Escritura es", maxEscritura)



