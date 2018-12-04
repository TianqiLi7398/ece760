# ECE 760 Final project

## Part 2. Pearl's Message Passing Alogirthm - inference application in human error prediction

Please check the [link](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6837128) for the model.

In this floder, there are three python 3.5 files to complete the inference problem.

* [graph.py](https://github.com/TianqiLi7398/ece760/tree/master/project/graph.py): this is the file to initialize a BN clasee named 'DAG'
* [pearl.py](https://github.com/TianqiLi7398/ece760/blob/master/project/pearl.py): this contains an inherit class of 'DAG', named Pearls, which has the main functions of pearl's message passing alg.

* [main.py](https://github.com/TianqiLi7398/ece760/blob/master/project/main.py): this is the executable file for inference. The BN strucuture, CPDs and all inference questions are hand coded inside.

### Instruction
To get the solution of first part project, please run
```
$ python main.py
```
to get results.

All inference will be printed in the terminal.


