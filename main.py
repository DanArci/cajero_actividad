saldo_inicial = 1000
print("-----------------------------------------------------")
print(".................Bienvenido al Cajero.................")
print("-----------------------------------------------------")
print("")
print("")
print("")
print("Coloca 1 para ver tu saldo")
print("Coloca 2 para retirar dinero")
print("Coloca 3 para depositar dinero")
print("")
opcion = input()
if opcion == "1" :

    print("")
    print("Tu saldo es de: ",saldo_inicial)

elif opcion == "2":
        
    terminar = 0
    print("")
    print ("Coloca el monto a retirar")
    print("")
    while terminar == 0:
        monto = int(input())    
        if monto <= 1000 and monto > 0:
            retiro = saldo_inicial - monto
            print("")
            print("Haz retirado ",monto," de tu cuenta ")
            print("Han quedado en tu cuenta: ",retiro)
            terminar = 1
        elif monto > 1000 :
            print("")
            print("Saldo insuficiente")
            print("")
            print("Coloque un monto a retirar")
            monto = 0
        else:
            print("")
            print("Coloque un valor valido")
            monto = 0

elif opcion == "3":
        
    terminar = 0
    print("")
    print ("Coloca el monto a depositar")
    while terminar == 0:
        monto = int(input())    
        if monto > 0:
            deposito = saldo_inicial + monto
            print("")
            print("Haz depositado ",monto," a tu cuenta ")
            print("Ahora tu cuenta tiene un saldo de: ",deposito)
            terminar = 1
        else:
            print("Coloque un valor valido")