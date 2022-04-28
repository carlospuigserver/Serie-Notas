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



