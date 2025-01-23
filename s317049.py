
######### RESULTS FOR EACH PROBLEM #########

import numpy as np


## Problem 0
def f0(x: np.ndarray) -> np.ndarray:
    return np.add(x[0], np.divide(np.sin(x[1]), 5.07429872773508))

# Problem 1
def f1(x: np.ndarray) -> np.ndarray:
    return np.add(x[0], 
                  np.square(np.divide(0.28433252442033385, 9.820495733511379)))


# Problem 2
def f2(x: np.ndarray) -> np.ndarray:
    return np.multiply(
        np.square(np.multiply(8.09037463120157, 8.09037463120157)),
        np.multiply(
            np.subtract(8.09037463120157, -8.594501415099812),
            np.multiply(
                np.subtract(8.09037463120157, -8.594501415099812),
                x[0])))

# Problem 3
def f3(x: np.ndarray) -> np.ndarray:
    return np.subtract(
        np.add(
            np.multiply(x[0], x[0]),
            np.add(np.multiply(x[0], x[0]), 5.884993886295414)),
            np.multiply(x[1], np.multiply(x[1], x[1])))

# Problem 4
def f4(x: np.ndarray) -> np.ndarray:
    return np.add(
        np.add(np.add(np.add(np.add(np.add(
            np.add(np.add(np.log(9.599800492150578),
                          np.cos(x[1])), np.cos(x[1])),
                          np.cos(x[1])), np.cos(x[1])), 
                          np.cos(x[1])), np.cos(x[1])),
                          np.cos(x[1])), np.cos(np.subtract(x[1], x[1])))


# Problem 5
def f5(x: np.ndarray) -> np.ndarray:
    return np.power(
        np.subtract(x[1], x[1]),
        1.203572808700951)


# Problem 6
def f6(x: np.ndarray) -> np.ndarray:
    return np.add(np.subtract(x[1], x[0]),
                  np.subtract(np.subtract(x[1], np.divide(np.subtract(x[1], x[0]), 7.038301194783468)),
                              np.divide(np.subtract(x[1], x[0]), 7.038301194783468)))

# Problem 7
def f7(x: np.ndarray) -> np.ndarray:
    return np.add(np.square(np.add(x[0], x[1])),
                  np.multiply(np.add(np.cos(
                      np.multiply(np.arcsin(np.cos(
                          np.subtract(x[0], x[1]))),
                          np.multiply(np.arcsin(np.cos(np.subtract(x[0], x[1]))),
                                      np.multiply(np.arcsin(np.cos(np.subtract(x[0], x[1]))),
                                                  np.arcsin(np.cos(np.subtract(x[0], x[1]))))))),
                                                  np.square( np.multiply(np.arcsin(
                                                      np.cos(np.subtract(x[0], x[1]))),
                                                      np.multiply(np.arcsin(np.cos(
                                                          np.subtract(x[0], x[1]))),
                                                          np.arcsin(np.cos(np.subtract(x[0], x[1]))))))),
                                                          np.square(np.add(x[0], x[1]))))


# Problem 8

def f8(x: np.ndarray) -> np.ndarray:
    return np.subtract(23.82495597313178,
                       np.add(
                           np.square(-23.7940974885513),
                           np.multiply(x[1], x[1])))