import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas
import tkinter.colorchooser
from tkinter import filedialog

class FractalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fractal Interativo")

        self.canvas = ScrolledCanvas(root)
        self.canvas.pack(fill=tk.BOTH, expand=tk.YES)

        self.turtle = RawTurtle(self.canvas)
        self.turtle.speed(0)
        self.turtle.hideturtle()

        self.order_label = tk.Label(root, text="Ordem:")
        self.order_label.pack(side=tk.LEFT, padx=5)

        self.order_var = tk.IntVar()
        self.order_slider = tk.Scale(root, from_=0, to=5, orient=tk.HORIZONTAL, variable=self.order_var, length=200, label="Ordem")
        self.order_slider.pack(side=tk.LEFT)

        self.size_label = tk.Label(root, text="Tamanho:")
        self.size_label.pack(side=tk.LEFT, padx=5)

        self.size_var = tk.IntVar()
        self.size_slider = tk.Scale(root, from_=1, to=300, orient=tk.HORIZONTAL, variable=self.size_var, length=200, label="Tamanho")
        self.size_slider.pack(side=tk.LEFT)

        self.fractal_type_label = tk.Label(root, text="Tipo de Fractal:")
        self.fractal_type_label.pack(side=tk.LEFT, padx=5)

        self.fractal_type_var = tk.StringVar()
        self.fractal_type_var.set("Koch")
        self.fractal_type_menu = tk.OptionMenu(root, self.fractal_type_var, "Koch", "Árvore", "Cantor")
        self.fractal_type_menu.pack(side=tk.LEFT)

        self.color_button = tk.Button(root, text="Escolher Cor", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=5)

        self.save_button = tk.Button(root, text="Salvar Imagem", command=self.save_image)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.draw_button = tk.Button(root, text="Desenhar Fractal", command=self.draw_fractal)
        self.draw_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = tk.Button(root, text="Limpar", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        self.info_text = tk.Text(root, height=5, width=40)
        self.info_text.pack(pady=10)

    def draw_fractal(self):
        order = self.order_var.get()
        size = self.size_var.get()
        fractal_type = self.fractal_type_var.get()
        color = self.turtle.pencolor()

        self.turtle.clear()
        self.turtle.penup()
        self.turtle.goto(-size / 2, -size / 2)
        self.turtle.pendown()
        self.turtle.pencolor(color)

        if fractal_type == "Koch":
            self.draw_koch_fractal(order, size)
        elif fractal_type == "Árvore":
            self.draw_tree_fractal(order, size)
        elif fractal_type == "Cantor":
            self.draw_cantor_fractal(order, size)

        info = f"Tipo: {fractal_type}\nOrdem: {order}\nTamanho: {size}\nCor: {color}"
        self.info_text.delete(1.0, tk.END)
        self.info_text.insert(tk.END, info)

    def draw_koch_fractal(self, order, size):
        if order == 0:
            self.turtle.forward(size)
        else:
            self.turtle.forward(size / 3)
            self.turtle.left(60)
            self.draw_koch_fractal(order - 1, size / 3)
            self.turtle.right(120)
            self.draw_koch_fractal(order - 1, size / 3)
            self.turtle.left(60)
            self.draw_koch_fractal(order - 1, size / 3)

    def draw_tree_fractal(self, order, size):
        if order == 0:
            self.turtle.forward(size)
        else:
            self.turtle.forward(size)
            self.turtle.left(45)
            self.draw_tree_fractal(order - 1, size * 0.6)
            self.turtle.right(90)
            self.draw_tree_fractal(order - 1, size * 0.6)
            self.turtle.left(45)
            self.turtle.backward(size)

    def draw_cantor_fractal(self, order, size):
        if order == 0:
            self.turtle.forward(size)
        else:
            self.turtle.forward(size / 2)
            self.turtle.penup()
            self.turtle.backward(size)
            self.turtle.pendown()
            self.draw_cantor_fractal(order - 1, size / 3)
            self.turtle.penup()
            self.turtle.forward(size / 2)
            self.turtle.pendown()
            self.draw_cantor_fractal(order - 1, size / 3)

    def choose_color(self):
        color = tk.colorchooser.askcolor()[1]
        self.turtle.pencolor(color)

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".eps", filetypes=[("Encapsulated PostScript", "*.eps")])
        if file_path:
            self.canvas.postscript(file=file_path, colormode='color')

    def clear_canvas(self):
        self.turtle.clear()
        self.info_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = FractalApp(root)
    root.mainloop()
