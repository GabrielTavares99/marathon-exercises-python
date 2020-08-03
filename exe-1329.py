while True:
    if input() == '0':
        break
    scoreboard = {
        'M': 0,
        'J': 0
    }
    for i in input().split(' '):
        owner = 'M' if i == '0' else 'J'
        scoreboard[owner] = scoreboard[owner] + 1
    print('Mary won {} times and John won {} times'.format(scoreboard['M'], scoreboard['J']))
