import numpy as np

class Gaussian:
    def __init__(self, input_matrix):
        self.matrix = input_matrix


class IsSingular(Exception):
    raise "Matrix is Singular"


