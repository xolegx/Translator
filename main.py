from translib import get_translation
import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import *
import keyboard


def about():
    showinfo("О программе", "Переводчик версия 0.0.0.2 \n\n Made by LEGO")


def trans():
    f = text1.get('1.0', 'end')
    word_end = get_translation(f, lang)['text']
    word = str(word_end[0])
    text2.delete('1.0', 'end')
    text2.insert(INSERT, word)


def change_leng():
    global lang
    if lang == 'en':
        btn_lang.config(image=lang_img_en)
        lang = 'ru'
    else:
        btn_lang.config(image=lang_img_ru)
        lang = 'en'


keyboard.add_hotkey('Ctrl + Enter', trans)
root = tk.Tk()
root.title("Translator")
root.geometry("278x229+870+100")
root.resizable(False, False)
lang_img_ru = tk.PhotoImage(file="D:/PycharmProjects/Translator/lang_ru.gif")
lang_img_en = tk.PhotoImage(file="D:/PycharmProjects/Translator/lang_en.gif")
enter_img = tk.PhotoImage(file="D:/PycharmProjects/Translator/butt.gif")
about_img = tk.PhotoImage(file="D:/PycharmProjects/Translator/about.gif")
en_img = tk.PhotoImage(file="D:/PycharmProjects/Translator/en.gif")
ru_img = tk.PhotoImage(file="D:/PycharmProjects/Translator/ru.gif")
lang = 'ru'
btn_trans = tk.Button(image=enter_img, command=trans)
btn_lang = tk.Button(image=lang_img_en, command=change_leng)
btn_about = tk.Button(image=about_img, command=about)
text1 = Text(width=25, height=5, wrap=WORD)
text2 = Text(width=25, height=5, wrap=WORD)
btn_trans.grid(row=1, column=4)
btn_lang.grid(row=0, column=1)
btn_about.grid(row=0, column=4, sticky=NE)
text1.grid(row=1, column=0, columnspan=4, rowspan=3)
text2.grid(row=4, column=0, columnspan=4, rowspan=3)
Label(image=en_img).grid(row=0, column=0)
Label(image=ru_img).grid(row=0, column=2)

root.mainloop()
