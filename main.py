import graphics
import random
from math import sin, asin, asinh, cos, acos, acosh, tan, atan, atanh
import pickle
import os

WIDTH, HEIGHT = 800, 800
SCALE = 100
functions = {'sin': sin, 'asin': asin, 'asinh': asinh, 'cos': cos, 'acos': acos, 'acosh': acosh, 'tan': tan, 'atan': atan, 'atanh': atanh}

class Drawing:

    def __init__(self, funcX1, funcX2, funcY1, funcY2):
        self.funcX1 = functions[funcX1]
        self.funcX2 = functions[funcX2]
        self.funcY1 = functions[funcY1]
        self.funcY2 = functions[funcY2]
        self.range_a = (-3, 3)
        self.range_b = (-3, 3)
        self.range_c = (0.5, 1.5)
        self.range_d = (-0.5, 1.5)

    # @classmethod
    # def from_file(self, filename):

    def save_parameters(self):
        name = self.get_funcs_string()
        lengh = len(name)
        path = os.path.join(os.path.dirname(__file__), 'parameters/')
        m = 0
        for filename in os.listdir(path):
            if name in filename:
                num = int(filename.replace('.values', '')[lengh:])
                print(num)
                if m > num:
                    continue
                m = num + 1
        name = name + str(m)
        with open(os.path.join(path, name), 'wb') as f:
            pickle.dump(self, f)
    
    def get_funcs_string(self):
        names = []
        for f in (self.funcX1, self.funcX2, self.funcY1, self.funcY2):
            names.append(list(functions.keys())[list(functions.values()).index(f)])
        return '-'.join(names)

    def custom_range(self, parameter, start, end):
        setattr(self, f'range_{parameter}', (start, end))

    def draw(self, win, count, parameters_text, iterations=30_000, create_new_parameters=True, is_loaded=False):
        if not hasattr(self, 'a') or create_new_parameters:
            self.new_parameters()
        parameters_text.setText(f'a: {self.a}, b: {self.b}, c: {self.c}, d: {self.d}')
        X = Y = 0.1
        for i in range(iterations+1):
            X, Y = self.update(X, Y)
            P = self.get_point(X, Y) 
            P.setFill('white')
            P.draw(win)
            count.setText(i)
            key = win.checkKey()
            if not key:
                continue
            if not is_loaded:
                if key == 'space':
                    return None
                elif key == 'q':
                    return -1
                elif key == 's':
                    self.save_parameters()
                    continue
                elif key == 'f':
                    return 'functions'
                elif key == 'range':
                    return 'range'
            else:
                if key == 'Left':
                    return 0
                elif key == 'Right':
                    return 1
                elif key == 'q':
                    return -1


        return None

    def new_parameters(self):
        self.a = random.uniform(*self.range_a)
        self.b = random.uniform(*self.range_b)
        self.c = random.uniform(*self.range_c)
        self.d = random.uniform(*self.range_d)

    def update(self, x, y):
        X = self.funcX1(y+self.a) + self.c*self.funcX2(x+self.a)
        Y = self.funcY1(x+self.b) + self.d*self.funcY2(y+self.b)
        return X, Y

    def get_point(self, X, Y):
        return graphics.Point(X*SCALE, Y*SCALE)
        

def draw_helpers(win, color='white'):
    t1 = graphics.Text(graphics.Point(-WIDTH/2 + 45, HEIGHT/2 - 15), 'iterations:')
    t1.setFill(color)
    t1.draw(win)

    count = graphics.Text(graphics.Point(-WIDTH/2 + 110, HEIGHT/2 - 16), '0')
    count.setFill(color)
    count.draw(win)

    parameters_text = graphics.Text(graphics.Point(80, HEIGHT/2 - 15), 'a: None,     b: None,     c: None,     d: None')
    parameters_text.setFill(color)
    parameters_text.draw(win)
    return count, parameters_text

def main():
    win = graphics.GraphWin('Trig Chaos Drawing', WIDTH, HEIGHT)
    win.setBackground('black')
    win.setCoords(-WIDTH/2, -HEIGHT/2, WIDTH/2, HEIGHT/2)

    params = input('functions (x1, x2, y1, y2): ').strip()
    while True:
        win.delete('all')
        count, parameters_text = draw_helpers(win, 'blue')
        drawing = Drawing(*params.split())
        key = drawing.draw(win, count, parameters_text)
        if not key:
            continue
        elif key == -1:
            break
        elif key == 'functions':
            params = input('functions (x1, x2, y1, y2): ').strip()

if __name__ == '__main__':
    main()