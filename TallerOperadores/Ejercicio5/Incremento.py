salario_actual = float(input("Ingrese el salario mínimo actual: "))

# Calcular el incremento
incremento = salario_actual * 0.042

# Calcula el nuevo salario sumando el incremento
nuevo_salario = salario_actual + incremento

# Paso 4: Mostrar el nuevo salario
print(f"El nuevo salario mínimo es: {nuevo_salario:.2f} pesos")
