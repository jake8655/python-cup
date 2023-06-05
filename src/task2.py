import tkinter as tk
import os
import re as regex
import random

WIDTH = 800
HEIGHT = 600

canvas = tk.Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()

def click(number):
    print(number)

image_files = os.listdir('assets')
animals = list(filter(lambda file: file.startswith('zviera'), image_files))
steps = list(filter(lambda file: file.startswith('stopy'), image_files))
# select random step
step = random.choice(steps)

photo_images = {'animals': [], 'step': None}
for idx, img in enumerate(animals):
    number = regex.findall(r'\d+', img)[0]
    # button = tk.Button(borderwidth=0, highlightthickness=0)
    # button.pack()
    img = tk.PhotoImage(file=f"assets/{img}")
    photo_images['animals'].append(img)
    # button.bind('<Button-1>', func=click)

    label = tk.Label(image=img, borderwidth=0, highlightthickness=0)
    label.place(x=100+idx*50, y=600, anchor='center')
    label.pack()
    label.bind('<Button-1>', func=lambda x=number: click(number))

    # button.config(image=img, anchor='center')
    # canvas.create_image(100+idx*150, 100, anchor='center', image=photo_images['animals'][-1], tag=f"zviera-{number}")

photo_images['step'] = tk.PhotoImage(file=f"assets/{step}")
number = step[-5]
canvas.create_image(100, 500, anchor='center', image=photo_images['step'], tag=f"step-{number}")

tk.mainloop()
