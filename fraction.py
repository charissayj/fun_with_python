import math

def greatestCommonDenominator(m,n):
		while m % n != 0:
			oldm = m
			oldn = n

			m = oldn
			n = oldm % oldn
		return n

class Fraction:
	def __init__(self, numerator, denominator):
		self.numerator = numerator
		self.denominator = denominator

	def __str__(self):
		return str(self.numerator) + "/" + str(self.denominator) 
	
	def __add__(self, secondFraction):
		newNumerator = self.numerator * secondFraction.denominator + self.denominator*secondFraction.numerator
		newDenominator = self.denominator * secondFraction.denominator
		commonDenominator = greatestCommonDenominator(newNumerator, newDenominator)
		return Fraction(newNumerator//commonDenominator, newDenominator//commonDenominator)

	def __sub__(self, secondFraction):
		newNumerator = self.numerator * secondFraction.denominator - self.denominator*secondFraction.numerator
		newDenominator = self.denominator * secondFraction.denominator
		commonDenominator = greatestCommonDenominator(newNumerator, newDenominator)
		return Fraction(newNumerator//commonDenominator, newDenominator//commonDenominator)

	def __mul__(self, otherFraction):
		newNumerator = self.numerator * otherFraction.numerator
		newDenominator = self.denominator * otherFraction.denominator
		commonDivisor = greatestCommonDenominator(newNumerator, newDenominator)
		return Fraction(newNumerator//commonDivisor, newDenominator//commonDivisor)


	def __div__(self, otherFraction):
		newNumerator = self.numerator * otherFraction.denominator
		newDenominator = self.denominator * otherFraction.denominator
		commonDivisor = greatestCommonDenominator(newNumerator, newDenominator)
		return Fraction(newNumerator//commonDivisor, newDenominator//commonDivisor)

	def __eq__(self, otherFraction):
		firstNumerator = self.numerator * otherFraction.denominator
		secondNumerator = otherFraction.numerator * self.denominator
		return firstNumerator == secondNumerator

	def __lt__(self, otherFraction):
		firstNumerator = self.numerator * otherFraction.denominator
		secondNumerator = otherFraction.numerator * self.denominator
		return firstNumerator < secondNumerator

	def __gt__(self, otherFraction):
		firstNumerator = self.numerator * otherFraction.denominator
		secondNumerator = otherFraction.numerator * self.denominator
		return firstNumerator > secondNumerator


myFraction = Fraction(3,5)
print(myFraction)
print("I ate {} of the pizza".format(myFraction))
print("That's right. Twas I that ate {} of the pizza!".format(myFraction))

#Adding fractions
fraction1 = Fraction(1,4)
fraction2 = Fraction(1,2)
fraction3 = fraction1 + fraction2
fraction4 = fraction1 - fraction2
fraction5 = fraction3 * fraction1
fraction6 = fraction2 / fraction1

#prints 6/8 instead of 3/4
#need functionality to reduce the fraction
#use Euclid's Algorithm
print("{} + {} = {}".format(fraction1, fraction2, fraction3))
print("{} - {} = {}".format(fraction1, fraction2, fraction4))
print("{} * {} = {}".format(fraction3, fraction1, fraction5))
print("{} / {} = {}".format(fraction2, fraction1, fraction6))
print(fraction1 == fraction2)
print(fraction1 > fraction2)
print(fraction1 > fraction2)