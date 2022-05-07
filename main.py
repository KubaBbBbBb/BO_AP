from math import inf
import numpy as np
import copy

class Hungary:

    def __init__(self, tab, fi = 0):
        self.tab = tab
        self.fi = fi
        self.copy_tab = tab

    def reduction_row(self):
        min = inf
        for i in self.copy_tab:
            min = i.min()
            i -= min
            self.fi += min

        return self.copy_tab

    def reduction_col(self):
        min = inf
        for j in self.copy_tab.T:
            min = j.min()
            j -= min
            self.fi += min

        return self.copy_tab

    def zero_independent(self):
        list_row = []
        list_col = []
        for i in range(0, len(self.copy_tab)):
            for j in range(0, len(self.copy_tab[i])):
                if self.copy_tab[i][j] == 0:
                    if i not in list_row and j not in list_col:
                        self.copy_tab[i][j] = -1
                        list_row.append(i)
                        list_col.append(j)

        return self.copy_tab

    def cross(self):
        matrix = copy.deepcopy(self.copy_tab)
        row_of_zeros = []
        col_of_zeros = []
        for i in matrix:
            row_of_zeros.append(len(i[i == 0]) + len(i[i == -1]))
        for j in matrix.T:
            col_of_zeros.append(len(j[j == 0]) + len(j[j == -1]))

        return row_of_zeros, col_of_zeros







m = np.array([[5, 2, 3, 2, 7], [6, 8, 4, 2, 5], [6, 4, 3, 7, 2],
              [6, 9, 0, 4, 0], [4, 1, 2, 4, 0]])

Matrix = Hungary(m)
Matrix.reduction_row()
Matrix.reduction_col()
print(Matrix.zero_independent())
print(Matrix.cross())


