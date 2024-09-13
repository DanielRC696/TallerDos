# Ingresa la cantidad a convertir
pesos_colombianos = float(input("Ingrese la cantidad de pesos colombianos: "))

# Definir la tasa de conversión
tasa_conversion = float(input("Ingrese la tasa de conversión de pesos a dólares: "))

# Convertir pesos a dólares
dolares = pesos_colombianos / tasa_conversion

print(f"{pesos_colombianos:.2f} pesos colombianos equivalen a {dolares:.2f} dólares.")
