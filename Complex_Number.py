from math import hypot, cos, sin, tan


class CustomComplex:
    """
    This class represent a complex number i.e., x+yj.

    A lot of dunder methods are overloaded to keep the functionalities of
    built-in operators and functions.
    """
    def __init__(self, real_number, imag_number):
        """
        Initializes a complex number
        :param real_number: real part
        :param imag_number: imaginary part
        """
        self.real = real_number
        self.imag = imag_number

    def conjugate(self):
        """
        returns the conjugate of complex number
        :return: complex number
        """
        return self.__class__(self.real, - self.imag)

    def argz(self):
        """
        returns the argument of complex number
        :return: float
        """
        return tan(self.imag / self.real)

    def __repr__(self):
        """
        representation of an instance of the class. it can be used with eval()
        for execution.
        :return: str
        """
        return f"{self.__class__.__name__}({self.real}, {self.imag})"

    def __str__(self):
        """
        returns a user-friendly representation of complex numbers
        :return: str
        """
        return f"({self.real},{self.imag:+}j)"

    def __add__(self, other):
        """
        performs adding of complex numbers with int, float and complex numbers itself.
        :param other: can be int, float and complex number
        :return: complex number
        """
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real + other
            imag_part = self.imag
        elif isinstance(other, self.__class__):
            real_part = self.real + other.real
            imag_part = self.imag + other.imag
        else:
            return TypeError("Please provide proper input i.e., int, float and complex number")

        return self.__class__(real_part, imag_part)

    def __sub__(self, other):
        """
        performs subtraction of complex numbers with int, float and complex numbers.
        :param other: int, float or complex number
        :return: complex number
        """
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real - other
            imag_part = self.imag
        elif isinstance(other, self.__class__):
            real_part = self.real - other.real
            imag_part = self.imag - other.imag
        else:
            return TypeError("Please provide proper input i.e., int, float and complex number")

        return self.__class__(real_part, imag_part)

    def __mul__(self, other):
        """
        performs multiplication of complex numbers with int, float and complex number
        :param other: int float or complex number
        :return: complex number
        """
        if isinstance(other, float) or isinstance(other, int):
            real_part = self.real * other
            imag_part = self.imag
        elif isinstance(other, self.__class__):
            real_part = self.real * other.real
            imag_part = self.imag * other.imag
        else:
            return TypeError("Please provide proper input i.e. int, float and complex number")

        return self.__class__(real_part, imag_part)

    def __radd__(self, other):
        """
        performs reverse addition i.e. other + complex number
        :param other: int, float or complex number
        :return: complex number
        """
        return self.__add__(other)

    def __rmul__(self, other):
        """
        performs reverse multiplication i.e. other x complex number
        :param other: int, float or complex number
        :return: complex number
        """
        return self.__mul__(other)

    def __rsub__(self, other):
        """
        performs reverse subtraction i.e. other - complex number.
        Subtraction is not commutative, that is why a separate condition is mentioned.
        :param other: int, float and complex number
        :return: complex number
        """
        if isinstance(other, float) or isinstance(other, int):
            real_part = other - self.real
            imag_part = self.imag
        else:
            return TypeError("Please provide proper input i.e. int, float")

        return self.__class__(real_part, imag_part)

    def __eq__(self, other):
        """
        performs equality i.e. other == complex number
        :param other: complex number
        :return: Bool
        """
        if isinstance(other, self.__class__):
            return (self.real == other.real) and (self.imag == other.imag)
        else:
            return False

    def __ne__(self, other):
        """
        performs inequality i.e. other != complex number
        :param other: complex number
        :return: Bool
        """
        if isinstance(other, self.__class__):
            return (self.real != other.real) or (self.imag != other.real)
        else:
            return True

    def __pow__(self, power):
        """
        responsible for calculating the power of a complex number
        :param power: int or float
        :return: complex number
        """
        if isinstance(power, float) or isinstance(power, int):
            modulus_pow = hypot(self.real, self.imag) ** power
            argz_mult = self.argz() * power

            real_part = round(modulus_pow * (cos(argz_mult)))
            imag_part = round(modulus_pow * (sin(argz_mult)))

            return self.__class__(real_part, imag_part)
        else:
            return TypeError("Please provide an int or float as power")


