import tkinter as tk
import math

class HeartAnimation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Heart Animation")
        self.canvas = tk.Canvas(self, width=400, height=400, bg='white')
        self.canvas.pack()
        self.draw_heart(200, 200, 50)
        self.animate()

    def draw_heart(self, x, y, size):
        self.canvas.delete("heart")
        self.canvas.create_arc(x - size, y - size, x, y, start=0, extent=180, outline='red', fill='red', tag="heart_left")
        self.canvas.create_arc(x, y - size, x + size, y, start=0, extent=180, outline='red', fill='red', tag="heart_right")
        self.canvas.create_polygon(x - size, y, x, y + size, x + size, y, fill='red', outline='red', tag="heart")

    def animate(self):
        for i in range(50, 100):
            self.draw_heart(200, 200, i)
            self.update()
            self.after(20)
        for i in range(100, 50, -1):
            self.draw_heart(200, 200, i)
            self.update()
            self.after(20)

if __name__ == "__main__":
    app = HeartAnimation()
    app.mainloop()
