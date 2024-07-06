def exe_1198(_input):
    items = sorted([int(x) for x in _input.split(' ')])
    return items[1] - items[0]


def execute():
    while True:
        try:
            word = input()
        except EOFError:
            break
        print(exe_1198(word))


execute()
