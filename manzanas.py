'''  Este programa lo hizo Daniel Rojas
 en esta fecha 04/02/2022 '''

print("Programa que te dice cuanto tienes que pagar")

cantidadManzanas=int(input("Ingresa el numero de manzanas: "))
costodeManzanas=int(input("Ingresa el costo de las manzanas: "))
totalaPagar=cantidadManzanas*costodeManzanas

if cantidadManzanas==18:
    print("desacuento secreto")
    descuento=totalaPagar*.25
elif cantidadManzanas>10:
    print("descuento del 10 %")
    descuento=totalaPagar*.10
else:
    print("no hay descuento master")
    descuento=0
print("descuento: ",descuento)
print("el cliente va a pagar" ,totalaPagar-descuento, "pesos")
