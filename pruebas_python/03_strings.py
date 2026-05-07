### Strings ###

my_string = "Mi string"
my_other_string = 'Mi string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string) # Si metemos un espacio entre comillas te separa la concatenación también.

my_new_line_string = 'Este es un String \n con salto de línea' # \n es un salto de línea.
print(my_new_line_string)

my_new_line_string = '\t Este es un String con tabulación' # \t es una tabulación.
print(my_new_line_string)

my_new_line_string = '\t Este es un String \n escapado' # Se pueden combinar.
print(my_new_line_string)

my_new_line_string = '\\t Este es un String \\n escapado' # La doble barra (\\) elimina el efecto de una barra (\t o \n)
print(my_new_line_string)

# Formateo

'''
El .format una plantilla o un "formulario para rellenar". 
Las llaves {} son cajas vacías o "asientos reservados".
El .format(name, surname, age) al final de la frase es la instrucción que le dice a Python: "Oye, mete estas variables en las cajas".

'''

name, surname, age = "Aris", "Fernández", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %s" %(name, surname, age))
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaqueado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse

reversed_language = language[::-1]
print(reversed_language)

# Funciones del lenguaje

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))
print("Py" == "py")  # No es lo mismo