# This file is the main file for the ECE 760 Graphic Probability Model in 2018 Fall, Texas A & M University.
# Author: Tianqi Li
# the file is the part 2 for final project, which implement the Pearl's message
# passing ALG in a human error preditction model
#
# few notation in this code:
# pi_X(Z=z_value) is pi_msg[Z][X][z_value]
# lamda_X(Z = z_value) is lamda_msg[Z][X][z_value]

import numpy as np
from graph import DAG
import sys
from pearl import Pearls
import copy


def main():

    g = {"t": ["w"],
         "o": ["w"],
         "q": ["s"],
         "r": ["s"],
         "a": ["p"],
         "w": ["p"],
         "e": ["f"],
         "i": ["f"],
         "p": ["h"],
         "f": ["h"],
         "s": ["h"],
         "h": []
         }

    marginal = {"t": {0: 0.1, 1: 0.3, 2: 0.6},
                "o": {0: 0.05, 1: 0.2, 2: 0.75},
                "q": {0: 0.05, 1: 0.15, 2: 0.8},
                "r": {0: 0.1, 1: 0.2, 2: 0.7},
                "a": {0: 0.2, 1: 0.3, 2: 0.5},
                "w": {0: [], 1: [], 2: []},
                "e": {0: 0.1, 1: 0.4, 2: 0.5},
                "i": {0: 0.1, 1: 0.3, 2: 0.6},
                "p": {0: [], 1: [], 2: []},
                "f": {0: [], 1: [], 2: []},
                "s": {0: [], 1: [], 2: []},
                "h": {0: [], 1: []}
                }

    CPD = {"t": [],
           "o": [],
           "q": [],
           "r": [],
           "a": [],
           "w": {0: [["t", 'o'], [[0.01, 0.05, 0.2], [0.05, 0.1, 0.8], [0.2, 0.8, 0.9]]],
                 1: [["t", 'o'], [[0.09, 0.15, 0.6], [0.15, 0.8, 0.15], [0.6, 0.15, 0.09]]],
                 2: [["t", 'o'], [[0.9, 0.8, 0.2], [0.8, 0.1, 0.05], [0.2, 0.05, 0.01]]]},
           "e": [],
           "i": [],
           "p": {0: [["a", 'w'], [[0.2, 0.05, 0.01], [0.6, 0.1, 0.1], [0.9, 0.8, 0.3]]],
                 1: [["a", 'w'], [[0.5, 0.15, 0.09], [0.3, 0.7, 0.3], [0.09, 0.15, 0.5]]],
                 2: [["a", 'w'], [[0.3, 0.8, 0.9], [0.1, 0.2, 0.6], [0.01, 0.05, 0.2]]]},
           "f": {0: [["e", 'i'], [[0.9, 0.8, 0.6], [0.4, 0.15, 0.1], [0.2, 0.1, 0.01]]],
                 1: [["e", 'i'], [[0.09, 0.15, 0.3], [0.5, 0.7, 0.5], [0.6, 0.2, 0.09]]],
                 2: [["e", 'i'], [[0.01, 0.05, 0.1], [0.1, 0.15, 0.4], [0.2, 0.7, 0.9]]]},
           "s": {0: [["q", 'r'], [[0.9, 0.7, 0.2], [0.7, 0.2, 0.1], [0.2, 0.1, 0.01]]],
                 1: [["q", 'r'], [[0.09, 0.2, 0.6], [0.2, 0.6, 0.6], [0.6, 0.3, 0.09]]],
                 2: [["q", 'r'], [[0.01, 0.1, 0.2], [0.1, 0.2, 0.3], [0.2, 0.6, 0.9]]]},
           "h": {0: [['p', 'f', 's'], [[[0.3, 0.5, 0.7], [0.5, 0.8, 0.9], [0.7, 0.9, 0.99]],
                                       [[0.8, 0.4, 0.5], [0.3, 0.6, 0.8], [0.5, 0.8, 0.9]],
                                       [[0.01, 0.1, 0.3], [0.2, 0.4, 0.5], [0.3, 0.5, 0.7]]]],
                 1: [['p', 'f', 's'], [[[0.7, 0.5, 0.3], [0.5, 0.2, 0.1], [0.3, 0.1, 0.01]],
                                       [[0.2, 0.6, 0.5], [0.7, 0.4, 0.2], [0.5, 0.2, 0.1]],
                                       [[0.99, 0.9, 0.7], [0.8, 0.6, 0.5], [0.7, 0.5, 0.3]]]]},
           }
    # all inference
    A = Pearls(g, marginal, CPD)
    print('the prior probability', A.cpd)
    # get the Posterior probability
    A.update_network('h', 1)
    print('the posterior probability', A.cpd)
    # calculae the h=1 given different root condition
    print('calculae the h=1 given different root condition')
    for r in A.root:
        A = Pearls(g, marginal, CPD)
        A.update_network(r, 0)
        print(r, 'caused the error probability is', A.cpd['h'][1])


if __name__ == "__main__":
    main()
