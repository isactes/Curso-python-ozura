tripulantes = 125 

if tripulantes>=25:
    print("se an envarcado mas de la mita de los tripulantes")
elif tripulantes <= 10:
    print("Se han embarcado menos de 50 tripulantes")
elif tripulantes >=20 and tripulantes <=30:
    print("se han embarcado de 20 a 30")
else: 
    print("no se sabe exactamente")

'''bucles'''
while tripulantes <= 150:
    print("todavia no se ha embarcado a todos Numero tripulante:" + str(tripulantes))
    tripulantes = tripulantes + 1

for i in range (1,11):
    print("numero: " + str(i))