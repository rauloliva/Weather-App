from tkinter import *
import os
from PIL import Image, ImageTk

FONT_FAMILY = 'Ariel'

class WeatherInterface:

    def __init__(self):
        self.create_window()

        self.create_canvas()

        self.create_title()

        self.window.mainloop()

    def create_window(self):
        self.window = Tk()
        self.window.title('Weather App')
        self.window.config(padx=0, pady=0)

    def create_canvas(self):
        self.canvas = Canvas(width=500, height=750)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        rain_path = os.path.join(script_dir, 'rain.jpg')
        
        img = Image.open(rain_path)
        img = img.resize((500, 750))
        rain = ImageTk.PhotoImage(img)

        self.canvas.create_image(0, 0, image=rain, anchor='nw')
        self.canvas.rain = rain
        self.canvas.config(bg='#B1DDC6', highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=3, rowspan=6)

    def create_title(self):
        self.label = Label(text='Weather App', fg='White', bg='green', font=(FONT_FAMILY, 20, 'bold'))
        self.label.grid(row=0, column=1)