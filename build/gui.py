from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, StringVar

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "C:/Users/narma/Desktop/Chirec-Hackathon/build/assets/frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("750x445")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=445,
    width=750,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(508.0, 222.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(508.0, 222.0, image=image_image_2)

canvas.create_text(
    15.0,
    30.0,
    anchor="nw",
    text="Hey there, How are you",
    fill="#1E1E1E",
    font=("SourceSerifPro Regular", -21)
)

canvas.create_text(
    24.0,
    83.0,
    anchor="nw",
    text="We need some basic information to get you started",
    fill="#000000",
    font=("SourceSerifPro Regular", -17)
)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(167.5, 197.0, image=entry_image_1)

name_var = StringVar()
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=name_var
)
entry_1.place(
    x=87.0,
    y=185.0,
    width=161.0,
    height=22.0,
)

canvas.create_text(
    5.0,
    185.0,
    anchor="nw",
    text="Your Name",
    fill="#000000",
    font=("IndieFlower Regular", -15)
)

canvas.create_text(
    13.0,
    219.0,
    anchor="nw",
    text="Age",
    fill="#000000",
    font=("IndieFlower Regular", -15)
)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(168.5, 235.5, image=entry_image_2)

age_var = StringVar()
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=age_var
)
entry_2.place(
    x=89.0,
    y=223.0,
    width=159.0,
    height=23.0
)

canvas.create_text(
    13.0,
    257.0,
    anchor="nw",
    text="Gender",
    fill="#000000",
    font=("IndieFlower Regular", -15)
)

Gender_var = StringVar()
entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(169.5, 269.5, image=entry_image_3)

entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    textvariable=Gender_var
)
entry_3.place(
    x=91.0,
    y=257.0,
    width=157.0,
    height=23.0
)

#button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    #image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    text="Next",
    command=lambda: print(age_var.get(), name_var.get(), Gender_var.get()),
    relief="flat"
)
button_1.place(
    x=130.0,
    y=335.0,
    width=109.0,
    height=27.0
)

canvas.create_text(
    169.0,
    335.0,
    anchor="nw",
    text="Next",
    fill="#000000",
    font=("IndieFlower Regular", -17)
)

window.resizable(True, True)

window.mainloop()
