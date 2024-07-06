import pytest

from uri.exe_1045 import exec_1045

inputs_exe_1045 = [
    ('7.0 5.0 7.0', ['TRIANGULO ACUTANGULO', 'TRIANGULO ISOSCELES']),
    ('6.0 6.0 10.0', ['TRIANGULO OBTUSANGULO', 'TRIANGULO ISOSCELES']),
    ('6.0 6.0 6.0', ['TRIANGULO ACUTANGULO', 'TRIANGULO EQUILATERO']),
    ('5.0 7.0 2.0', ['NAO FORMA TRIANGULO']),
    ('6.0 8.0 10.0', ['TRIANGULO RETANGULO']),
]


@pytest.mark.parametrize("ab, a", inputs_exe_1045)
def test_exe_1045(ab, a):
    results = exec_1045(ab)
    for ab in a:
        assert ab in results
