saldo_inicial = 1000
print("""
-----------------------------------------------------
.................Bienvenido al Cajero.................
----------------------------------------------------- 

Coloca 1 para ver tu saldo
Coloca 2 para retirar dinero
Coloca 3 para depositar dinero
      
""")
opcion = input()
if opcion == "1" :
    
    print("""
Tu saldo es de: """,saldo_inicial)
    
elif opcion == "2":

    terminar = 0
    print ("""
Coloca el monto a retirar
           """)
    while terminar == 0:
        try:
            monto = int(input())
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        if monto <= 1000 and monto > 0:
            retiro = saldo_inicial - monto
            print("""
Haz retirado """,monto,""" de tu cuenta 
                  """)
            print("Han quedado en tu cuenta: ",retiro)
            terminar = 1
        elif monto > 1000 :
            print("""
Saldo insuficiente
                  """)
            print("Coloque un monto a retirar")
            monto = 0
        else:
            print("""
Coloque un valor valido""")
            monto = 0

elif opcion == "3":
        
    terminar = 0
    print ("""
Coloca el monto a depositar""")
    while terminar == 0:
        try:
            monto = int(input())
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        if monto > 0:
            deposito = saldo_inicial + monto
            print("""
Haz depositado """,monto,""" a tu cuenta
Ahora tu cuenta tiene un saldo de: """,deposito)
            terminar = 1
        else:
            print("Coloque un valor valido")