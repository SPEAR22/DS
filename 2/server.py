import sys
from omniORB import CORBA, PortableServer
import Calculator, Calculator__POA

class CalculatorImpl(Calculator__POA.Calculator):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            raise Calculator.DivisionByZero("Division by zero")

orb = CORBA.ORB_init(sys.argv, CORBA.ORB_ID)
poa = orb.resolve_initial_references("RootPOA")
poa.activate()

calculator = CalculatorImpl()

# Obtain a reference to the Calculator object
obj = calculator._this()

# Print the object reference (IOR)
ior = orb.object_to_string(obj)
print("Server IOR:", ior)

# Run the ORB event loop
orb.run()

