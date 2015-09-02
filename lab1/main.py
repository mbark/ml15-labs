import monkdata as m
import dtree

def assignment1():
	print "   ", "Entropy"
	print "M1 ", dtree.entropy(m.monk1)
	print "M2 ", dtree.entropy(m.monk2)
	print "M3 ", dtree.entropy(m.monk3)

def avgForDataset(dataset):
	res = "";
	for attr in m.attributes:
		res += "{:.5f}".format(dtree.averageGain(dataset, attr))
		res += " "
	return res

def assignment2():
	print "   ", "     a1", "     a2", "     a3" , "     a4", "     a5", "     a6"
	print "M1 ", avgForDataset(m.monk1)
	print "M2 ", avgForDataset(m.monk2)
	print "M3 ", avgForDataset(m.monk3)

assignment1()
print
assignment2()