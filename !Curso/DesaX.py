def promedio(numeros):
  """Calcula el promedio de una lista de números.
  Args:
    numeros: Una lista de números.
  Returns:
    El promedio de los números en la lista.
  """
  if not numeros:
    return None  # Si la lista está vacía, retornamos None
  suma = sum(numeros)
  cantidad = len(numeros)
  promedio = suma / cantidad
  return promedio
# Ejemplo de uso:
numeros = [10, 20, 30, 40, 50]
resultado = promedio(numeros)
print("El promedio es:", resultado)