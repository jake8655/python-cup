import random
import tkinter as tk

WIDTH = 800
HEIGHT = 600

canvas = tk.Canvas(width=WIDTH, height=HEIGHT)
canvas.pack()


def move_to_coords(tag: str, x: int, y: int):
    coords = canvas.coords(tag)
    canvas.move(tag, x - coords[0], y - coords[1])


def event_listener(add: bool, m: int, n: int):
    for i in range(m):
        for j in range(n):
            if add:
                canvas.tag_bind(
                    f"square-{i}-{j}",
                    "<Button-1>",
                    func=lambda _, coords=(i, j): click(coords),
                )
            else:
                canvas.tag_unbind(f"square-{i}-{j}", "<Button-1>")


def generate_play_area(m: int, n: int):
    if (m < 3 or m > 5) or (n < 3 or n > 7):
        raise ValueError("Invalid parameters")

    square_size = 50

    for i in range(m):
        for j in range(n):
            # create a rectangle
            canvas.create_rectangle(  # type: ignore
                200 + i * square_size,
                150 + j * square_size,
                200 + (i + 1) * square_size,
                150 + (j + 1) * square_size,
                tag=f"square-{i}-{j}",
                fill=random.choice(["white", "lightgrey"]),
                outline="black",
                width=2,
            )


m = random.randint(3, 5)
n = random.randint(3, 7)
generate_play_area(m, n)

img = tk.PhotoImage(file="./assets/duch.png")
canvas.create_image(WIDTH // 2, HEIGHT // 2, anchor="center", image=img, tag="ghost")
canvas.itemconfig("ghost", state="hidden")
canvas.update()
canvas.after(1000)

last_square = (0, 0)
iterations = random.randint(3, 5)
for i in range(iterations):
    square = random.randint(0, m - 1), random.randint(0, n - 1)
    if i == iterations - 1:
        last_square = square
    canvas.itemconfig("ghost", state="hidden")
    canvas.update()
    canvas.after(1000)
    move_to_coords("ghost", 225 + square[0] * 50, 175 + square[1] * 50)
    canvas.itemconfig("ghost", state="normal")
    canvas.update()
    canvas.after(500)

canvas.itemconfig("ghost", state="hidden")
canvas.update()
event_listener(True, m, n)


def click(square: tuple[int, int]):
    event_listener(False, m, n)
    text = "SUPER" if square == last_square else "TU SOM"

    canvas.create_text(
        260 + last_square[0] * 50,
        150 + last_square[1] * 50,
        text=text,
        anchor="n",
        font=("Arial", 15),
        fill="purple",
    )
    canvas.itemconfig("ghost", state="normal")
    canvas.update()


tk.mainloop()
