import numpy
from hsic import dHSIC

# --- Number of variables and samples
D = 5
N = 1000

# --- Simulate distribution
X = numpy.array([numpy.linspace(-1, 1, N) for _ in range(D)]).T
TWO_D = 2*numpy.array(range(D))
Y = numpy.matmul(numpy.multiply(X, X), TWO_D)
# ---

# --- Run dHSIC calculation
# --- (if no parameters have been changed, this will return 0.05190...
print(dHSIC(X, Y))

# --- Generate several sets of random data
X1 = numpy.array([numpy.random.uniform(-1, 1, N) for _ in range(D)]).T
X2 = numpy.array([numpy.random.uniform(-1, 1, N) for _ in range(D)]).T
Y = numpy.matmul(numpy.multiply(X1, X2), TWO_D)
print(dHSIC(X1, X2, Y))

# or, if you want to pass your arguments as a list, unpack it:
print(dHSIC(*[X1, X2, Y]))

print("ok! Good to go.")
