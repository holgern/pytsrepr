# Copyright (c) 2017-2019 Holger Nahrstaedt
# See LICENSE for license details.

from __future__ import division, print_function, absolute_import
import numpy as np


class PAA(object):
    """
    This class is for generation of piecewise aggregate approximations
    
    """

    def __init__(self, nseg, func = None):

        self.func = func
        self.nseg = nseg

    def apply(self, data):
    
        data_len = np.size(data)
        data_len = data_len - (data_len % self.nseg)
        data = data[0:data_len]
        win_size = int(np.floor(data_len / self.nseg))
    
        if (data_len == self.nseg):
            out = data
        elif self.func is None:
            out = np.mean(np.reshape(data, (self.nseg, win_size)), axis=1)
        else:
            out = self.func(np.reshape(data, (self.nseg, win_size)), axis=1)
        return out
