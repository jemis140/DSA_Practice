class graph:
	def __init__(self, gdict = None):
		if gdict is None: 
			gdict = []
		self.gdict = gdict
	def getVertices(self):
		return list(self.gdict.keys())

	def edges(self):
		return self.findedges()

	def findedges(self): 
		edgename = []
		for vrtx in self.gdict:
			for nxtvrtx in self.gdict[vrtx]:
				if {nxtvrtx, vrtx} not in edgename:
					edgename.append({vrtx, nxtvrtx}) 
		return edgename

	def addVertex(self, vrtx):

		if vrtx not in self.gdict:
			self.gdict[vrtx] = []

	def AddEdge(self, edge): 
		edge = set(edge)
		(vrtx1, vrtx2) = tuple(edge) 
		if vrtx1 in self.gdict:
			self.gdict[vrtx1].append(vrtx2) 
		else:
			self.gdict[vrtx1] = [vrtx2]

graph_elements = {"a" : ["b", "c"], "b" : ["a", "d"],"c" : ["a", "d"], "d" : ["e"],"e" : ["d"]}
g = graph(graph_elements)
g.addVertex('f') 
print(g.getVertices())
g.AddEdge({'a','e'})
g.AddEdge({'f','e'}) 
g.AddEdge({'q','v'}) 
print(g.gdict)
print(g.edges())