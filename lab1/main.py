import monkdata as m
import dtree

def assignment1():
	print("monk1", dtree.entropy(m.monk1))
	print("monk2", dtree.entropy(m.monk2))
	print("monk3", dtree.entropy(m.monk3))

def avgForDataset(dataset, name):
	for attr in m.attributes:
		print(name, attr.name, dtree.averageGain(dataset, attr))

def assignment2():
	avgForDataset(m.monk1, "monk1")
	avgForDataset(m.monk2, "monk2")
	avgForDataset(m.monk3, "monk3")

assignment1()
assignment2()