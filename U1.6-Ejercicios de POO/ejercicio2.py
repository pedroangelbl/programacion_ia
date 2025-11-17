"""Ejercicio 2

Crea una clase, y pruébala, que modele fracciones. Debe permitir:

Crear fracciones indicando numerador y denominador.
 Ejemplo: f = Fraction(2, 3)
Ojo!!! No se puede tener un denominador cero.
Las fracciones pueden operar entre sí.
Sumar, multiplicar, dividir, restar.
Ojo!!! esto se puede hacer: f + 1, 5 * f
Las fracciones se pueden comparar.
==, <, <=, >, >=, !=
Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
Ojo!!! esto se puede hacer 1 < 1/2"""

from __future__ import annotations
from math import gcd
from fractions import Fraction as PyFraction
from typeguard import typechecked


@typechecked
class Fraction:

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("El denominador no puede ser 0")
        common = gcd(numerator, denominator)
        self._numerator = numerator // common
        self._denominator = denominator // common

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, numerator):
        self._numerator = numerator

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, denominator):
        if denominator == 0:
            raise ValueError("El denominador no puede ser 0")
        self._denominator = denominator

    def __normalize(self, other: Fraction | int | float) -> Fraction:
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, float):
            py_fraction = PyFraction(other).limit_denominator()
            other = Fraction(py_fraction.numerator, py_fraction.denominator)
        return other

    def __add__(self, other: Fraction | int | float):
        other = self.__normalize(other)
        num = self.numerator * other.denominator + self.denominator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other: Fraction | int | float):
        other = self.__normalize(other)
        num = self.numerator * other.denominator - self.denominator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __rsub__(self, other):
        return self - other

    def __mul__(self, other: Fraction | int | float):
        other = self.__normalize(other)
        num = self.numerator * other.numerator
        den = other.denominator * other.denominator
        return Fraction(num, den)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other: Fraction | int | float):
        other = self.__normalize(other)
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __rtruediv__(self, other):
        other = self.__normalize(other)
        return other / self

    def __eq__(self, other):
        other = self.__normalize(other)
        return (self.numerator, self.denominator) == (
            other.numerator,
            other.denominator,
        )

    def __ne__(self, other):
        other = self.__normalize(other)
        return (self.numerator, self.denominator) != (
            other.numerator,
            other.denominator,
        )

    def __lt__(self, other):
        other = self.__normalize(other)
        return (self.numerator * other.denominator) < (
            other.numerator * self.denominator
        )

    def __le__(self, other):
        other = self.__normalize(other)
        return (self.numerator * other.denominator) <= (
            other.numerator * self.denominator
        )

    def __gt__(self, other):
        other = self.__normalize(other)
        return (self.numerator * other.denominator) > (
            other.numerator * self.denominator
        )

    def __ge__(self, other):
        other = self.__normalize(other)
        return (self.numerator * other.denominator) >= (
            other.numerator * self.denominator
        )
