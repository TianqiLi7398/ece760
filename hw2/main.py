# This file is the main file for the ECE 760 Graphic Probability Model in 2018 Fall, Texas A & M University.
# Author: Tianqi Li
# the file is the Problem 2 in hw2, which validate the d-sepration ALG for a DAG

import numpy as np
import graph
import sys


def output_1(graph, observe, source, end):
    # test if the end point is in the Y set
    Y = graph.D_sep(source, observe)
    if end in Y:
        return False
    else:
        return True


def main():

    infile = sys.argv[1]
    print(infile)

    g = {"a": ["d"],
         "b": ["d"],
         "c": ["e"],
         "d": ["g", "h"],
         "e": ["i"],
         "f": ["i", "j"],
         "g": ["k"],
         "h": ["k", "e"],
         "i": ["l"],
         "j": ["m"],
         "k": [],
         "l": [],
         "m": []
         }  # graph with all nodes and their children
    Graph = graph.DAG(g)

    problems = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    observes = [{'g', 'l'}, {'l'}, {'d'}, {'d', 'k', 'm'},
                {'c', 'g', 'l'}, {'k', 'e'}, {'l'}]
    sources = ['a', 'a', 'g', 'g', 'b', 'a', 'b']  # all source node
    ends = ['j', 'c', 'l', 'l', 'f']  # end point for prob a - e

    for i in range(5):
        print(problems[i], "). The flow can reach from node ",
              sources[i], "to node ", ends[i], " is ", output_1(Graph, observes[i], sources[i], ends[i]))

    for i in range(2):
        i += 5
        print(problems[i], "). The Y set contains all nodes are d-separated from ",
              sources[i], ", given Z = ", observes[i], " are Y = ", Graph.D_sep(sources[i], observes[i]))


if __name__ == "__main__":
    main()
