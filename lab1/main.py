import monkdata as m
import dtree as d

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

assignment1()
print
assignment2()
print
assignment3()