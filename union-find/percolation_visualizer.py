import tkinter as tk
from percolation import Percolation
import threading
import time

class Visualizer:
    def __init__(self, log):
        self.open = []
        self.percolation = []

        window_size = 500

        self.top = tk.Tk()
        self.canvas = tk.Canvas(self.top, height=window_size, width=window_size)
        
        # Set drawing settings
        render_size = window_size * 0.7
        self.start = (window_size / 2) - (render_size / 2)
        
        self.num = (int(log[0].split(" ")[1]))
        del log[0]

        self.cell_size = render_size / self.num
        self.log = log

        while len(self.log):
            self.render()

        time.sleep(2)

    def parse_log(self):
        c_log = self.log[0].split(" ")
        del self.log[0]

        op = c_log[0]
        if op == "open":
            self.open.append(int(c_log[1]))
        elif op == "percolation":
            self.percolation = [int(s) for s in c_log[1].split(",")]

    def render(self):
        self.parse_log()
        self.canvas.delete(tk.ALL)

        for r in range(self.num):
            for c in range(self.num):
                y = self.start + (r * self.cell_size)
                x = self.start + (c * self.cell_size)

                index = r * self.num + c
                
                is_open = index in self.open
                is_percolation = index in self.percolation
                
                fill = "black" if not is_open else "yellow" if is_percolation else "white"

                self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size,
                outline="#f11", fill=fill, width=1)

        self.canvas.pack()
        self.top.update_idletasks()
        self.top.update()
        pass


if __name__ == "__main__":
    p = Percolation(30, logging=True)
    p.percolate()
    v = Visualizer(p.log)
    

    



