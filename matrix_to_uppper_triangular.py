import numpy as np

class Gaussian:
    __matrix = np.ndarray([], dtype=float)
    def __init__(self, input_matrix: np.ndarray):
        self.__matrix = input_matrix

    def convert_to_echelon(self):
        pass


class IsSingular(Exception):
    pass