
x = {'a': 1, 'b': 2, 'c': 3}
y = {'c': 3, 'd': 4, 'e': 5}

x_and_y = x | y
xy = {}

for key in x_and_y:
    if key in x and key in y:
        xy[key] = [x[key], y[key]]
    elif key in x:
        xy[key] = [x[key], None]
    else:
        xy[key] = [None, y[key]]
print(xy)
