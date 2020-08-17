data = input()
data = data.split(' ')

qtd_comp, qtd_sheets, qtd_sheets_comp = int(data[0]), int(data[1]), int(data[2])

inside_limit = qtd_sheets_comp * qtd_comp <= qtd_sheets

print('S' if inside_limit else 'N')
