import random
numero_secreto = random.randint(1,100)
adivinado= False
cant_intentos = 0
cant_max_intentos = 5
print("Bienvenido al juego de adivinar el número secreto")


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
    
    cant_intentos += 1 
