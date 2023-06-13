import os
from pathlib import Path

import numpy as np

from kwave.utils.interp import get_delta_bli
from tests.matlab_test_data_collectors.python_testers.utils.record_reader import TestRecordReader


def test_make_cart_rect():
    test_record_path = os.path.join(Path(__file__).parent, 'collectedValues/getDeltaBLI.mat')
    reader = TestRecordReader(test_record_path)

    for i in range(len(reader)):
        Nx = reader.expected_value_of('Nx')
        dx = reader.expected_value_of('dx')
        xgrid = reader.expected_value_of('x_grid')
        position = reader.expected_value_of('position')
        include_imag = reader.expected_value_of('include_imag')
        f_grid = get_delta_bli(Nx, dx, xgrid, position, include_imag)

        assert np.allclose(f_grid, reader.expected_value_of('f_grid'))
        reader.increment()

    print('get_delta_bli(..) works as expected!')
