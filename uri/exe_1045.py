def exec_1045(_data):
    datas = sorted([float(x) for x in _data.split(' ')], reverse=True)
    _a = float(datas[0])
    _b = float(datas[1])
    _c = float(datas[2])

    result = []
    if _a >= _b + _c:
        result.append('NAO FORMA TRIANGULO')
        return result
    if _a * _a == (_b * _b) + (_c * _c):
        result.append('TRIANGULO RETANGULO')
    if _a * _a > (_b * _b) + (_c * _c):
        result.append('TRIANGULO OBTUSANGULO')
    if _a * _a < (_b * _b) + (_c * _c):
        result.append('TRIANGULO ACUTANGULO')
    if _a == _b == _c:
        result.append('TRIANGULO EQUILATERO')
    if len([i for i in [_a == _b, _a == _c, _b == _c] if i is True]) == 1:
        result.append('TRIANGULO ISOSCELES')

    return result


data = input()
items = exec_1045(data)
for item in items:
    print(item)
