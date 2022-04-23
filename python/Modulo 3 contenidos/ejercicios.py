#almacen = ["cocina", "Sal de control", "Sala de maquinas", "Sala de evaluacion", "Almacen"]
#print(almacen)

#meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre")

#salir = False

#while(not salir):
    #numero = int(input("Que numero es:"))

    #if(numero==0):
        #salir= True
    #else:
        #if:(numero >= 1 and numero <= 1 en(meses))
            #print(meses[numero-1])
        #else:
            #print("inserta numero de 1 y ", len(meses))


#nombres = []
#edades = []

#while True:
 #   nombre = input("Nombre del pasajero")
  #  if nombre != "*":
   #     nombres.append(nombre)
    #    edades.append(int(input("Cual es tu edad")))
    #if nombre == "*": break;


#edad_max = max(edades)
#print("Pasajeros mayores")
#print("==================")

#for nombre,edad in zip(nombres, edades):
 #   if edad >= 18:
  #      print(nombre)


#print("pasajeros mayor de edad")
#print("===================")
#for nombre,edad in zip(nombres,edades):
 #   if edad == edad_max:
  #      print(nombre)


#tripulantes = {}

#cantidad = int(input("Introduce la cantida de teipulantes que se guarda"))
#for num in range(cantidad):
 #   tripulante = input("Nombre del tripulante:")
  #  while tripulante in tripulantes:
   #     print("tripulante ya existe")
    #    tripulante = input("nombre del tripulante:")
    #notas=[]
    #nota = int(input("Dame una nota del tripulante en negativo"))
    #while nota > 0:
     #   notas.append(nota)
      #  nota = int(input("dame una nota del tripulante en negativo"))
    #tripulantes[tripulante] = notas.copy()

#for tripulante, notas in tripulantes.items():
 #   print("%s ha sacada de nota media %f" % (tripulante,sum(notas)/len(notas)))


frutas = {}

nombre = int(input("Dame el precio de la fruta"))
for num in range(nombre):
    fruta = input("nombre de la fruta")
    while fruta in frutas:
        print("fruta ya existe")
        fruta = input("nombre de la fruta")
    notas=[]
    nota = int(input("dame una fruta"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("dame una fruta"))
    frutas[fruta] = notas.copy()

for fruta, notas in frutas.items():
    print("%s ha repetido la fruta %f" % (fruta,sum(notas)/len(notas)))
    
