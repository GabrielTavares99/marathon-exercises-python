def exe_3303(word):
    return 'palavrao' if len(word) >= 10 else 'palavrinha'


def execute():
    word = input()
    return exe_3303(word)


print(execute())
