"""Ejercicio 2

Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. Recuerda
que puedes usar unas dentro de otras si es necesario.

Observa bien lo que hace cada función ya que, si las implementas en el orden adecuado,
te puedes ahorrar mucho trabajo. Por ejemplo, la función is_palindromic() resulta trivial teniendo
reverse() y la función next_prime() también es muy fácil de implementar teniendo is_prime().

Está prohibido usar funciones de conversión del número a una cadena.

is_palindromic: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
is_prime: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
next_prime: devuelve el menor primo que es mayor al número que se pasa como parámetro.
digits: devuelve el número de dígitos de un número entero.
reverse: le da la vuelta a un número.
digit_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de izquierda a derecha.
digit_position: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra, devuelve -1.
remove_behind: le quita a un número n dígitos por detrás (por la derecha).
remove_ahead: le quita a un número n dígitos por delante (por la izquierda).
paste_behind: añade un dígito a un número por detrás.
paste_ahead: añade un dígito a un número por delante.
piece_of_number: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente.
concatenate: pega dos números para formar uno.
"""


def digits(num):
    count_digits = 0

    while num > 0:
        num = num // 10
        count_digits += 1
    return count_digits


def reverse(num):
    inverted_num = 0

    while num > 0:
        last_digit = num % 10
        inverted_num = inverted_num * 10 + last_digit
        num = num // 10

    return inverted_num


def is_palindromic(num):
    if num == reverse(num):
        return True
    return False


def digit_n(num, n):
    total = digits(num)

    num = num // 10 ** (total - n - 1)

    return num % 10


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def next_prime(num):
    while True:
        if is_prime(num + 1):
            return num + 1
        num += 1


def digit_position(num, digit):
    total = digits(num)

    for position in range(total):
        if digit_n(12345, position) == digit:
            return position
    return -1


def remove_behind(num, n):
    return num // 10**n


def remove_ahead(num, n):
    total = digits(num)
    return num % 10 ** (total - n)


def paste_behind(num, n):
    return num * 10 + n


def paste_ahead(num, n):
    total = digits(num)
    return ((num / 10**total) + n) * (10**total)


def piece_of_number(num, start, end):
    total = digits(num)
    num = remove_ahead(num, start)
    num = remove_behind(num, total - end - 1)
    return num


def concatenate(num1, num2):
    return ((num2 / 10) + num1) * 10


def main():
    print("digit_n(12345, 2):", digit_n(12345, 2))
    print("is_palindromic(12321):", is_palindromic(12321))
    print("next_prime(14):", next_prime(14))
    print("digit_position(987654, 5):", digit_position(987654, 5))
    print("piece_of_number(123456, 1, 3):", piece_of_number(123456, 1, 3))
    print("concatenate(2, 6):", concatenate(2, 6))


if __name__ == "__main__":
    main()
