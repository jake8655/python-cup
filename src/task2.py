import tkinter as tk
import os
import random

WIDTH = 800
HEIGHT = 600

canvas = tk.Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()


image_files = os.listdir(f"{os.getcwd()}/assets")

animals = list(filter(lambda file: file.startswith("zviera"), image_files))
# randomize animals list so that they are not in the same order all the time
random.shuffle(animals)

steps = list(filter(lambda file: file.startswith("stopy"), image_files))
# select random step
step = random.choice(steps)
photo_images = {"animals": [], "step": None}


def move_to_coords(tag: str, x: int, y: int):
    coords = canvas.coords(tag)
    canvas.move(tag, x - coords[0], y - coords[1])


def click(number: int):
    # check if clicked animal belongs to steps
    if str(number) not in step:
        return

    # move animal to steps
    move_to_coords(f"animal-{number}", 100, 500)
    canvas.update()
    # while animal is on screen move by 50px to the right
    i = 0
    while canvas.coords(f"animal-{number}")[0] < WIDTH + 100:
        i += 1
        canvas.after(500)
        canvas.move(f"animal-{number}", 100, 0)
        canvas.create_image(100 + i * 100, 500, anchor="center", image=photo_images["step"])
        canvas.update()


for idx, file_name in enumerate(animals):
    number = file_name[-5]
    img = tk.PhotoImage(file=f"./assets/{file_name}")
    photo_images["animals"].append(img)

    # draw image
    canvas.create_image(100 + idx * 150, 150, anchor="s", image=photo_images["animals"][-1], tag=f"animal-{number}")
    # add event listener
    canvas.tag_bind(f"animal-{number}", "<Button-1>", func=lambda _, number=number: click(number))

photo_images["step"] = tk.PhotoImage(file=f"./assets/{step}")
number = step[-5]
canvas.create_image(100, 500, anchor="center", image=photo_images["step"], tag=f"step-{number}")

tk.mainloop()
