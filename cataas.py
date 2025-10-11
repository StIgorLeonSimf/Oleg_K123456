from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        image_data = BytesIO(resp.content)
        img = Image.open(image_data)
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)

    except Exception as er:
        print(f'Ошибка - {er}')
        return None


def open_img():
    img = load_image(url)
    if img:
        label.config(image=img)
        label.image = img


root = Tk()
root.title('Cats')
root.geometry('600x600')

btn = Button(root, text='Forward', width=10, command=open_img)
btn.pack(pady=10)
label = Label()
label.pack()
url = 'https://cataas.com/cat'
# img = load_image(url)
# if img:
#     label.config(image=img)
#     label.image = img

root.mainloop()