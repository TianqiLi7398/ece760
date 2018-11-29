import numpy as np
from graph import DAG
import sys
import copy


class Pearls(DAG):

    def __init__(self,  graph_dict, marginal, CPD):

        DAG.__init__(
            self,  graph_dict)
        self.E, self.e = [], []
        self.value = [
            0, 1]
        self.lamda = dict.fromkeys(
            graph_dict.keys())
        self.pi = dict.fromkeys(
            graph_dict.keys())
        self.lamda_msg = dict.fromkeys(
            graph_dict.keys())
        self.pi_msg = dict.fromkeys(
            graph_dict.keys())

        self.cpd = dict.fromkeys(
            graph_dict.keys())

        for x in self.vertices:
            self.lamda[x], self.lamda_msg[x], self.pi[x], self.pi_msg[x], self.cpd[x] = {
            }, {}, {}, {}, {}

#         given info of the graph
        self.marginal = marginal
        self.CPD = CPD

        self.get_root()
#         initialize laumda
        for x in self.vertices:
            for x_value in self.value:
                self.lamda[x][x_value] = 1

#         initialize lamuda_msg
            for z in self.parents[x]:
                self.lamda_msg[z][x] = {
                }
                for z_value in self.value:
                    self.lamda_msg[z][x][z_value] = 1

#          initialize pi_msg
            for y in self.graph_dict[x]:

                self.pi_msg[x][y] = {
                }
                for x_value in self.value:
                    self.pi_msg[x][y][x_value] = 1


#         send pi_message
        for R in self.root:
            for r_value in self.value:
                self.pi[R][r_value] = self.marginal[R][r_value]
                self.cpd[R][r_value] = self.marginal[R][r_value]

            for W in self.graph_dict[R]:
                self.send_pi_msg(
                    R, W)

    def get_root(self):
        self.root = []
        for x in self.vertices:
            if self.parents[x] == []:
                self.root.append(
                    x)
        return

    def send_pi_msg(self, Z, X):
        #         Z is parent node, X is child node

        #         get all parent of Z:
        U = copy.deepcopy(
            self.graph_dict[Z])
        U.remove(
            X)
        for z_value in self.value:
            self.pi_msg[Z][X][z_value] = self.pi[Z][z_value]

            if U != None:
                for u in U:

                    self.pi_msg[Z][X][z_value] = self.pi_msg[Z][X][z_value] * \
                        self.lamda_msg[Z][u][z_value]

        P_tilta = []
        if X not in self.E:
            for x_value in self.value:
                [zs, probs] = self.CPD[X]
                total = self.calculate_pi(
                    X, x_value, zs, probs)
                self.pi[X][x_value] = total
                P_tilta.append(
                    self.lamda[X][x_value] * self.pi[X][x_value])

            self.normalize(
                X, P_tilta)

            for Y in self.graph_dict[X]:
                self.send_pi_msg(
                    X, Y)

        for x_value in self.value:
            if self.lamda[X][x_value] != 1:
                other_parents = copy.deepcopy(
                    self.parents[X])
                other_parents.remove(
                    Z)
                if other_parents != None:
                    for W in other_parents:
                        if W not in self.E:
                            self.send_lamda_msg(
                                X, W)

        return

    def calculate_pi(self, X, x, zs, probs):
        #         X: node name of X, x is value of the X node
        #         zs are node names of all other parents
        #         probs will be a 2^n dimentional matrix for n parents
        k = len(
            zs)

        prob_matrix = np.matrix(
            probs)
        prob_matrix = prob_matrix.flatten()
        total = 0

        for i in range(2**k):

            if x == 1:
                p = prob_matrix[0, i]
            else:
                p = 1 - \
                    prob_matrix[0, i]

            for j in range(k):
                if i - 2**(k-j-1) + 1 > 0:
                    #                     this means z_k value is 1
                    p = p * \
                        self.pi_msg[zs[j]
                                    ][X][1]
                    i = i - \
                        2**(k-j-1)
                else:
                    p = p * \
                        self.pi_msg[zs[j]
                                    ][X][0]
            total += p
        return total

    def normalize(self, X, P):
        sum_ = 0
        for i in self.value:
            sum_ += P[i]
        for x_value in self.value:
            self.cpd[X][x_value] = P[x_value] / sum_

    def calculate_lamda(self, X, x, Y, zs, probs):
        k = len(
            zs)

        prob_matrix = np.matrix(
            probs)
        prob_matrix = prob_matrix.flatten()
        total = 0
        x_index = zs.index(
            X)

        for y in self.value:

            for i in range(2**k):

                if y == 1:
                    p = prob_matrix[0, i]
                else:
                    p = 1 - \
                        prob_matrix[0, i]

                for j in range(k):
                    if i - 2**(k-j-1) + 1 > 0:
                        #                     this means z_k = 1
                        if j == x_index:
                            #                             pass x
                            if x != 1:
                                p = 0
                            else:
                                p = p

                        else:
                            p = p * \
                                self.pi_msg[zs[j]
                                            ][Y][1]

                        #   update i
                        i = i - \
                            2**(k-j-1)
                    else:
                        #                         this means z_k = 0

                        if j == x_index:
                            #             pass x
                            if x != 0:
                                p = 0
                            else:
                                p = p
                        else:
                            p = p * \
                                self.pi_msg[zs[j]
                                            ][Y][0]

                total += p * \
                    self.lamda[Y][y]
        return total

    def send_lamda_msg(self, Y, X):
        #         Y(child) -> X(parent)

        P_tilta = []

        for x_value in self.value:
            [zs, probs] = self.CPD[Y]
            self.lamda_msg[X][Y][x_value] = self.calculate_lamda(
                X, x_value, Y, zs, probs)

            lamda = 1

#             calculate lamuda(x)
            for u in self.graph_dict[X]:
                lamda = lamda * \
                    self.lamda_msg[X][u][x_value]
            self.lamda[X][x_value] = lamda

            P_tilta.append(
                self.lamda[X][x_value] * self.pi[X][x_value])

#         get self.cpd
        self.normalize(
            X, P_tilta)

        for Z in self.parents[X]:
            if Z not in self.E:
                self.send_lamda_msg(
                    X, Z)

        for U in self.graph_dict[X]:
            if U != Y:
                self.send_pi_msg(
                    X, U)

        return

    def update_network(self, V, v_value_hat):

        self.E.append(
            V)
        self.e.append(
            (V, v_value_hat))

        for v in self.value:
            if v == v_value_hat:
                self.lamda[V][v] = 1
                self.pi[V][v] = 1
                self.cpd[V][v] = 1
            else:
                self.lamda[V][v] = 0
                self.pi[V][v] = 0
                self.cpd[V][v] = 0

        for Z in self.parents[V]:
            if Z not in self.E:
                self.send_lamda_msg(
                    V, Z)

        for Y in self.graph_dict[V]:
            self.send_pi_msg(
                V, Y)

        return


def solver(g, marginal, CPD, questions):
    '''
    This function is for solving the CPD inference,
    P(X = x|E = e)
    '''
    Answers = []
    for q in questions:

        A = Pearls(
            g, marginal, CPD)
        answer = 1
        [X, E, x,
            e] = q
        for i in range(len(E)):
            A.update_network(
                E[i], e[i])

#         if len(X) > 1:
        for j in range(len(X)):
            answer = answer * \
                A.cpd[X[j]
                      ][x[j]]
            A.update_network(
                X[j], x[j])
#                 answer = answer * A.cpd[X[j]][x[j]]

#         answer = answer * A.cpd[X[-1]][x[-1]]
        print("P(", X, "=", x, " | e = ",
              E, "=", e, ") = ", answer)
        Answers.append(
            answer)
    return Answers
