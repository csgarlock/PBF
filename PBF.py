class PBF:
	def __init__(self, file):
		self.file = open(file, "r")
		self.ptr = 0
		self.ins_list = self.file.read().split("\n")
		self.pbi_list = []
		for l in self.ins_list:
			self.pbi_list.append(PBI(l))
		i = 0
		self.pbm_list = []
		while(True):
			if(self.pbi_list[i].is_death()):
				break
			if(self.pbi_list[])



class PBI:
	def __init__(self, line):
		self.line = line
		self.parts = self.line.split(" ")
		self.ins = self.parts[0]
		self.args = self.parts[1:]

	def get_ins(self):
		return self.ins

	def is_meth(self):
		return self.ins == "fun"

	def is_meth_end(self):
		return self.ins == "end"

	def is_death(self):
		return self.ins == "die"

class PBM:
	def __init__(self, ins):
		self.ins = ins
		self.length = len(ins)
		self.name = ins[0].args[0]
 		