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

	def __eq__(self, other):
		firstNumerator = self.numerator * other.denominator
		secondNumerator = other.numerator * self.denominator
		return firstNumerator == secondNumerator


myFraction = Fraction(3,5)
print(myFraction)
print("I ate {} of the pizza".format(myFraction))
print("Yeah, you read that right. I ate {} of the pizza!".format(myFraction))

#Adding fractions
fraction1 = Fraction(1,4)
fraction2 = Fraction(1,2)
fraction3 = fraction1 + fraction2
#prints 6/8 instead of 3/4
#need functionality to reduce the fraction
#use Euclid's Algorithm
print("{} + {} = {}".format(fraction1, fraction2, fraction3))
print(fraction1 == fraction2)