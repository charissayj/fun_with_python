class LogicGate:
	def __init__(self, n):
		self.label = n
		self.output = None

	def getLabel(self):
		return self.label

	def getOutput(self):
		self.output = self.performGateLogic()
		return self.output

class BinaryGate(LogicGate):
	def __init__(self, n):
		LogicGate.__init__(self, n)
		self.pinA = None
		self.pinB = None

	def getPinA(self):
		if self.pinA == None:
			return int(input("Enter Pin A input for gate " + self.getLabel() + " --> "))
		else:
			return self.pinA.getFrom().getOutput()

	def getPinB(self):
		if self.pinB == None:
			return int(input("Enter Pin B input for gate " + self.getLabel() + " --> "))
		else:
			return self.pinB.getFrom().getOutput()

	def setNextPin(self, source):
		if self.pinA == None:
			self.pinA = source
		else:
			if self.pinB == None:
				self.pinB = source
			else:
				print("Cannot Connect, NO EMPTY PINS on this gate")


class UrnaryGate(LogicGate):
	def __init__(self, n):
		LogicGate.__init__(self, n)
		self.pin = None

	def getPin(self):
		if self.pin == None:
			return int(input("Enter Pin input for gate " + self.getLabel() + " --> "))
		else:
			return self.pin.getFrom().getOutput()

	def setNextPin(self, source):
		if self.pin == None:
			self.pin = source
		else:
			print("Cannot Connect: NO EMPTY PINS on this gate")

class AndGate(BinaryGate):
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a == 1 and b == 1:
			return 1
		else:
			return 0

class OrGate(BinaryGate):
	def __init__(self, n):
		BinaryGate.__init__(self, n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		if a == 1 or b == 1:
			return 1
		else:
			return 0

class NotGate(UrnaryGate):
	def __init__(self, n):
		UrnaryGate.__init__(self, n)

	def performGateLogic(self):
		if self.getPin():
			return 0
		else:
			return 1

class Connector:
	def __init__(self, fromGate, toGate):
		self.fromGate = fromGate
		self.toGate = toGate
		toGate.setNextPin(self)

	def getFrom(self):
		return self.fromGate

	def getTo(self):
		return self.toGate



gate1 = AndGate("Gate1")
print(gate1.getOutput())

gate2 = OrGate("Gate2")
print(gate2.getOutput())

gate3 = NotGate("Gate3")
print(gate3.getOutput())

connector1 = Connector(gate1, gate3)