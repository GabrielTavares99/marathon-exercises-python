while True:
    data = input()
    datas = data.split(' ')
    if datas[0] == '0' and datas[1] == '0':
        break
    a = int(datas[0])
    b = int(datas[1])
    c = a + b
    print(f'{c}'.replace('0', ''))
