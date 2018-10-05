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


def result_hw1():
    # to aviod trivial query in hw1, I hand coded the queries.
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

    # initialize graph
    Graph = graph.DAG(g)

    problems = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    observes = [{'g', 'l'}, {'l'}, {'d'}, {'d', 'k', 'm'},
                {'c', 'g', 'l'}, {'k', 'e'}, {'l'}]
    sources = ['a', 'a', 'g', 'g', 'b', 'a', 'b']  # all source node
    ends = ['j', 'c', 'l', 'l', 'f']  # end point for prob a - e

    for i in range(5):
        print(problems[i], "). Y = ", Graph.D_sep(sources[i], observes[i]), " The flow can reach from node ",
              sources[i], "to node ", ends[i], " is ", output_1(Graph, observes[i], sources[i], ends[i]))

    for i in range(2):
        i += 5
        print(problems[i], "). The Y set contains all nodes are d-separated from ",
              sources[i], ", given Z = ", observes[i], " are Y = ", Graph.D_sep(sources[i], observes[i]))
    return


def read_txt(filename):
    # this function opens a txt file, convert contains to graph and queries

    # open file
    file = open(filename, 'r')
    a = file.read().split('\n')

    # first line read V, M, Q
    # where V and M are the number of nodes and edges in the BN, respectively,
    # Q is the number of queries
    try:
        V, M, Q = list(map(int, a[0].split(' ')))
    except ValueError:
        return print("first line is not V, M, Q pattern, please check :)")

    g, L = dict(), []  # g is the graph structure, L is all keys of the graph
    for i in range(M):
        # explore all vertices in all edges
        try:
            L.append(a[i+1].split(' ')[0])
            L.append(a[i+1].split(' ')[1])
        except IndexError:
            return print('edges are not well determind at', i+1, 'th line.')
    # initialize the graph by giving all keys
    keys = set(L)
    # check correctness of V value
    if len(keys) != V:
        print('V is not the number of vertices, while it is ', V, '.')
        return
    # add children to each vertices
    for key in keys:
        g[key] = []
    for i in range(M):
        try:
            g[a[i+1].split(' ')[0]].append(a[i+1].split(' ')[1])  # check edge is complete
        except IndexError:
            return print('edge is not well determind at', i+1, 'th line :(')
    # graph is constructed completed!

    # grab queries info
    observes, sources = [], []
    for i in range(Q):
        # queries are in 'source | observation' mode
        if a[i + M + 1].find('|') < 0:
            print('The query in', i + M + 2, 'th line is not complete :)')
            return
        sources.append(a[i + M + 1].split('|')[0].split(' ')[0])
        observes.append(set(a[i + M + 1].split('|')[1][1:].split(' ')))

    return g, observes, sources


def main():

    filename = sys.argv[1]
    # print(infile)

    if filename == 'hw1':
        # output the result of hw1
        result_hw1()
        return
    else:
        g, observes, sources = read_txt(filename)

    # start calculating, initilize the graph structure
    Graph = graph.DAG(g)

    import string
    # show the results
    Y = []
    for i in range(len(observes)):
        result = Graph.D_sep(sources[i], observes[i])
        print(string.ascii_lowercase[i], "). The Y set contains all nodes are d-separated from ",
              sources[i], ", given Z = ", observes[i], " are Y = ", result)
        Y.append(result)
    # write all Ys into stdout.txt
    output = open('stdout.txt', 'w')
    for y in Y:
        #     print(" ".join(y))
        output.writelines(" ".join(y)+'\n')
    output.close()


if __name__ == "__main__":
    main()
