import render

r = None


def glinit():
    return


def glCreateWindow(width, height):
    global r

    w = width % 4
    width_ajustada = width

    if w != 0:
        width_ajustada = width + width % 4

    r = render.Render(width_ajustada, height)


def glViewPort(x, y, width, height):
    global r

    r.viewport = {
        "x": x,
        "y": y,
        "width": width if width < r.width else r.width - x - 1,
        "height": height if height < r.height else r.height - y - 1
    }


def glClear():
    global r
    r.clear()


def glClearColor(red, green, blue):
    global r

    red = int(red*255)
    green = int(green*255)
    blue = int(blue*255)

    r.current_color = color(red, green, blue)


def glVertex(x, y):
    global r

    r.point(* r.convertir_cords(x, y))


def glLine(x0, y0, x1, y1):
    global r

    r.line(
        * r.convertir_cords(x0, y0),
        * r.convertir_cords(x1, y1)
    )


def glColor(red, green, blue):
    global r

    red = int(red*255)
    green = int(green*255)
    blue = int(blue*255)

    r.verterx_color = color(red, green, blue)


def glFinish():
    r.write('imagen.bmp')


def color(r, g, b):
    return bytes([b, g, r])


BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
