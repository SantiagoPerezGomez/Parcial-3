"""
1. Crea una clase Complejo que permita trabajar con números complejos (parte real y
parte imaginaria). Incluye los siguientes métodos: constructores (por defecto y
parametrizado), accedentes, mutadores, suma, resta, multiplicación, división,
acumulación y print().
"""
import cmath
import math


class Complex:
    first = 0
    second = 0
    suma = 0
    resta = 0
    division = 0
    multiplicacion = 0

    def __init__(self, f, s):
        self.first = f
        self.second = s

    def print(self):
        print("Primer número = " + str(self.first))
        print("Segundo número = " + str(self.second))
        print("Suma de los dos números = " + str(self.suma))
        print("Resta de los dos números = " + str(self.resta))
        print("División de los dos números = " + str(self.division))
        print("Multiplicación de los dos números = " +
              str(self.multiplicacion))

    def calculate(self):
        self.suma = complex(self.first) + complex(self.second)
        self.resta = complex(self.first) - complex(self.second)
        self.division = complex(self.first) / complex(self.second)
        self.multiplicacion = complex(self.first) * complex(self.second)

    def mut(self):
        self.n1 = -1
        self.n2 = -5

    def acumulacion(self):
        numbers = [self.n1, self.n2]
        for i in numbers:
            print(i)


obj = Complex(1000, 2000)
obj.calculate()
obj.print()
obj.mut()
obj.acumulacion()

"""
2. Crea una clase Racional que permita trabajar con números racionales (fracciones).
Incluye los siguientes métodos: constructores (por defecto y parametrizado), accedentes,
leer(), suma, resta, multiplicación, división, comparaciones, copia() y print().
"""
print("-------------------------------------------------------")


class Racional:
    first = 0
    second = 0
    suma = 0
    resta = 0
    multiplicacion = 0
    division = 0

    def __init__(self, f, s):
        self.first = f
        self.second = s

    def print(self):
        print("Primer número = " + str(self.first))
        print("Segundo número = " + str(self.second))
        print("Suma de los dos números = " + str(self.suma))
        print("Resta de los dos números = " + str(self.resta))
        print("División de los dos números = " + str(self.division))
        print("Multiplicación de los dos números = " +
              str(self.multiplicacion))

    def calculate(self):
        self.suma = self.first + self.second
        self.resta = self.first - self.second
        self.division = self.first / self.second
        self.multiplicacion = self.first * self.second

    def comparate(self):
        return self.first == self.second


obj = Racional(0.25, 0.23)
obj.calculate()
print(obj.comparate())
obj.print()


print("-------------------------------------------------------")

"""
3. Crea una clase Rectangulo que modele rectángulos por medio de cuatro puntos (los
vértices). Dispondrá de dos constructores: uno que cree un rectángulo partiendo de sus
cuatro vértices y otro que cree un rectángulo partiendo de la base y la altura, de forma
que su vértice inferior izquierdo esté en (0,0). La clase también incluirá un método para
calcular la superficie y otro que desplace el rectángulo en el plano.
"""


class Rectangulo:
    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0

    def __init__(self, a, b, c, d):
        self.v1 = a
        self.v2 = b
        self.v3 = c
        self.v4 = d

    def area(self):
        return (self.v1+self.v2)*(self.v3+self.v4)

    def crear_rectangulo(self):
        return [self.v1, self.v4, self.v2, self.v3]


obj = Rectangulo(1, 2, 1, 2)
print(obj.area())
print(obj.crear_rectangulo())


print("-------------------------------------------------------")

"""
4. Define una clase Linea con dos atributos: _puntoA y _puntoB. Son dos puntos por
los que pasa la línea en un espacio de dos dimensiones. La clase dispondrá de los
siguientes métodos:
 Linea()
Constructor predeterminado que crea una línea con sus dos puntos como (0,0) y (0,0).
 Linea(Punto, Punto)
Constructor que recibe como parámetros dos objetos de la clase Punto,
que son utilizados para inicializar los atributos.
 mueveDerecha(double)
Desplaza la línea a la derecha la distancia que se indique.
 mueveIzquierda(double)
Desplaza la línea a la izquierda la distancia que se indique.
 mueveArriba(double)
Desplaza la línea hacia arriba la distancia que se indique.
 mueveAbajo(double)
Desplaza la línea hacia abajo la distancia que se indique.
 Accedentes y mutadores.
 Método que nos permita mostrar la información de la línea de la siguiente forma:
[puntoA,puntoB]. Por ejemplo: [(0.0,0.0),(1.0,1.0)].
"""


class Linea:
    _puntoA = 0
    _puntoB = 0

    def __init__(self, x, y):
        self._puntoA = x
        self._puntoB = y

    def crear_linea(self) -> list:
        return [self._puntoA, self._puntoB]

    def mueveDerecha(self, d) -> list:
        return [self._puntoA+d, self._puntoB]

    def mueveIzquierda(self, d) -> list:
        return [self._puntoA-d, self._puntoB]

    def mueveArriba(self, d) -> list:
        return [self._puntoA, self._puntoB+d]

    def mueveAbajo(self, d) -> list:
        return [self._puntoA, self._puntoB-d]

    def mut(self) -> str:
        self._puntoA = math.pi
        self._puntoB = math.cos(12)
        return (f"variables mutadas -> x:{math.pi},y:{math.cos(12)}")


obj = Linea(1, 1)
print(obj.crear_linea())
print(obj.mueveDerecha(1.1))
print(obj.mueveIzquierda(1.1))
print(obj.mueveArriba(1.1))
print(obj.mut())
print(obj.mueveAbajo(1.1))


print("-------------------------------------------------------")

"""
5. Crea una clase Cuenta (bancaria) con atributos para el número de cuenta (un entero
largo), el DNI del cliente (otro entero largo), el saldo actual y el interés anual que se
aplica a la cuenta (porcentaje). Define en la clase los siguientes métodos:
 Constructor por defecto y constructor con DNI, saldo e interés * 
 Accedentes y mutadores. Para el número de cuenta no habrá mutador.*
 actualizarSaldo(): actualizará el saldo de la cuenta aplicándole el interés diario
(interés anual dividido entre 365 aplicado al saldo actual).
 ingresar(double): permitirá ingresar una cantidad en la cuenta.
 retirar(double): permitirá sacar una cantidad de la cuenta (si hay saldo).
 Método que nos permita mostrar todos los datos de la cuenta.
El número de cuenta se asignará de forma correlativa a partir de 100001, asignando
el siguiente número al último asignado.
"""


class CuentaBancaria:
    numero_de_cuenta = 0
    dni = 0
    saldo_actual = 0
    interes_anual = 0

    def __init__(self,  d, saldo, interes):
        self.numero_de_cuenta = 100001
        self.dni = d
        self.saldo_actual = saldo
        self.interes_anual = interes

    def mut(self):
        self.dni = 101010101
        self.saldo_actual = 112.22
        self.interes_anual = 0.10

    def actualizarSaldo(self):
        return self.saldo_actual*(self.interes_anual/365)

    def ingresar(self, d):
        return self.saldo_actual+d

    def retirar(self, d):
        if self.saldo_actual <= 0:
            print("No se puede retira, saldo insuficiente.")
        else:
            return self.saldo_actual - d

    def print(self):
        print(f"numero de cuenta: {self.numero_de_cuenta}")
        print(f"dni: {self.dni}")
        print(f"saldo actual: {self.saldo_actual}")
        print(f"interes anual: {self.interes_anual*100}%")


obj = CuentaBancaria("109388444", 10.1, 0.10)
obj.print()
print("----Ingresando plata 100 pesos----")
print("saldo actual:", obj.ingresar(100))
print("retirando 100")
print("saldo actual:", obj.retirar(100))
print("Saldo con la tasa diaria")
print(obj.actualizarSaldo())
