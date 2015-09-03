from cvxopt.solvers import qp
from cvxopt.base import matrix
from matplotlib import pylab
import numpy, random, math

def q(l):
	return numpy.full(l, -1)

def h(l):
	return numpy.full(l, 0)

def G(l):
	g = numpy.zeros(shape=(l, l))
	numpy.fill_diagonal(g, -1)
	return g

def linearK(x, y):
	return numpy.dot(x, y)+1

def polynomialK(x, y):
	K = linearK(x, y)
	return K*K*K

def t(data):
	t = []
	x = []
	for d in data:
		x.append([d[0], d[1]])
		t.append(d[2])

	return x, t

def P(x, t):
	N = len(x)
	matrix = numpy.zeros(shape=(N, N))
	for i in range(N):
		for j in range(N):
			matrix[i][j] = t[i] * t[j] * polynomialK(x[i], x[j])

	return matrix

def ind(point, a, t, data):
	sum = 0
	for i in range(len(data)):
		sum += a[i] * t[i] * polynomialK(point, data[i])
	return sum

def basically_zero(v):
	t = 0.00001
	return v >= -t and v <= t

classA = [(random.normalvariate(-1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)] + [(random.normalvariate(1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)]
classB = [(random.normalvariate(0.0, 0.5), random.normalvariate(-0.5, 0.5), -1.0) for i in range(10)]

data = classA + classB
random.shuffle(data)

d = map(lambda d: d[:-1], data)
t = map(lambda d: d[-1], data)
l = len(d)
P = P(d, t)
q = q(l)
G = G(l)
h = h(l)

r = qp(matrix(P), matrix(q), matrix(G), matrix(h))
alpha = list(r['x'])

nonZeroA = []
nonZeroP = []
nonZeroT = []
for i, a in enumerate(alpha):
	if(not basically_zero(a)):
		nonZeroA.append(alpha[i])
		nonZeroP.append(d[i])
		nonZeroT.append(t[i])

pylab.hold(True)
pylab.plot([p[0] for p in classA],
	[p[1] for p in classA],
	'bo')
pylab.plot([p[0] for p in classB],
	[p[1] for p in classB],
	'ro')

xrange = numpy.arange(-4, 4, 0.05)
yrange = numpy.arange(-4, 4, 0.05)

grid = matrix([[ind([x, y], nonZeroA, nonZeroT, nonZeroP)
	for y in yrange]
	for x in xrange])

pylab.contour(xrange, yrange, grid,
	(-1.0, 0.0, 1.0),
	colors=('red', 'black', 'blue'),
	linewidths=(1, 3, 1))

pylab.show()
