# This file is the main file for the ECE 760 Graphic Probability Model in 2018 Fall, Texas A & M University.
# Author: Tianqi Li
# the file is the part 1 for final project, which implement the Pearl's message passing ALG
#
# few notation in this code:
# pi_X(Z=z_value) is pi_msg[Z][X][z_value]
# lamda_X(Z = z_value) is lamda_msg[Z][X][z_value]

import numpy as np
from graph import DAG
import sys
from pearl import Pearls
from pearl import solver
import copy


def main():

    g = {"a": ["c"],
         "b": ["c"],
         "c": ["d", "e"],
         "d": ["f", "g"],
         "e": [],
         "f": [],
         "g": []
         }

    marginal = {"a": {1: 0.7, 0: 0.3},
                "b": {1: 0.4, 0: 0.6},
                "c": {1, 0},
                "d": {1, 0},
                "e": {1, 0},
                "f": {1, 0},
                "g": {1, 0}
                }
    CPD = {"a": [],
           "b": [],
           "c": [["a", "b"], [[0.1, 0.5], [0.3, 0.9]]],
           "d": [["c"], [0.8, 0.3]],
           "e": [["c"], [0.2, 0.6]],
           "f": [["d"], [0.1, 0.7]],
           "g": [["d"], [0.9, 0.4]]
           }

    questions = [[["a"], ["b"], [1], [0]],
                 [["a"], ["d"], [
                     1], [0]],
                 [["a"], ["d", "b"], [
                     1], [0, 0]],
                 [["a"], ["d", "g"], [
                     1], [0, 1]],
                 [["b"], ["a"], [
                     1], [1]],
                 [["b"], ["c"], [
                     1], [1]],
                 [["b"], ["a", "c"], [
                     1], [1, 1]],
                 [["b"], ["c", "f"], [
                     1], [1, 0]],
                 [["c"], [], [
                     1], []],
                 [["c"], ["a"], [
                     1], [1]],
                 [["c"], ["a", "b"], [
                     1], [1, 0]],
                 [["c"], ["d"], [
                     1], [0]],
                 [["c"], ["d", "f"], [
                     1], [0, 0]],
                 [["d"], [], [
                     1], []],
                 [["d"], ["e"], [
                     1], [0]],
                 [["d"], ["c", "e"], [
                     1], [0, 0]],
                 [["d"], ["b", "g"], [
                     1], [1, 0]],
                 [["d"], ["b", "g", "f"], [
                     1], [1, 0, 1]],
                 [["e"], [], [
                     1], []],
                 [["e"], ["c"], [
                     1], [1]],
                 [["e"], ["f"], [
                     1], [0]],
                 [["e"], ["c", "f"], [
                     1], [1, 0]],
                 [["e"], ["a", "b"], [
                     1], [1, 1]],
                 [["f"], [], [
                     1], []],
                 [["f"], ["a"], [
                     1], [1]],
                 [["f"], ["a", "c"], [
                     1], [1, 0]],
                 [["f"], ["a", "c", "e"], [
                     1], [1, 0, 0]],
                 [["f"], ["b", "g"], [
                     1], [1, 0]],
                 [["g"], [], [
                     1], []],
                 [["g"], ["c"], [
                     1], [0]],
                 [["g"], ["c", "d"], [
                     1], [0, 0]],
                 [["g"], ["e"], [
                     1], [0]],
                 [["g"], ["a", "b"], [
                     1], [0, 1]],
                 [["a", "d"], ["f", "b"], [
                     1, 1], [0, 1]],
                 [["c", "e"], ["f", "g"], [
                     0, 1], [1, 0]],
                 [["f", "b"], ["g", "e"], [
                     0, 1], [0, 1]],
                 [["g", "b"], ["f", "a"], [1, 0], [1, 0]]]

    # A = Pearls(
    #     g, marginal, CPD)
    # A.update_network(
    #     "c", 0)
    # print(
    #     A.cpd)
    answers = solver(
        g, marginal, CPD, questions)


if __name__ == "__main__":
    main()
