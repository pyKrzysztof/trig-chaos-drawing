import graphics
from main import Drawing, draw_helpers
import os
import pickle


WIDTH = 800
HEIGHT = 800
PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'parameters/'))


def load(files, current_idx):
    print(files[current_idx])
    with open(os.path.join(PATH, files[current_idx]), 'rb') as f:
        drawing = pickle.load(f)
    return drawing

def main():
    win = graphics.GraphWin('Trig Chaos Drawing from file', WIDTH, HEIGHT)
    win.setBackground('black')
    win.setCoords(-WIDTH/2, -HEIGHT/2, WIDTH/2, HEIGHT/2)

    files = []
    for f in os.listdir(PATH):
        files.append(f)
    current_idx = 0

    while True:
        win.delete('all')
        count, parameters_text = draw_helpers(win, 'black')
        drawing = load(files, current_idx)
        key = drawing.draw(win, count, parameters_text, iterations=60_000, create_new_parameters=False, is_loaded=True)
        if key is None:
            continue
        elif key == 1:
            current_idx = (current_idx+1) if current_idx+1 < len(files) else current_idx
        elif key == 0:
            current_idx = (current_idx-1) if current_idx-1 > -1 else current_idx
        elif key == -1:
            break


if __name__ == '__main__':
    main()