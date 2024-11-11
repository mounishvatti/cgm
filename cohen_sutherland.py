import matplotlib.pyplot as plt

LEFT, RIGHT, BOTTOM, TOP = 1, 2, 4, 8

def compute_outcode(x, y, xmin, xmax, ymin, ymax):
    code = 0
    if x < xmin: code |= LEFT
    elif x > xmax: code |= RIGHT
    if y < ymin: code |= BOTTOM
    elif y > ymax: code |= TOP
    return code

def cohen_sutherland_line_clip(x0, y0, x1, y1, xmin, xmax, ymin, ymax):
    outcode0 = compute_outcode(x0, y0, xmin, xmax, ymin, ymax)
    outcode1 = compute_outcode(x1, y1, xmin, xmax, ymin, ymax)
    accept = False

    while True:
        if not (outcode0 | outcode1):
            accept = True
            break
        elif outcode0 & outcode1:
            break
        else:
            x, y = 0, 0
            outcode_out = outcode0 if outcode0 else outcode1
            if outcode_out & TOP:
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                y = ymax
            elif outcode_out & BOTTOM:
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                y = ymin
            elif outcode_out & RIGHT:
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                x = xmax
            elif outcode_out & LEFT:
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                x = xmin

            if outcode_out == outcode0:
                x0, y0, outcode0 = x, y, compute_outcode(x, y, xmin, xmax, ymin, ymax)
            else:
                x1, y1, outcode1 = x, y, compute_outcode(x, y, xmin, xmax, ymin, ymax)

    if accept:
        return (x0, y0, x1, y1)
    else:
        return None

# Clipping region
xmin, xmax, ymin, ymax = 1, 10, 1, 10
line = cohen_sutherland_line_clip(0, 5, 12, 5, xmin, xmax, ymin, ymax)

if line:
    plt.plot([line[0], line[2]], [line[1], line[3]], 'bo-')
plt.xlim(0, 12)
plt.ylim(0, 12)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Cohen-Sutherland Line Clipping Algorithm")
plt.show()