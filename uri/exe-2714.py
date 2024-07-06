rounds = input()
for round_index in range(int(rounds)):
    ra = input()
    if 'RA' not in ra or len(ra) != 20:
        print('INVALID DATA')
        continue
    ra = ra.replace('RA', '')
    m = ''
    found = False
    for c in ra:
        if int(c) > 0:
            found = True
        if found:
            m = m + c
    print('INVALID DATA' if len(m) == 0 else m)
