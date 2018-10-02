# ece 760 HW2

This file is the homework 2: d-separation finding Algorithm.

To run for results, please run 'test.py', which contains problem

1. a - e are the problems of given observation set and start node in a DAG (Directed Aclylic Graph), to analyze if the start node could influence end node;

2. f - g are the problems of given observation set and start node in a DAG, provide the set of nodes Y that are d-separated.

The library file graph.py defines the class of DAG, which contains function DAG.D_sep() that returns set of nodes Y that are d-separated from source node given observation.
