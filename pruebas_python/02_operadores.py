### Operadores - Para números ### 

print(3 + 4) # suma
print(3 - 4) # resta
print(3 * 4) # multiplicación
print(3 / 4) # división
print(10 % 3) # operador de módulo - Te dice cuánto sobra cuando divides a entre b
print(3 // 4) # división "floor" - Aproxima el resultado a un número entero
print(2 ** 3) # calcular un exponen (ej. 2 elevado a 3)
print(2 ** 3 + 3  - 7 / 1 // 4)

print("Hola" + "Python") # El + concatena las palabras, pero el resto de símbolos da error
print("Hola" + str(5)) # No se pueden mezclar palabras y números a no ser que los convirtamos al mismo tipo
print("Hola " * 10) # Te multiplica la palabra por tantas veces que lo pongas
print("Hola " * (2 **3)) # Este operador también funciona, pero no es muy habitual

my_float = 2.5 * 2 
print("Hola " * int(my_float))

### Operadores comparativos ###
# Para los símbolos hay que instalar Fira Code en Visual Studio

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 3)
print(3 > 4 == 2)

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")
print("aaaa" >= "bbbb") # Ordenación alfabética. "b" es mayor que "a". 
print("aaaa" >= "AAAA") # Tiene también en cuenta mayúsculas y minúsculas.

### Operadores lógicos ###

print(3 > 4 and "Hola" > "Python") # Para que una expresión con and sea verdadera, todas las condiciones individuales deben ser verdaderas.
print(3 > 4 or "Hola" > "Python") # Para que una expresión con or sea verdadera, basta con que al menos una de las condiciones sea verdadera.
print(not(3 > 4)) # 'not' niega todo lo que viene después. Si lo que viene después es falso, el 'not' lo convierte en verdadero.

