# import asyncio
# from g4f.client import AsyncClient
#
#
# async def main():
#     client = AsyncClient()
#
#     response = await client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[
#             {
#                 "role": "user",
#                 "content": "Say this is a test"
#             }
#         ],
#         web_search=False
#     )
#
#     print(response.choices[0].message.content)
#
#
# asyncio.run(main())



#
# async def main():
#     client = AsyncClient()
#
#     response = await client.images.generate(
#         prompt="a white dog",
#         model="flux",
#         response_format="url"
#         # Add any other necessary parameters
#     )
#
#     image_url = response.data[0].url
#     print(f"Generated image URL: {image_url}")

#
# asyncio.run(main())

import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import asyncio
from g4f.client import AsyncClient
from translate import Translator


async def gen_url(nm):
    client = AsyncClient()

    response = await client.images.generate(
        prompt=nm,
        model="flux",
        response_format="url"
        # Add any other necessary parameters
    )

    image_url = response.data[0].url
    print(f"Generated image URL: {image_url}")
    return image_url


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

    nm = text.get().strip()
    nm = transl_ru_en.translate(nm.capitalize())
    url = asyncio.run(gen_url(nm))
    if url:
        img = load_image(url)

    if img:
        label.config(image=img)
        label.image = img


if __name__ == '__main__':
    transl_ru_en = Translator(from_lang='ru', to_lang='en')

    # nm = 'Kittes'
    # url = 'https://cataas.com/cat'
    root = tk.Tk()
    root.title('Cats')
    root.geometry('600x600')
    frame1 = tk.Frame(root)
    frame1.pack()
    frame2 = tk.Frame(root)
    frame2.pack()
    text = tk.Entry(frame1, width=40)
    text.grid(row=0, columnspan=2)
    text.insert(0, 'Kittes')
    btn = tk.Button(frame1, text='Forward', width=10, command=open_img)
    btn.grid(row=1, column=0)
    btn_s = tk.Button(frame1, text='Save', width=10, command=open_img)
    btn_s.grid(row=1, column=1)
    label = tk.Label(frame2)
    label.pack()
    open_img()
    # url = asyncio.run(gen_url())
    # img = load_image(url)
    # if img:
    #     label.config(image=img)
    #     label.image = img

    root.mainloop()

