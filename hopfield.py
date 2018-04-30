#!/usr/bin/python
# -*- coding: utf8 -*-
# Author: Shun Arahata
"""
Code for assignment
Hopfield Network
"""
import numpy as np


class Hopfield_Network():
    """Hopfield Network"""

    def __init__(self):
        """Constructor

        :param num_of_pattern: number of patterns to memorized
        """
        self.theta = np.zeros([25, 1])
        self.weight = np.zeros([5 * 5, 5 * 5])

    def train(self, *train):
        """ train weight Hebbian

        :param train: n times n train list
        """
        length = len(train)
        for i in range(length):
            train_flatten = np.ravel(train[i])
            self.weight += train_flatten @ train_flatten.T / length
        np.fill_diagonal(self.weight, 0)

    def potential_energy(self, input_flatten):
        """calculate lyapunov function

        :param input_flatten:input image (flatten)
        :return v:energy
        """
        v = -1 / 2 * input_flatten.T @ self.weight @ input_flatten
        v += self.theta.T @ input_flatten
        return v

    def recall(self, input, iter_num=10):
        """recall image from input

        :param input: 5 times 5 array
        :param iter_num: number of iterations
        :return:
        """
        input_flatten = np.ravel(input)
        energy_array = []
        for i in range(iter_num):
            index = np.random.randint(25)  # 0 to 24 random value
            energy_now = self.potential_energy(input_flatten)
            energy_array.append(energy_now)
            temp = input_flatten[:]
            temp[index] = 1 if temp[index] == 0 else 0
            energy_candidate = self.potential_energy(temp)
            print("now",energy_now)
            print("candidate",energy_candidate)
            print('----------')
            if energy_candidate < energy_now:
                input_flatten = temp[:]

        recall_img = np.reshape(input_flatten, (5, 5))
        return recall_img, energy_array


image_1 = np.array(
    [[0, 0, 1, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 1, 0, 0],
     [0, 0, 1, 0, 0]])


def test_1():
    hopfield = Hopfield_Network()
    hopfield.train(image_1)
    test = np.array([[0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0],
                     [0, 0, 1, 0, 0]])
    hoge, _ = hopfield.recall(test)
    print(hoge)

if __name__ == '__main__':
    test_1()