# Variables

my_string_variable = "My String Variable"
print(my_string_variable)  

my_int_variable = 5
print(my_int_variable)

#Convertimos un numero entero en una cadena de texto. Esto se llama 'Casting' en programación
my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

#Concatenación de variables en un print - Concatenar es unir varias cadenas de texto para crear una más larga
print(my_string_variable, str(my_int_variable), my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable)) # len: Cuenta el número caracteres, incluyendo los espacios

# Variables en una sola línea
name, surname, alias, age = "Aris", "Fernández", "Ars", 35
print("Me llamo:", name, surname, "My edad es:", age, "Y mi alias es:", alias)

# ME HE QUEDADO EN EL MIN: 1:16:38
