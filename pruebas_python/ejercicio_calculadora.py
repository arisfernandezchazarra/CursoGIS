print("""Bienvenidos a la calculadora
Para salir escribe 'salir'
Las operaciones son: suma, resta, multi, div""")

resultado = None

while True:
    # Si no hay resultado previo, pedimos el primer número
    if resultado is None:
        entrada = input("Ingresa número: ")
        if entrada.lower() == "salir":
            break
        try:
            resultado = float(entrada)
        except ValueError:
            print("Número no válido, inténtalo de nuevo.")
            continue

    # Pedimos operación
    operacion = input("Ingresa operación: ")
    if operacion.lower() == "salir":
        break

    # Pedimos siguiente número
    entrada2 = input("Ingresa siguiente número: ")
    if entrada2.lower() == "salir":
        break
    try:
        num2 = float(entrada2)
    except ValueError:
        print("Número no válido, inténtalo de nuevo.")
        continue

    # Calculamos
    if operacion == "suma":
        resultado += num2
    elif operacion == "resta":
        resultado -= num2
    elif operacion == "multi":
        resultado *= num2
    elif operacion == "div":
        if num2 == 0:
            print("Error: no se puede dividir entre cero.")
            continue
        resultado /= num2
    else:
        print("Operación no reconocida.")
        continue

    print(f"El resultado es: {resultado}")

print("¡Hasta luego!")
