print("Bienvenidos a la Terrafama")
num_entero = 8 #intMore actions

num_decimal = 8.78 #float

mensaje = "Terrafama es un sitio para terrarios" #str

suma = num_entero + num_decimal 

resta = num_entero - num_decimal

multipliccion = num_entero * num_decimal

division = num_entero / num_decimal

print("suma: ", suma)

print("resta: ", resta)

print("multiplicacion: ", multiplicacion)

print("division: ", division)

print("Mensaje: ", mensaje)

nombre = input("¿Cuál es el nombre del emprendimiento? ")More actions

saludo = "hola" + nombre + " , ¡Terrafama!"

print(saludo)

print("¡Gracias por conocer nuestro emprendimiento!")

numero_usuario = int(input("Introduce un número entero: "))More actions

if numero_usuario % 2 == 0:

    print(f"El número {numero_usuario} es par.")

else:

    print(f"El número {numero_usuario} es impar.")

 
numeros = [2, 10, 15, 28, 29]More actions


print("\nLCalculando los cuadrados de los números en la lista:")


for numero in numeros:


    cuadrado = numero ** 2


    print(f"El cuadrado de {numero} es {cuadrado}")

   entrada_usuario = ""More actions


print("\nEscribe 'salir' para terminar el programa.")


while entrada_usuario != "salir":


    entrada_usuario = input("Escribe algo: ")


    if entrada_usuario != "salir":


        print(f"Intentelo de nuevo, escribiste: {entrada_usuario}")


    if entrada_usuario == "salir":


        print("\n¡¡Felicidades!! Finalizaste el programa.")  
    
    estudiantes = ["Efrain", "Benkos Biojo", "Renato", "Ayrton", "Tiago" ]More actions


print("Lista de estudiantes: ")


for nombre in estudiantes:


    print(f"- {nombre}")

   contacto = {More actions


    "nombre": "Efrain Acevedo",


    "correo": "efrauniatlantico@gmail.com",


    "telefono": "3002803707",


}


print("\nInformación de contacto:")


for clave, valor in contacto.items():


    print(f"{clave.capitalize()}: {valor}") 

 estudiantes = ["Efrain", "Benkos Biojo", "Renato", "Ayton", "Tiago"]More actions


contacto = {


    "nombre": "Marco Roldan",


    "correo": "roldanbmt@hotmail.com",


    }


opcion = input("¿Quieres agregar un 'estudiante' o actualizar 'correo'?: ")


if opcion == "estudiante":


    nuevo_estudiante = input("Introduce el nombre del nuevo estudiante: ")


    estudiantes.append(nuevo_estudiante)


    print("\nLista de estudiantes actualizada:")


elif opcion == "correo":


    nuevo_correo = input("Introduce el nuevo correo: ")


    contacto["correo"] = nuevo_correo


    print("\nDiccionario de contacto actualizado:")


else:


    print("Opción no válida. Por favor, elige 'estudiante' o 'correo'.") 

   print("calculadora basica")More actions


print("puedes sumar, restar, multiplicar o dividir")


numero1 = float(input("introduce el primer numero: "))


numero2 = float(input("introduce el segundo numero: "))


operacion = input("¿Que operacion quieres realizar? (suma, resta, multiplicacion, division): ").lower()


if operacion == "suma":


    resultado = numero1 + numero2


    print(f"La suma de {numero1} y {numero2} es: {resultado}")


elif operacion == "resta":


    resultado = numero1 - numero2


    print(f"La resta de {numero1} y {numero2} es: {resultado}")


elif operacion == "multiplicacion":


    resultado = numero1 * numero2


    print(f"La multiplicación de {numero1} y {numero2} es: {resultado}")


elif operacion == "division":


    if numero2 != 0:


        resultado = numero1 / numero2


        print(f"La división de {numero1} entre {numero2} es: {resultado}")


    else:


        print("Error: No se puede dividir por cero.")


else:


    resultado = None


    print("Operación no válida. Por favor, elige entre suma, resta, multiplicación o división.") 

  import randomMore actions


numero_secreto = random.randint(1, 100)


intentos_usuario = 0


print("\nBienvenido al juego de adivinanza de números ---\n")


print("He pensado en un número entre 1 y 100.")


while intentos_usuario != numero_secreto:


    intentos_usuario = int(input("Introduce tu numero: "))


    if intentos_usuario < numero_secreto:


        print("El número es mayor. Inténtalo de nuevo.")


    elif intentos_usuario > numero_secreto:


        print("El número es menor. Inténtalo de nuevo.")


    else:


        print(f"¡Felicidades! Has adivinado el número secreto: {numero_secreto}.")    