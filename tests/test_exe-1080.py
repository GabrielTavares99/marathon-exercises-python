import pytest

from uri.exe_1080 import exe_1080

_inputs = [
    ([1, 10, 2], 10, 2),
    ([10, 1, 2], 10, 1),
    ([2, 1, 10], 10, 3),
]


@pytest.mark.parametrize("_inputs, base, position", _inputs)
def test_exe_1080(_inputs, base, position):
    response_base, response_position = exe_1080(_inputs)
    assert base == response_base
    assert position == response_position
