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
        self.canvas = tk.Canvas(self.top, height=window_size + 50, width=window_size, bg="black")
        
        # Set drawing settings
        self.render_size = window_size * 0.7
        self.start = (window_size / 2) - (self.render_size / 2)
        
        # Get grid size
        self.num = (int(log[0].split(" ")[1]))
        del log[0]

        self.cell_size = self.render_size / self.num
        self.p_open = tk.Label(self.top, text="0.00%", font=("Courier", 18), fg="white", bg="black")
        self.p_percolated = tk.Label(self.top, text="0.00%", font=("Courier", 18), fg="#89CFF0", bg="black")
        self.p_open.place(relx=0.69, rely=0.8)
        self.p_percolated.place(relx=0.51, rely=0.8)

        self.log = log
        self.render()

        time.sleep(20)

    def __draw_square(self, index, percolation=False):
        r, c = (index // self.num, index % self.num)

        y = self.start + (r * self.cell_size)
        x = self.start + (c * self.cell_size)
        
        fill = "#89CFF0" if percolation else "white"
        self.canvas.create_rectangle(x, y, x + self.cell_size - 1, y + self.cell_size - 1,
                    outline="black", fill=fill, width=0)


    def render(self):
        self.canvas.create_line(self.start, self.start - 1, self.start + self.render_size, self.start - 1, fill="#89CFF0", width=2)
        opened = []
        for log in self.log:
            (operation, data) = log.split(" ")

            if operation == "open":
                index = int(data)
                self.__draw_square(index)
                opened.append(index)
                self.p_open.config(text="{p:.2f}%".format(p = len(opened) / (self.num ** 2)))
            elif operation == "percolation":
                indices = [int(s) for s in data.split(",") if int(s) in opened]
                indices.sort()
                indices = indices[:-2]

                for index in indices:
                    self.__draw_square(index, True)

                self.p_percolated.config(text="{p:.2f}%".format(p = len(indices) / (self.num ** 2)))

            self.canvas.pack()
            self.top.update_idletasks()
            self.top.update()
            time.sleep(0.00001)

if __name__ == "__main__":
    p = Percolation(111, logging=True)
    p.percolate()
    v = Visualizer(p.log)
    

    



