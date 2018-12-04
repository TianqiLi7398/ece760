# This file is the main file for the ECE 760 Graphic Probability Model in 2018
# Fall, Texas A & M University.
# Author: Tianqi Li
# the file is the Problem 1 in hw2, which constructs a class called DAG and
# executes the d-separate searching ALG to return set Y of all vertices that is
# d-separated from the source vertex given observation Z.
from collections import deque


class DAG(object):
    # This class is used for Directed Acyclic Graph, which same vertex cannot
    # be met twice in a path

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict  # includes all nodes with their children
        self.parents = dict.fromkeys(self.graph_dict.keys())
        for key in self.parents:
            self.parents[key] = []  # initilize the self.parents list
        self.get_vertex()
        self.get_parent()

    def get_vertex(self):
        # get the list of all vertices, which is stored in self.vertices
        self.vertices = sorted(self.graph_dict.keys())

    def get_parent(self):
        # get the parents of all vertices, which is stored in self.parents
        for vertex in self.vertices:
            for i in self.vertices:
                if vertex in self.graph_dict[i]:
                    self.parents[vertex].append(i)

    def get_A(self, observe):
        # this function gets all parents of the observation Z, which is used to
        # check V-constructs
        L, A = deque(), list()
        for i in observe:
            L.append(i)
        while len(L) != 0:
            n = L.popleft()
            if n not in A:
                for par in self.parents[n]:
                    L.append(par)
            A.append(n)
        return sorted(A)  # return the set A= {parents of Z}

    def D_sep(self, sn, observe):
        # This algorithm returns
        # Y ={d-separated nodes from sn | observation set Z}
        # Reference: P75 Algorithm 3.1 in Probabilisitc Graphic Model: Principles and Techniques
        # Input: (sn: start node, observe: observation)
        # Output: Y ={d-separated nodes from sn | observation set Z}

        L, V, R = deque(), list(), list()
        # L: a queue of tuples of (node, direction) to visit
        # specificly, direction :
        # 'forward' same direction with the edge, 'backward' is opposite
        # V: visited nodes
        # R: all reachable nodes
        L.append((sn, 'backward'))
        A = self.get_A(observe)

        while len(L) != 0:
            (node, direction) = L.popleft()
            # pop the first node out of the queue
            if (node, direction) not in V:
                # the node + direction is not visited
                if node not in observe and node not in R:
                    R.append(node)
                V.append((node, direction))  # mark node + direction visited
                if direction == 'backward' and node not in observe:
                    for z in self.parents[node]:
                        # evidential trail
                        L.append((z, 'backward'))
                    for z in self.graph_dict[node]:
                        # common cusal trail
                        L.append((z, 'forward'))
                elif direction == 'forward':
                    if node not in observe:
                        # causal trail
                        for z in self.graph_dict[node]:
                            L.append((z, 'forward'))
                    if node in A:
                        # there is a activated V- structure, so trace the parents
                        for z in self.parents[node]:
                            L.append((z, 'backward'))
        return sorted(self.graph_dict.keys() - R - observe)  # Y =  All nodes - R - Z
