x = [-1.5, 4.5, -3.75, 1, -3, 4, -1, 3.25, -1, 2]

y = [2, -3, 3, -1, 1.5, -2, 1, -3.5, 1, -2.75, 2.25, -2.0]


i = 0
j = 0

# calcul distances
x = [abs(i) for i in x]
y = [abs(i) for i in y]


def calcul_points(x):
    x_pos = []
    x_sum = 0
    for i in x:
        x_sum += i
        x_pos.append(x_sum)
    return x_pos


def merge_points(x, y):
    z = x
    z.extend(y)
    z.sort()
    z = list(set(z))
    return z


def asynch_vertlines(x, y):
    """
    get points to draw vertline in asynchron case
    """
    # calcul distances
    x = [abs(i) for i in x]
    y = [abs(i) for i in y]
    x_pos = []
    x_sum = 0
    for i in x:
        x_sum += i
        x_pos.append(x_sum)
    y_pos = []
    y_sum = 0
    for i in y:
        y_sum += i
        y_pos.append(y_sum)
    z = x_pos
    z.extend(y_pos)
    z.sort()
    z = list(set(z))
    return z


def distances(x):
    x_segments = []
    previous = 0
    for i in x:
        x_segments.append(i - previous)
        previous = i
    return x_segments


def alter(x):
    x_segments = []
    previous = 1
    for i in x:
        level = "H" if previous == 1 else "L"
        x_segments.append("%.2f%s" % (i, level))
        previous *= -1
    return x_segments


x_pos = calcul_points(x)
y_pos = calcul_points(y)
z_pos = merge_points(x_pos, y_pos)
w_pos = asynch_vertlines(x, y)
w_seg = distances(w_pos)
w_seg_level = alter(w_seg)
print("x", x)
print("y ", y)
print("x_pos ", x_pos)
print("y_pos ", y_pos)
print("z_pos ", z_pos)
print("w_pos ", w_pos, z_pos, w_pos == z_pos)
print("segments ", w_seg)
print("signal ", " ".join(w_seg_level))
