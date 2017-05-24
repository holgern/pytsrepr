# Copyright (c) 2017 Holger Nahrstaedt
# See LICENSE for license details.

from __future__ import division, print_function, absolute_import
import numpy as np


def paa(data, nseg):

    data_len = np.size(data)
    data_len = data_len - (data_len % nseg)
    data = data[0:data_len]
    win_size = int(np.floor(data_len / nseg))

    if (data_len == nseg):
        PAA = data
    else:
        PAA = np.mean(np.reshape(data, (nseg, win_size)), axis=1)
    return PAA
