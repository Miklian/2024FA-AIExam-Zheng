class Problem:
    def __init__(self, j1, j2, j3, goal):
        #size is the capacities of the jar
        self.size1 = j1
        self.size2 = j2
        self.size3 = j3
        self.start = (0, 0, 0)
        self.goal = [(goal, 0, 0), (0, goal, 0), (0, 0, goal)]
    def startState(self):
        return self.start
    def isGoal(self, node):
        return node in self.goal
    def nextStates(self, node):
        neighbors = []
        j12, j8, j3 = node
        # fill jar1:
        if j12<self.size1:
            neighbors.append (((self.size1, j8, j3), 'Fill jar 1'))
        # Fill jar2:
        if j8<self.size2:
            neighbors.append (((j12, self.size2, j3), 'Fill jar 2'))
        # Fill jar3:
        if j3<self.size3:
            neighbors.append (((j12, j8, self.size3), 'Fill jar 3'))
        # Empty jar1:
        if j12>0: neighbors.append (((0, j8, j3), 'Empty jar 1'))
        # Empty jar2:
        if j8>0: neighbors.append (((j12, 0, j3), 'Empty jar 2'))
        # Empty jar2:
        if j3>0: neighbors.append (((j12, j8, 0), 'Empty jar 3'))

        # pour jar12 to jar8:
        left_jar1 = self.size2 - j8
        if j12>0 and left_jar1>0:
            if left_jar1 > j12:
                neighbors.append (((0, j8+j12, j3), 'pour jar 1 into jar 2'))
            else:
                neighbors.append (((j12 - left_jar1, self.size2, j3), 'pour jar 1 into jar 2'))

        # pour jar12 to jar3:
        left_jar2 = self.size3 - j3
        if j12>0 and left_jar2>0:
            if left_jar2 > j12:
                neighbors.append (((0, j8, j3+j12), 'pour jar 1 into jar 3'))
            else:
                neighbors.append (((j12 - left_jar2, j8, self.size3), 'pour jar 1 into jar 3'))

        # pour jar8 to jar12:
        left_jar3 = self.size1 - j12
        if j8>0 and left_jar3>0:
            if left_jar3 > j8:
                neighbors.append (((j12+j8, 0, j3), 'pour jar 2 into jar 1'))
            else:
                neighbors.append (((self.size1, j8 - left_jar3, j3), 'pour jar 2 into jar 1'))

        # pour jar8 to jar3:
        left_jar4 = self.size3 - j3
        if j8>0 and left_jar4>0:
            if left_jar4 > j8:
                neighbors.append (((j12, 0, j3+j8), 'pour jar 2 into jar 3'))
            else:
                neighbors.append (((j12, j8 - left_jar4, self.size3), 'pour jar 2 into jar 3'))

        # pour jar3 to jar12:
        left_jar5 = self.size1 - j12
        if j3>0 and left_jar5>0:
            if left_jar5 > j3:
                neighbors.append (((j12+j3, j8, 0), 'pour jar 3 into jar 1'))
            else:
                neighbors.append (((self.size1, j8, j3 - left_jar5), 'pour jar 3 into jar 1'))

        # pour jar3 to jar8:
        left_jar6 = self.size2 - j8
        if j3>0 and left_jar6>0:
            if left_jar6 > j3:
                neighbors.append (((j12, j8+j3, 0), 'pour jar 3 into jar 2'))
            else:
                neighbors.append (((j12, self.size2, j3 - left_jar6), 'pour jar 3 into jar 2'))

        #print(j12, j8, j3)
        return neighbors










