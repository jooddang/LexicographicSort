# binary search tree
class LexicoBst(object):
	def __init__(self, value, lexicoIndex):
		self.value = value
		self.left = None
		self.right = None

		self.lexicoIndex = lexicoIndex
		# construct hash for comparison. the order is defined by the order of lexicoIndex 
		self.lexicoHash = {}
		self.lexicoHash[''] = 0
		for i in range(0, len(lexicoIndex)):
			self.lexicoHash[lexicoIndex[i]] = i + 1
	
	def search(self, value):
		# not used in this quiz.. but searching is a main function of bst
		if self.value == value:
			return self
		elif self.value < value:
			if self.right is None:
				return None
			else:
				self.right.search(value)
		elif self.value > value:
			if self.left is None:
				return None
			else:
				self.left.search(value)

	def insert(self, value):
		if self.value == value:
			# show only once for duplicated key
			return
		elif self.isGreaterThan(value):
			if self.left is None:
				self.left = LexicoBst(value, self.lexicoIndex)
			else:
				self.left.insert(value)
		else:
			if self.right is None:
				self.right = LexicoBst(value, self.lexicoIndex)
			else:
				self.right.insert(value)
			

	def isGreaterThan(self, value):
		# comparison func based on the hash value
		minLen = min(len(self.value), len(value))
		for i in range(0, minLen):
			if self.lexicoHash[self.value[i]] < self.lexicoHash[value[i]]:
				return False
			elif self.lexicoHash[self.value[i]] > self.lexicoHash[value[i]]:
				return True

		if len(self.value) < len(value):
			return False
		return True

	def goLeftpushingParents(self, node):
		# utility func for toList(). push parent nodes into a list and return
		parents = []
		l = node
		while l.left is not None:
			parents.append(l)
			l = l.left
		if l.right is not None:
			parents.append(l)
			return None, parents
		return l, parents

	def toList(self):
		# in-order listing
		s = []
		l, parents = self.goLeftpushingParents(self)
		if l is not None:
			s.append(l.value)

		while len(parents) > 0:
			s.append(parents[-1].value)
			r = parents[-1].right
			if r is not None:
				l, p2 = self.goLeftpushingParents(r)
				if l is not None:
					s.append(l.value)
				parents = parents[:-1] + p2
			else:
				parents = parents[:-1]

		return s

# call this function to start
def lexicographicSort(strList, lexicoIndex):
	lex = LexicoBst(strList[0], lexicoIndex)
	for i in range(1, len(strList)):
		lex.insert(strList[i])

	print lex.toList()


if __name__ == '__main__':
	lexicographicSort(['b', 'abc', 'a', 'aa', 'c', 'cc', 'dcc', 'abd', 'abdd', 'dcd', 'd'], 'acbd')
	lexicographicSort(['c', '', 'dc', 'd'], 'dc')
