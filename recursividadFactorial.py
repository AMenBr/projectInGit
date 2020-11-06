def factorial(n):
    """Calcula el factorial de n.

    param int n > 0
    retorna n!
    """
    if n == 1:
        return 1
    return n * factorial(n -1)

result = int(input('Entre un numero: '))
print(factorial(result))