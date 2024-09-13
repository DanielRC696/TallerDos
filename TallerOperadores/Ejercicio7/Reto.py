# Función para validar notas
def validar_nota(nota_num):
    nota = float(input(f"Ingrese la {nota_num} nota (1.0 a 5.0): "))
    while nota < 1 or nota > 5:
        print(f"Error: La {nota_num} nota debe estar entre 1.0 y 5.0.")
        nota = float(input(f"Ingrese la {nota_num} nota (1.0 a 5.0): "))
    else:
        return nota

# Leer las notas
nota1 = validar_nota("primera")
print("Todas las notas deben estar entre 1 y 5.")
nota2 = validar_nota("segunda")
nota3 = validar_nota("tercera")
nota4 = validar_nota("cuarta")
nota5 = validar_nota("quinta")

# Calcular la nota final
nota_final = (nota1 * 0.20) + (nota2 * 0.15) + (nota3 * 0.22) + (nota4 * 0.10) + (nota5 * 0.33)
# Imprimir la nota final
print(f"La nota final del estudiante es: {nota_final:.2f}")

# Evalua la calificación final
if nota_final >= 4.5:
    print("Excelente")
elif nota_final >= 3.5:
    print("Bueno")
elif nota_final >= 3.0:
    print("Regular")
else:
    print("Insuficiente.")


