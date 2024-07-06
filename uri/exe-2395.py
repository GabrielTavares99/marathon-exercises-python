container = input()
ship = input()
container = container.split(' ')
ship = ship.split(' ')
a, b, c = int(container[0]), int(container[1]), int(container[2])
x, y, z = int(ship[0]), int(ship[1]), int(ship[2])

qtd_containers = int(x / a) * int(y / b) * int(z / c)
print(qtd_containers)
