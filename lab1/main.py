import monkdata as m
import dtree as d
import random as r
import pyqtgraph as pg
import numpy as np
from pylab import *

fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]

def assignment1():
	print "   ", "Entropy"
	print "M1 ", d.entropy(m.monk1)
	print "M2 ", d.entropy(m.monk2)
	print "M3 ", d.entropy(m.monk3)

def avgForDataset(dataset):
	res = "";
	for attr in m.attributes:
		res += "{:.5f}".format(d.averageGain(dataset, attr))
		res += " "
	return res

def assignment2():
	print "   ", "     a1", "     a2", "     a3" , "     a4", "     a5", "     a6"
	print "M1 ", avgForDataset(m.monk1)
	print "M2 ", avgForDataset(m.monk2)
	print "M3 ", avgForDataset(m.monk3)

def checkAndBuild(dataset, compare):
	t = d.buildTree(dataset, m.attributes);
	return d.check(t, compare)

def assignment3():
	print "   ", "  train", "   test"
	print "M1 ", "{:.5f}".format(checkAndBuild(m.monk1, m.monk1)), "{:.5f}".format(checkAndBuild(m.monk1, m.monk1test))
	print "M2 ", "{:.5f}".format(checkAndBuild(m.monk2, m.monk2)), "{:.5f}".format(checkAndBuild(m.monk2, m.monk2test))
	print "M3 ", "{:.5f}".format(checkAndBuild(m.monk3, m.monk3)), "{:.5f}".format(checkAndBuild(m.monk3, m.monk3test))

def findBestTree(tree, compare, lastBest=0, lastBestTree=None):
	bestTree = lastBestTree
	bestVal = lastBest

	for p in d.allPruned(tree):
		val = d.check(p, compare)
		if val > bestVal:
			bestTree = p
			bestVal = val

	if(bestVal > lastBest):
		return findBestTree(bestTree, compare, bestVal, bestTree)
	else:
		return bestTree

def partition(data, fraction):
	ldata = list(data)
	r.shuffle(ldata)
	breakPoint = int(len(ldata) * fraction)

	return ldata[:breakPoint], ldata[breakPoint:]

def bestTreeByFraction(dataset, compare, fraction):
	train, val = partition(dataset, fraction)
	t = d.buildTree(train, m.attributes);
	bt = findBestTree(t, val)

	return d.check(bt, compare)

def valuesForFractions(dataset, compare):
	vals = []
	for fraction in fractions:
		vals.append(bestTreeByFraction(dataset, compare, fraction))

	return vals

def formatFractionValues(vals):
	res = ""
	for v in vals:
		res += "{:.5f}".format(v) + " "	

	return res

def assignment4():
	x = fractions
	y1 = valuesForFractions(m.monk1, m.monk1test)
	y3 = valuesForFractions(m.monk3, m.monk3test)


	print "   ", "    0.3", "    0.4", "    0.5", "    0.6", "    0.7", "    0.8"
	print "M1 ", formatFractionValues(y1)
	print "M3 ", formatFractionValues(y3)

	plot(x, y1)
	plot(x, y3)

	xlabel('fraction')
	ylabel('correctly classified')
	grid(True)
	show()

assignment1()
print
assignment2()
print
assignment3()
print
assignment4()