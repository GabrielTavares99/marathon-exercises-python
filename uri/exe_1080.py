def exe_1080(_numbers):
    _base = 0
    _position = 0
    index = 1
    for number in _numbers:
        if number > _base:
            _base = number
            _position = index
        index += 1
    return _base, _position


numbers = []
for i in range(100):
    numbers.append(int(input()))

base, position = exe_1080(numbers)
print(base)
print(position)
