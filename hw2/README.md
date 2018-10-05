# ECE 760 HW2

## Question 1. Finding d-separated nodes

A py script is built to get info from txt files and output txt file with all d-separated nodes. All code is generated in python 3.5.5. The library file `graph.py` defines the class of DAG, which contains function `DAG.D_sep()` that returns set of nodes Y that are d-separated from source node given observation.

### Instruction
With txt file put in the same folder with main.py file, we can run
```
$ python main.py filename.txt
```
to get results.

A `result.txt` will be generated in the same flolder.

## Question 2. HW1 queries

In HW1, the queries are

1. a - e are the problems of given observation set and start node in a DAG (Directed Aclylic Graph), to analyze if the start node could influence end node;

2. f - g are the problems of given observation set and start node in a DAG, provide the set of nodes Y that are d-separated.

Because the trivial queries do not fit the txt format given by instructor, I hand code the all queries in code, to get result of HW1, please run
```
$ python main.py hw1
```
