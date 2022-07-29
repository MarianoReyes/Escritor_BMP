from writeutilities import *


def color(r, g, b):
    return bytes([b, g, r])


BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)


class Render(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.current_color = WHITE
        self.verterx_color = BLACK
        self.clear()

    def createWindow(self, width, height):
        self.width = width
        self.height = height

    def clear(self):
        self.framebuffer = [
            [self.current_color for x in range(self.width)]
            for y in range(self.height)
        ]

    def write(self, filename):
        f = open(filename, 'bw')

        # pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))

        # info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        # pixel data
        for x in range(self.height):
            for y in range(self.width):
                f.write(self.framebuffer[y][x])

        f.close()

    def point(self, x, y):
        if x >= 0 and x <= self.width and y >= 0 and y <= self.height:
            self.framebuffer[x][y] = self.verterx_color

    def convertir_cords(self, x, y):
        if x < -1 or x > 1 or y < -1 or y > 1:
            return

        x = x + 1
        y = y + 1

        x_convertida = (x * self.viewport["width"])/2
        y_convertida = (y * self.viewport["height"])/2

        x_final = int(x_convertida + self.viewport["x"])
        y_final = int(y_convertida + self.viewport["y"])

        return x_final, y_final

    def line(self, x1, y1, x2, y2):
        """
        Draws a line in the screen.
        Input: 
        start: size 2 array with x,y coordinates
        end: size 2 array with x,y coordinates
        """
        x1, y1 = x1, y1
        x2, y2 = x2, y2

        dy = abs(y2 - y1)
        dx = abs(x2 - x1)
        steep = dy > dx

        if steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        dy = abs(y2 - y1)
        dx = abs(x2 - x1)

        offset = 0
        threshold = dx

        y = y1
        for x in range(x1, x2 + 1):
            if steep:
                self.point(y, x)
            else:
                self.point(x, y)

            offset += dy * 2
            if offset >= threshold:
                y += 1 if y1 < y2 else -1
                threshold += dx * 2
