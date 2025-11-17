"""En Python existen clases para manipular duraciones de tiempo (horas:minutos:segundos), 
pero no nos gustan, vamos a hacer una nueva que se llamará Duration y será inmutable. Debe permitir:

Crear duraciones de tiempos.
    Ejemplo: t = Duration(10,20,56)
    Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
    Si no indico la hora, minuto o segundo estos valores son cero:
        Duration() --> (0, 0, 0)
        Duration(34) --> (34, 0, 0)
        Duration(34, 15) --> (34, 15, 0)
        Duration(34, 61) --> (35, 1, 0)
Las duraciones de tiempo se pueden comparar.
A las duraciones de tiempo les puedo sumar y restar segundos.
Las duraciones de tiempo se pueden sumar y restar."""

from __future__ import annotations
from typeguard import typechecked


@typechecked
class Duration:

    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        self.__hours, self.__minutes, self.__seconds = hours, minutes, seconds
        self.__normalize()

    def __str__(self):
        return f"{self.hours}h {self.minutes}m {self.seconds}s"

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.hours}, {self.minutes}, {self.seconds})"
        )

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    def __normalize(self):
        """Cambia las horas, minutos y segundos del objeto Duration a segundos para que se pueda
        trabajar mejor con ellas y poder reajustarlas a horas, minutos y segundos adecuadamente
        """
        seconds = self.__total_seconds()
        if seconds < 0:
            raise ValueError("No puede haber duraciones de tiempo negativas")
        self.__hours = seconds // 3600
        self.__minutes = (seconds % 3600) // 60
        self.__seconds = seconds % 3600 % 60

    def __total_seconds(self):
        time_in_seconds = self.hours * 3600 + self.__minutes * 60 + self.__seconds
        return time_in_seconds

    def __add__(self, other: Duration):
        return Duration(
            self.hours + other.hours,
            self.minutes + other.minutes,
            self.seconds + other.seconds,
        )

    def __sub__(self, other: Duration):
        return Duration(
            self.hours - other.hours,
            self.minutes - other.minutes,
            self.seconds - other.seconds,
        )

    def __eq__(self, other: Duration):
        return (self.hours, self.minutes, self.seconds) == (
            other.hours,
            other.minutes,
            other.seconds,
        )

    def __ne__(self, other: Duration):
        return (self.hours, self.minutes, self.seconds) != (
            other.hours,
            other.minutes,
            other.seconds,
        )

    def __lt__(self, other: Duration):
        return (self.hours, self.minutes, self.seconds) < (
            other.hours,
            other.minutes,
            other.seconds,
        )

    def __le__(self, other: Duration):
        return (self.hours, self.minutes, self.seconds) <= (
            other.hours,
            other.minutes,
            other.seconds,
        )

    def __gt__(self, other: Duration):
        return (self.hours, self.minutes, self.seconds) > (
            other.hours,
            other.minutes,
            other.seconds,
        )

    def __ge__(self, other: Duration):
        return (self.hours, self.minutes, self.seconds) >= (
            other.hours,
            other.minutes,
            other.seconds,
        )
