
import random
numero_secreto = random.randint(1,100)
adivinado= False
cant_intentos = 0 #para agregarle complejidad
cant_max_intentos = 5
print("Bienvenido al juego de adivinar el número secreto")

while not adivinado and cant_intentos < cant_max_intentos: 
    numero= int(input("Introduce un número del 1 al 99: "))
    # input: permite que el usuario haga una entrada de un valor
    # el input trae texto (string), por lo que habrá que Castearlo (convertirlo a número) para que el juego funcione 
    # Para que funcione y pueda trabajar con el mismo tipo de variables, hay dos opciones: 
      # 1) numero= int(input("Introduce un número del 1 al 99")) o 
      # en dos líneas: 2) entrada=input("Introduce un número") y numero=int(entrada)  
    
    if numero == numero_secreto:
        print("Felicidades! Has adivinado el número secreto!")
        adivinado= True
    elif numero < numero_secreto: 
        print("Oh no! El número secreto es mayor al ingresado")
    else: 
        print("Oh no! El número secreto es menor al ingresado")
    
    cant_intentos +=1 #para que me vaya descontanto intentos

if not cant_intentos< cant_max_intentos: 
    print("Game Over! Has llegado a la cantidad máxima de intentos")

#---------------------------------------
"""Otra forma de resolver/ejecutar el programa usando BREAK sería: 

while not adivinado: 
    if not cant_intentos< cant_max_intentos: 
    print("Game Over! Has llegado a la cantidad máxima de intentos")  
    break
    
    numero= int(input("Introduce un número del 1 al 99: "))
    if numero == numero_secreto:
        print("Felicidades! Has adivinado el número secreto!")
        adivinado= True
    elif numero < numero_secreto: 
        print("Oh no! El número secreto es mayor al ingresado")
    else: 
        print("Oh no! El número secreto es menor al ingresado")
    
    cant_intentos +=1 

"""